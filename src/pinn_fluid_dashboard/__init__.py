"""Reusable Python backbone for the PINN Fluid Dynamics Dashboard."""

from .flow_surrogate import FlowConfig, velocity_field, pinn_prediction, grok_epoch
from .grokking import grokking_curves, reynolds_grokking_curves, spectral_bias_curves

__all__ = [
    "FlowConfig",
    "velocity_field",
    "pinn_prediction",
    "grok_epoch",
    "grokking_curves",
    "reynolds_grokking_curves",
    "spectral_bias_curves",
]
