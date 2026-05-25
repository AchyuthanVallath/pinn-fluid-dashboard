"""Physics-inspired flow surrogate used by the dashboard.

This module is not a production CFD solver. It builds smooth educational velocity
fields that mimic common flow features: wall slowdown, boundary layers, wakes,
separation, and PINN-style memorization before grokking.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np

ShapeName = Literal["circle", "ellipse", "triangle", "plate", "wing"]
TrainingMode = Literal["separate", "co_grokking"]


@dataclass(frozen=True)
class FlowConfig:
    """Controls the synthetic wind-tunnel and PINN surrogate."""

    nx: int = 320
    ny: int = 160
    x_min: float = 0.0
    x_max: float = 10.0
    y_min: float = -2.5
    y_max: float = 2.5
    center_x: float = 2.2
    center_y: float = 0.0
    wind_speed: float = 1.0
    angle_deg: float = 0.0
    collocation_fraction: float = 0.3
    random_seed: int = 7


GROK_EPOCHS_SEPARATE: dict[ShapeName, int] = {
    "circle": 8000,
    "ellipse": 10000,
    "triangle": 13000,
    "plate": 14500,
    "wing": 16000,
}


def make_grid(config: FlowConfig) -> tuple[np.ndarray, np.ndarray]:
    x = np.linspace(config.x_min, config.x_max, config.nx)
    y = np.linspace(config.y_min, config.y_max, config.ny)
    return np.meshgrid(x, y)


def fbm_noise(x: np.ndarray, y: np.ndarray, phase: float, *, octaves: int = 4, seed: float = 0.0) -> np.ndarray:
    """Small fractal texture used to mimic unsteady turbulent structure."""

    value = np.zeros_like(x, dtype=float)
    amplitude = 0.5
    frequency = 1.0
    for octave in range(octaves):
        p = phase * 0.18 * (octave + 1)
        value += amplitude * (
            np.sin(frequency * x * 1.4 - p + seed + octave * 2.3)
            * np.cos(frequency * y * 2.1 + p * 0.7 + seed)
        )
        amplitude *= 0.52
        frequency *= 2.07
    return np.clip(value + 0.5, 0.0, 1.0)


def _distance_to_shape(x: np.ndarray, y: np.ndarray, shape: ShapeName, config: FlowConfig) -> tuple[np.ndarray, np.ndarray, float, float]:
    """Return distance-like field, inside mask, wake origin, and wake half-width."""

    dx = x - config.center_x
    dy = y - config.center_y

    if shape == "circle":
        radius = 0.55
        distance = np.sqrt(dx**2 + dy**2) / radius - 1.0
        inside = distance <= 0.0
        return distance, inside, config.center_x, 0.55

    if shape == "ellipse":
        distance = np.sqrt((dx / 0.8) ** 2 + (dy / 0.45) ** 2) - 1.0
        inside = distance <= 0.0
        return distance, inside, config.center_x, 0.45

    if shape == "triangle":
        inside = (x >= 1.65) & (x <= 2.75) & (y <= 0.5 * x - 0.825) & (y >= -0.5 * x + 0.825)
        dx_back = np.clip(x - 2.75, 0.0, None)
        dy_top = np.clip(y - (0.5 * x - 0.825), 0.0, None)
        dy_bottom = np.clip((-0.5 * x + 0.825) - y, 0.0, None)
        distance = np.sqrt(dx_back**2 + dy_top**2 + dy_bottom**2)
        distance[inside] = 0.0
        return distance, inside, 2.75, 0.55

    if shape == "plate":
        inside = (x >= 2.16) & (x <= 2.24) & (np.abs(y) <= 0.55)
        dx_plate = np.abs(x - 2.2) - 0.04
        dy_plate = np.abs(y) - 0.55
        distance = np.sqrt(np.clip(dx_plate, 0.0, None) ** 2 + np.clip(dy_plate, 0.0, None) ** 2)
        distance[inside] = 0.0
        return distance, inside, 2.24, 0.65

    chord_start = 1.4
    chord_end = 3.0
    chord = chord_end - chord_start
    thickness = 0.20
    angle = np.deg2rad(config.angle_deg)
    xr = config.center_x + (x - config.center_x) * np.cos(angle) + (y - config.center_y) * np.sin(angle)
    yr = config.center_y - (x - config.center_x) * np.sin(angle) + (y - config.center_y) * np.cos(angle)
    chord_position = np.clip((xr - chord_start) / chord, 0.0, 1.0)
    yt = 5.0 * thickness * chord * (
        0.2969 * np.sqrt(chord_position)
        - 0.1260 * chord_position
        - 0.3516 * chord_position**2
        + 0.2843 * chord_position**3
        - 0.1015 * chord_position**4
    )
    inside = (xr >= chord_start) & (xr <= chord_end) & (np.abs(yr) <= yt)
    distance = np.abs(yr) - yt
    distance[xr < chord_start] = np.sqrt((xr[xr < chord_start] - chord_start) ** 2 + yr[xr < chord_start] ** 2)
    distance[xr > chord_end] = np.sqrt((xr[xr > chord_end] - chord_end) ** 2 + yr[xr > chord_end] ** 2)
    distance[inside] = 0.0
    return distance, inside, chord_end, 0.32


def velocity_field(shape: ShapeName, *, phase: float = 0.0, config: FlowConfig | None = None) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute a normalized velocity-magnitude field for a selected shape."""

    config = config or FlowConfig()
    x, y = make_grid(config)
    distance, inside, wake_origin, wake_width = _distance_to_shape(x, y, shape, config)

    channel_profile = config.wind_speed * 0.85 * (1.0 - (y / 2.6) ** 4)
    boundary_layer = np.clip(1.0 - np.exp(-4.5 * np.maximum(distance, 0.0)), 0.0, 1.0)

    downstream = np.clip(x - wake_origin, 0.0, None)
    spread = wake_width * (1.0 + 0.24 * downstream)
    wake_center = -np.tan(np.deg2rad(config.angle_deg) * 0.45) * downstream if shape == "wing" else 0.0
    wake_profile = np.exp(-1.25 * ((y - wake_center) / np.clip(spread, 1e-5, None)) ** 2)

    transition = np.clip((x - (wake_origin + 2.3)) / 2.4, 0.0, 1.0)
    texture = fbm_noise(x / 2.4, y / 1.9, phase, seed=3.0 + len(shape))
    laminar_defect = 0.55 * wake_profile
    turbulent_defect = 0.70 * wake_profile * (0.35 + 0.85 * texture)
    wake_defect = (1.0 - transition) * laminar_defect + transition * turbulent_defect
    wake_ramp = np.clip((x - wake_origin) / 0.35, 0.0, 1.0)

    velocity = channel_profile * boundary_layer - wake_defect * wake_ramp
    velocity[inside] = 0.0
    return x, y, np.clip(velocity, 0.0, config.wind_speed)


