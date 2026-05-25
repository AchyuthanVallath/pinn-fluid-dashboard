"""Optional Streamlit interface for the Python backbone.

The main public dashboard is `index.html` on GitHub Pages. This file exists so
people can also inspect and run the Python surrogate that inspired the browser
visualization.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import streamlit as st

from pinn_fluid_dashboard.flow_surrogate import FlowConfig, grok_epoch, pinn_prediction, velocity_field

st.set_page_config(page_title="PINN Fluid Dashboard - Python", layout="wide")
st.title("PINN Fluid Dynamics Dashboard - Python Backbone")
st.caption("Educational flow surrogate and grokking simulation. Not a production CFD solver.")

with st.sidebar:
    shape = st.selectbox("Geometry", ["circle", "ellipse", "triangle", "plate", "wing"])
    training_mode = st.selectbox("Training mode", ["separate", "co_grokking"])
    epoch = st.slider("Training epoch", 0, 20000, 8500, 500)
    angle = st.slider("Wing angle of attack", -90, 90, 0, 1)
    wind_speed = st.slider("Wind speed scale", 0.2, 2.0, 1.0, 0.1)
    collocation = st.slider("Collocation fraction", 0.05, 0.9, 0.3, 0.05)

config = FlowConfig(angle_deg=float(angle), wind_speed=float(wind_speed), collocation_fraction=float(collocation))
x, y, truth = velocity_field(shape, phase=epoch / 2500.0, config=config)
threshold = grok_epoch(shape, training_mode=training_mode)
prediction, is_grokked = pinn_prediction(
    truth,
    epoch,
    threshold,
    collocation_fraction=collocation,
    seed=config.random_seed,
)

st.metric("Grok threshold", f"{threshold:,} epochs", "generalized" if is_grokked else "still memorizing")

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)
for ax, field, title in [
    (axes[0], truth, "Ground-truth surrogate"),
    (axes[1], prediction, "PINN prediction"),
]:
    image = ax.imshow(field, extent=[0, 10, -2.5, 2.5], origin="lower", cmap="turbo", vmin=0, vmax=wind_speed, aspect="auto")
    ax.set_title(title)
    ax.set_xlabel("x position")
    ax.set_ylabel("y position")
fig.colorbar(image, ax=axes, shrink=0.82, label="normalized velocity magnitude")
st.pyplot(fig, clear_figure=True)

st.markdown(
    """
### What this shows

The left panel is a physics-inspired target field. The right panel is a simulated
PINN output. Before the grok threshold, the model behaves like it has memorized
partial structure but has not generalized. After the threshold, the prediction
snaps toward the target field.

This is a teaching model for visualization and interpretation. A real CFD/PINN
study would need validated geometry, mesh independence, residual convergence,
force convergence, and benchmark comparison before making accuracy claims.
"""
)
