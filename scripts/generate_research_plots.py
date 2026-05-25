"""Generate publication-style research figures for the dashboard.

Run from the repository root:
    python scripts/generate_research_plots.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from pinn_fluid_dashboard.grokking import grokking_curves, reynolds_grokking_curves, spectral_bias_curves

OUT_DIR = Path("plots")


def apply_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 11,
            "axes.labelsize": 12,
            "axes.titlesize": 13,
            "legend.fontsize": 9,
            "figure.dpi": 160,
            "savefig.dpi": 300,
            "axes.grid": True,
            "grid.alpha": 0.35,
            "grid.linestyle": "--",
        }
    )


def save_grokking_plot() -> None:
    data = grokking_curves()
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2), constrained_layout=True)
    fig.suptitle("PINN Grokking: Loss, Accuracy, and Delayed Generalization", fontweight="bold")

    ax = axes[0]
    ax.plot(data["epoch"], data["train_loss"], color="#2563eb", lw=2.4, label="Training loss")
    ax.plot(data["epoch"], data["validation_loss"], color="#dc2626", lw=2.4, label="Validation loss")
    ax.set_yscale("log")
    ax.set_xlabel("Training epochs")
    ax.set_ylabel("Loss magnitude")
    ax.legend(frameon=False)

    ax = axes[1]
    ax.plot(data["epoch"], data["train_accuracy"], color="#2563eb", lw=2.4, label="Training accuracy")
    ax.plot(data["epoch"], data["validation_accuracy"], color="#16a34a", lw=2.4, label="Validation accuracy")
    ax.plot(data["epoch"], data["co_grokking_score"], color="#8b5cf6", lw=2.2, label="Co-grokking score")
    ax.set_xlabel("Training epochs")
    ax.set_ylabel("Accuracy / score (%)")
    ax.set_ylim(0, 105)
    ax.legend(frameon=False)

    fig.savefig(OUT_DIR / "grokking_loss_accuracy_cogrokking.png", bbox_inches="tight")
    plt.close(fig)


def save_reynolds_plot() -> None:
    data = reynolds_grokking_curves()
    spectral = spectral_bias_curves()
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2), constrained_layout=True)
    fig.suptitle("Flow Complexity vs PINN Generalization", fontweight="bold")

    ax = axes[0]
    for name, color in [
        ("wing_0_deg", "#f59e0b"),
        ("ellipse", "#06b6d4"),
        ("circle", "#2563eb"),
        ("wing_15_deg", "#ef4444"),
        ("triangle_wedge", "#8b5cf6"),
        ("flat_plate", "#ec4899"),
    ]:
        ax.plot(data["reynolds"], data[name], lw=2.2, color=color, label=name.replace("_", " "))
    ax.set_xlabel(r"Reynolds number, $Re = \rho U L / \mu$")
    ax.set_ylabel("Required epochs to grok")
    ax.legend(frameon=False, ncol=2)

    ax = axes[1]
    ax.plot(spectral["turbulence_intensity"], spectral["flat_plate"], color="#ec4899", lw=2.6, label="Flat plate")
    ax.plot(spectral["turbulence_intensity"], spectral["circle"], color="#2563eb", lw=2.6, label="Circle")
    ax.plot(spectral["turbulence_intensity"], spectral["wing"], color="#f59e0b", lw=2.6, label="Wing")
    ax.set_xlabel(r"Turbulence intensity, $I = u' / U_\infty$ (%)")
    ax.set_ylabel(r"Spectral representation gap, $||\hat a_{high}|| / ||\hat a_{low}||$")
    ax.legend(frameon=False)

    fig.savefig(OUT_DIR / "reynolds_turbulence_grokking.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    apply_style()
    save_grokking_plot()
    save_reynolds_plot()
    print(f"Saved research figures to {OUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