def grok_epoch(shape: ShapeName, training_mode: TrainingMode = "separate") -> int:
    """Epoch where the educational PINN surrogate snaps into generalization."""

    if training_mode == "co_grokking":
        return 12000
    return GROK_EPOCHS_SEPARATE[shape]


def pinn_prediction(
    true_field: np.ndarray,
    epoch: int,
    grok_threshold: int,
    *,
    collocation_fraction: float = 0.3,
    seed: int = 7,
) -> tuple[np.ndarray, bool]:
    """Simulate a PINN prediction before and after grokking.

    Before grokking, the prediction contains structured noise and weakly follows the
    true field. After grokking, it copies the target field to represent the sudden
    generalization transition used in the dashboard story.
    """

    if epoch >= grok_threshold:
        return true_field.copy(), True

    progress = epoch / max(grok_threshold, 1)
    scarcity = 1.0 + 1.2 * (0.3 / max(collocation_fraction, 0.05) - 1.0)
    noise_scale = np.clip(0.55 * (1.0 - 0.25 * progress) * scarcity, 0.0, 1.5)
    rng = np.random.default_rng(seed + epoch)
    noise = rng.normal(0.0, noise_scale, true_field.shape)
    prediction = true_field * (0.08 + 0.18 * progress) + noise
    return np.clip(prediction, 0.0, 1.0), False
