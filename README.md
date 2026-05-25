# PINN Fluid Dynamics Dashboard

Interactive scientific dashboard for exploring physics-informed neural network grokking in simplified fluid dynamics.

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

Public URL after Pages is enabled:

```text
https://AchyuthanVallath.github.io/pinn-fluid-dashboard/
```

## Accuracy Notice

This is an educational browser dashboard. It does not claim production CFD accuracy. Real CFD validation would require geometry cleanup, adaptive meshing, mesh independence, residual convergence, mass conservation checks, and benchmark validation.
