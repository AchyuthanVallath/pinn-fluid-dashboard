# PINN Fluid Dynamics Dashboard

Interactive scientific dashboard for exploring physics-informed neural network grokking in simplified fluid dynamics.

## Open the Website

- **Immediate public preview:** [Open Dashboard](https://htmlpreview.github.io/?https://github.com/AchyuthanVallath/pinn-fluid-dashboard/blob/main/index.html)
- **GitHub Pages URL after Pages is enabled:** [Open GitHub Pages Site](https://AchyuthanVallath.github.io/pinn-fluid-dashboard/)

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
