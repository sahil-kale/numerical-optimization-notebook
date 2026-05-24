import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Convexity: Visual Definitions", fontsize=14, fontweight="bold")

# ── Panel 1: Convex Set ──────────────────────────────────────────────────────
ax = axes[0]
ax.set_title("Convex Set\n" r"$\theta x + (1-\theta)y \in C \;\forall\, x,y \in C,\; \theta \in [0,1]$",
             fontsize=10)

theta_fill = np.linspace(0, 2 * np.pi, 300)
rx, ry = 2.0, 1.2
cx, cy = 0.0, 0.0
xs = cx + rx * np.cos(theta_fill)
ys = cy + ry * np.sin(theta_fill)
ax.fill(xs, ys, alpha=0.25, color="steelblue", label="Convex set $C$")
ax.plot(xs, ys, color="steelblue", linewidth=1.5)

x1, y1 = -1.4, -0.5
x2, y2 = 1.2, 0.7
ax.plot([x1, x2], [y1, y2], "k--", linewidth=1.5, label=r"Segment $\theta x+(1-\theta)y$")

for theta in np.linspace(0, 1, 9):
    px = theta * x1 + (1 - theta) * x2
    py = theta * y1 + (1 - theta) * y2
    ax.plot(px, py, "ko", markersize=3)

ax.plot(x1, y1, "rs", markersize=8, zorder=5, label="$x$")
ax.plot(x2, y2, "b^", markersize=8, zorder=5, label="$y$")
ax.text(x1 - 0.15, y1 - 0.25, "$x$", fontsize=11, color="red")
ax.text(x2 + 0.08, y2 + 0.12, "$y$", fontsize=11, color="blue")

ax.set_xlim(-3, 3)
ax.set_ylim(-2, 2)
ax.set_aspect("equal")
ax.legend(fontsize=8, loc="upper left")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")

# ── Panel 2: Non-Convex Set (contrast) ──────────────────────────────────────
ax = axes[1]
ax.set_title("Non-Convex Set\n(segment leaves the set)", fontsize=10)

# crescent: large circle minus an offset smaller circle
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

big = np.linspace(0, 2 * np.pi, 300)
bx = 1.8 * np.cos(big)
by = 1.8 * np.sin(big)
cut_x = 0.9 + 1.4 * np.cos(big)
cut_y = 0.0 + 1.4 * np.sin(big)

ax.fill(bx, by, alpha=0.25, color="steelblue")
ax.plot(bx, by, color="steelblue", linewidth=1.5, label="Non-convex set $C$")
ax.fill(cut_x, cut_y, alpha=1.0, color="white")
ax.plot(cut_x, cut_y, color="steelblue", linewidth=1.5)

x1, y1 = -1.3, 0.3
x2, y2 = 1.1, 0.9
ax.plot([x1, x2], [y1, y2], "r--", linewidth=1.8, label="Segment exits $C$")
ax.plot(x1, y1, "rs", markersize=8, zorder=5)
ax.plot(x2, y2, "b^", markersize=8, zorder=5)
ax.text(x1 - 0.15, y1 - 0.25, "$x$", fontsize=11, color="red")
ax.text(x2 + 0.08, y2 + 0.12, "$y$", fontsize=11, color="blue")

ax.set_xlim(-3, 3)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect("equal")
ax.legend(fontsize=8, loc="upper left")
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")

# ── Panel 3: Convex Function ──────────────────────────────────────────────────
ax = axes[2]
ax.set_title("Convex Function\n" r"$f(\theta x+(1-\theta)y) \leq \theta f(x)+(1-\theta)f(y)$",
             fontsize=10)

t = np.linspace(-2, 2, 400)
f = t ** 2

ax.plot(t, f, "steelblue", linewidth=2, label=r"$f(x) = x^2$")

x_a, x_b = -1.5, 1.2
f_a, f_b = x_a ** 2, x_b ** 2

# chord between (x_a, f_a) and (x_b, f_b)
ax.plot([x_a, x_b], [f_a, f_b], "k--", linewidth=1.8, label="Chord (RHS)")

# pick theta = 0.35
theta = 0.35
x_mid = theta * x_a + (1 - theta) * x_b
f_mid_func = x_mid ** 2                          # f(θx + (1-θ)y)  — on curve
f_mid_chord = theta * f_a + (1 - theta) * f_b   # θf(x)+(1-θ)f(y) — on chord

ax.plot(x_a, f_a, "rs", markersize=9, zorder=5, label=f"$x={x_a}$")
ax.plot(x_b, f_b, "b^", markersize=9, zorder=5, label=f"$y={x_b}$")

ax.plot(x_mid, f_mid_func, "go", markersize=9, zorder=6, label=r"$f(\theta x+(1-\theta)y)$")
ax.plot(x_mid, f_mid_chord, "ms", markersize=9, zorder=6, label=r"$\theta f(x)+(1-\theta)f(y)$")

# vertical gap arrow
ax.annotate("", xy=(x_mid, f_mid_chord), xytext=(x_mid, f_mid_func),
            arrowprops=dict(arrowstyle="<->", color="green", lw=1.5))
ax.text(x_mid + 0.07, (f_mid_func + f_mid_chord) / 2,
        r"$\leq$  (gap)", fontsize=9, color="green")

ax.text(x_a - 0.08, f_a + 0.15, "$x$", fontsize=11, color="red", ha="right")
ax.text(x_b + 0.05, f_b + 0.15, "$y$", fontsize=11, color="blue")

ax.set_xlim(-2.3, 2.3)
ax.set_ylim(-0.3, 5)
ax.legend(fontsize=7.5, loc="upper center")
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")

plt.tight_layout()
plt.savefig("convexity.png", dpi=150, bbox_inches="tight")
print("Saved convexity.png")
plt.show()
