"""Synthetic grokking and diagnostics data used by the public dashboard.

The curves here are deterministic educational surrogates. They are designed to
show the qualitative behavior discussed in the report: fast memorization,
delayed validation improvement, co-grokking, Reynolds-number difficulty, and
spectral bias under turbulence.
"""

from __future__ import annotations

import numpy as np


def grokking_curves(seed: int = 11) -> dict[str, np.ndarray]:
    """Return loss, accuracy, and co-grokking curves over training epochs."""

    rng = np.random.default_rng(seed)
    epochs = np.arange(0, 20001, 50)

    train_loss = 1.0 / (1.0 + np.exp((epochs - 800) / 300)) + 1e-6
    train_loss += rng.uniform(0, 1e-7, len(epochs))

    val_loss = np.where(
        epochs < 12000,
        0.9 + 0.08 * (epochs / 12000.0) + rng.normal(0, 0.012, len(epochs)),
        0.98 * np.exp(-12.0 * ((epochs - 12000.0) / 8000.0)) + 1e-6,
    )

    train_accuracy = 100.0 / (1.0 + np.exp(-(epochs - 1200) / 250))
    train_accuracy = np.clip(train_accuracy + rng.normal(0, 0.2, len(epochs)), 0.0, 100.0)

    validation_accuracy = np.where(
        epochs < 12000,
        10.0 + 3.0 * (epochs / 12000.0) + rng.normal(0, 0.5, len(epochs)),
        13.0 + 87.0 / (1.0 + np.exp(-5.0 * ((epochs - 12000.0) / 1500.0))),
    )
    validation_accuracy = np.clip(validation_accuracy, 0.0, 100.0)

    geometry_transfer = 100.0 / (1.0 + np.exp(-(epochs - 12200) / 650))
    physics_transfer = 100.0 / (1.0 + np.exp(-(epochs - 12600) / 780))
    co_grokking = np.clip(0.55 * geometry_transfer + 0.45 * physics_transfer, 0.0, 100.0)

    return {
        "epoch": epochs,
        "train_loss": np.clip(train_loss, 1e-7, None),
        "validation_loss": np.clip(val_loss, 1e-7, None),
        "train_accuracy": train_accuracy,
        "validation_accuracy": validation_accuracy,
        "co_grokking_score": co_grokking,
    }


def reynolds_grokking_curves(seed: int = 13) -> dict[str, np.ndarray]:
    """Return required grok epochs for several geometries vs Reynolds number."""

    rng = np.random.default_rng(seed)
    reynolds = np.linspace(100, 10000, 120)
    curves = {
        "wing_0_deg": 7900 + 0.27 * reynolds,
        "ellipse": 5000 + 0.95 * reynolds,
        "circle": 4000 + 1.15 * reynolds,
        "wing_15_deg": 10000 + 0.62 * reynolds,
        "triangle_wedge": 7000 + 2.9 * reynolds,
        "flat_plate": 8000 + 4.7 * reynolds,
    }
    noisy = {name: values + rng.normal(0, 130, len(reynolds)) for name, values in curves.items()}
    noisy["reynolds"] = reynolds
    return noisy


def spectral_bias_curves(seed: int = 17) -> dict[str, np.ndarray]:
    """Return high-frequency representation gap vs turbulence intensity."""

    rng = np.random.default_rng(seed)
    intensity = np.linspace(1.0, 15.0, 80)
    return {
        "turbulence_intensity": intensity,
        "flat_plate": 0.08 + 0.055 * intensity**1.45 + rng.normal(0, 0.07, len(intensity)),
        "circle": 0.04 + 0.035 * intensity**1.30 + rng.normal(0, 0.035, len(intensity)),
        "wing": 0.03 + 0.015 * intensity**1.25 + rng.normal(0, 0.015, len(intensity)),
    }


def activation_spectrum(seed: int = 19) -> dict[str, np.ndarray]:
    """Simulate DFT spectra before and after grokking."""

    rng = np.random.default_rng(seed)
    n = 128
    coordinate = np.linspace(0.0, 2.0 * np.pi, n)
    before = np.zeros(n)
    for frequency in range(1, 15):
        before += rng.uniform(0.05, 0.3) * np.sin(frequency * coordinate + rng.uniform(0.0, 2.0 * np.pi))
    before += rng.normal(0.0, 0.35, n)
    after = 2.5 * np.sin(3.0 * coordinate) + 1.8 * np.cos(7.0 * coordinate) + 0.9 * np.sin(11.0 * coordinate)
    after += rng.normal(0.0, 0.05, n)

    before_power = np.abs(np.fft.fft(before)[: n // 2]) ** 2
    after_power = np.abs(np.fft.fft(after)[: n // 2]) ** 2
    return {
        "frequency_index": np.arange(0, n // 2),
        "before_grokking": before_power / before_power.max(),
        "after_grokking": after_power / after_power.max(),
    }
