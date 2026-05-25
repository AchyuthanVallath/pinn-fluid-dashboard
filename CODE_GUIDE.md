# Code Guide

This repository contains two layers:

1. `index.html` is the public GitHub Pages dashboard.
2. `src/pinn_fluid_dashboard/` is the Python backbone used to explain and reproduce the main ideas behind the dashboard.

## Python Files

- `src/pinn_fluid_dashboard/flow_surrogate.py` builds the educational wind-tunnel fields. It contains shape distance functions, boundary-layer damping, downstream wake deficits, turbulence texture, grok thresholds, and simulated PINN predictions.
- `src/pinn_fluid_dashboard/grokking.py` creates deterministic research-style data for loss, accuracy, co-grokking, Reynolds-number difficulty, turbulence spectral bias, and activation-spectrum diagnostics.
- `scripts/generate_research_plots.py` renders publication-style figures into a local `plots/` directory.
- `streamlit_app.py` is an optional Python interface for the same ideas. The website does not require Streamlit, but this file makes the backbone easy to run locally.

## Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Generate figures:

```bash
set PYTHONPATH=src
python scripts/generate_research_plots.py
```

Run the optional Streamlit version:

```bash
set PYTHONPATH=src
streamlit run streamlit_app.py
```

On macOS/Linux, replace `set PYTHONPATH=src` with `export PYTHONPATH=src`.

## Scientific Scope

The Python code is a physics-inspired educational surrogate, not a production CFD solver. It demonstrates qualitative ideas:

- Boundary layers reduce velocity near solid geometry.
- Wakes form behind bluff or streamlined bodies.
- Higher geometry complexity and turbulence delay generalization.
- PINN-like training can show an apparent phase transition from memorization to generalization.
- Co-grokking describes shared representation learning across related flow tasks.

## Accuracy Notice

Do not use these fields as validated CFD results. A real solver would require geometry cleanup, adaptive meshing, mesh independence, residual convergence, CFL control, conservation checks, force convergence, and benchmark validation.
