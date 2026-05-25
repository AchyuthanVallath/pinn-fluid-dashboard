#  PINN Fluid Dynamics Dashboard

### Full Interactive Scientific Visualization Suite · Physics-Informed Neural Networks · Grokking · CFD Surrogates

<p align="center">
  <img alt="HTML" src="https://img.shields.io/badge/HTML-Canvas-e34c26?style=for-the-badge&logo=html5&logoColor=white">
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-Interactive-f7df1e?style=for-the-badge&logo=javascript&logoColor=111">
  <img alt="MathJax" src="https://img.shields.io/badge/MathJax-LaTeX-0ea5e9?style=for-the-badge">
  <img alt="PINN" src="https://img.shields.io/badge/PINN-Grokking-8b5cf6?style=for-the-badge">
  <img alt="GitHub Pages" src="https://img.shields.io/badge/GitHub%20Pages-Ready-22c55e?style=for-the-badge&logo=github&logoColor=white">
</p>

<p align="center">
  <a href="https://htmlpreview.github.io/?https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/index.html">
    <img alt="Open Dashboard" src="https://img.shields.io/badge/OPEN-DASHBOARD-0ea5e9?style=for-the-badge">
  </a>
  <a href="https://github.com/AchyuthanVallath/pinn-fluid-dashboard/archive/refs/heads/main.zip">
    <img alt="Download ZIP" src="https://img.shields.io/badge/DOWNLOAD-SOURCE%20ZIP-64748b?style=for-the-badge">
  </a>
  <a href="https://AchyuthanVallath.github.io/pinn-fluid-dashboard/">
    <img alt="GitHub Pages" src="https://img.shields.io/badge/GITHUB%20PAGES-LIVE%20SITE-8b5cf6?style=for-the-badge">
  </a>
</p>

<p align="center">
  <strong>An interactive lab-report dashboard exploring physics-informed neural network grokking, fluid-flow visualization, wake profiles, turbulence diagnostics, and PINN/CFD equations.</strong>
</p>

---

## Downloads

<p align="center">
  <a href="https://htmlpreview.github.io/?https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/index.html">
    <img alt="Open public preview" src="https://img.shields.io/badge/OPEN-PUBLIC%20PREVIEW-0284c7?style=for-the-badge">
  </a>
  <a href="https://github.com/AchyuthanVallath/pinn-fluid-dashboard/archive/refs/heads/main.zip">
    <img alt="Download source" src="https://img.shields.io/badge/DOWNLOAD-SOURCE%20CODE%20(.ZIP)-475569?style=for-the-badge">
  </a>
  <a href="https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/index.html">
    <img alt="View index" src="https://img.shields.io/badge/VIEW-index.html-8b5cf6?style=for-the-badge">
  </a>
</p>

## Sections

- **Live Wind Tunnel**: compares a ground-truth flow surrogate against a PINN-style prediction.
- **Shape Benchmark**: compares grokking behavior across circle, ellipse, wedge, plate, and wing geometries.
- **Research Graphs**: shows loss, accuracy, co-grokking, wake profiles, Reynolds number effects, turbulence effects, and spectral bias.
- **Diagnostics**: visualizes activation spectrum, collocation scarcity, geometry snap comparison, and training phase behavior.
- **Architecture**: explains the PINN model structure and AI equations.
- **Physics**: explains governing flow and reliability formulas.
- **Report**: full lab-report style explanation of the project, settings, graphs, equations, limitations, and conclusions.

## GitHub Pages

This repository is ready to publish with GitHub Pages from the `main` branch and repository root. The dashboard entry point is `index.html`.

If the GitHub Pages link is not live yet, open repository **Settings → Pages**, then deploy from branch `main` and folder `/ (root)`.

## Accuracy Notice

This is an educational browser dashboard. It does not claim production CFD accuracy. Real CFD validation would require geometry cleanup, adaptive meshing, mesh independence, residual convergence, mass conservation checks, and benchmark validation.
