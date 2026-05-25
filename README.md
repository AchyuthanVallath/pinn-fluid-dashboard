# PINN Fluid Dynamics Dashboard

### Full Interactive Scientific Visualization Suite · Physics-Informed Neural Networks · Grokking · CFD Surrogates

<p align="center">
  <img alt="HTML" src="https://img.shields.io/badge/HTML-Canvas-e34c26?style=for-the-badge&logo=html5&logoColor=white">
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-Interactive-f7df1e?style=for-the-badge&logo=javascript&logoColor=111">
  <img alt="Python" src="https://img.shields.io/badge/Python-Backbone-3776ab?style=for-the-badge&logo=python&logoColor=white">
  <img alt="MathJax" src="https://img.shields.io/badge/MathJax-LaTeX-0ea5e9?style=for-the-badge">
  <img alt="PINN" src="https://img.shields.io/badge/PINN-Grokking-8b5cf6?style=for-the-badge">
  <img alt="GitHub Pages" src="https://img.shields.io/badge/GitHub%20Pages-Ready-22c55e?style=for-the-badge&logo=github&logoColor=white">
</p>

<p align="center">
  <a href="https://AchyuthanVallath.github.io/pinn-fluid-dashboard/">
    <img alt="Open Dashboard" src="https://img.shields.io/badge/OPEN-DASHBOARD-0ea5e9?style=for-the-badge">
  </a>
  <a href="https://github.com/AchyuthanVallath/pinn-fluid-dashboard/tree/main/src/pinn_fluid_dashboard">
    <img alt="Python Backbone" src="https://img.shields.io/badge/PYTHON-BACKBONE-2563eb?style=for-the-badge">
  </a>
  <a href="https://github.com/AchyuthanVallath/pinn-fluid-dashboard/archive/refs/heads/main.zip">
    <img alt="Download ZIP" src="https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-64748b?style=for-the-badge">
  </a>
</p>

<p align="center">
  <strong>An interactive lab-report dashboard exploring physics-informed neural network grokking, fluid-flow visualization, wake profiles, turbulence diagnostics, and PINN/CFD equations.</strong>
</p>

---

## Downloads

<p align="center">
  <a href="https://AchyuthanVallath.github.io/pinn-fluid-dashboard/">
    <img alt="Open GitHub Pages site" src="https://img.shields.io/badge/OPEN-GITHUB%20PAGES%20SITE-0284c7?style=for-the-badge">
  </a>
  <a href="https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/CODE_GUIDE.md">
    <img alt="Code guide" src="https://img.shields.io/badge/READ-CODE%20GUIDE-8b5cf6?style=for-the-badge">
  </a>
  <a href="https://github.com/AchyuthanVallath/pinn-fluid-dashboard/archive/refs/heads/main.zip">
    <img alt="Download source" src="https://img.shields.io/badge/DOWNLOAD-SOURCE%20CODE%20(.ZIP)-475569?style=for-the-badge">
  </a>
</p>

## Public Code

The repository now includes the Python backbone behind the project narrative:

- [`src/pinn_fluid_dashboard/flow_surrogate.py`](https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/src/pinn_fluid_dashboard/flow_surrogate.py): educational wind-tunnel velocity fields, geometry distance functions, boundary-layer damping, wake defects, angle of attack, grok thresholds, and simulated PINN predictions.
- [`src/pinn_fluid_dashboard/grokking.py`](https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/src/pinn_fluid_dashboard/grokking.py): loss, accuracy, co-grokking, Reynolds-number, turbulence, and activation-spectrum diagnostics.
- [`scripts/generate_research_plots.py`](https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/scripts/generate_research_plots.py): recreates research-style plots from the Python data generators.
- [`streamlit_app.py`](https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/streamlit_app.py): optional Python interface for the same surrogate model.
- [`CODE_GUIDE.md`](https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/CODE_GUIDE.md): explains how to run and interpret the code.

## Run The Python Version

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set PYTHONPATH=src
streamlit run streamlit_app.py
```

Generate the research plots:

```bash
set PYTHONPATH=src
python scripts/generate_research_plots.py
```

## Sections

- **Live Wind Tunnel**: compares a ground-truth flow surrogate against a PINN-style prediction.
- **Shape Benchmark**: compares grokking behavior across circle, ellipse, wedge, plate, and wing geometries.
- **Research Graphs**: shows loss, accuracy, co-grokking, wake profiles, Reynolds number effects, turbulence effects, and spectral bias.
- **Diagnostics**: visualizes activation spectrum, collocation scarcity, geometry snap comparison, and training phase behavior.
- **Architecture**: explains the PINN model structure and AI equations.
- **Physics**: explains governing flow and reliability formulas.
- **Report**: full lab-report style explanation of the project, settings, graphs, equations, limitations, and conclusions.



## Accuracy Notice

This is an educational browser dashboard. It does not claim production CFD accuracy. Real CFD validation would require geometry cleanup, adaptive meshing, mesh independence, residual convergence, mass conservation checks, and benchmark validation.
