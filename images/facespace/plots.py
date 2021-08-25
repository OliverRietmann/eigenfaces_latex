import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
import matplotlib.pyplot as plt

def confidence_ellipse(x, y, ax, alpha, n_std=2.6, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of `x` and `y`

    Parameters
    ----------
    x, y : array_like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    Returns
    -------
    matplotlib.patches.Ellipse

    Other parameters
    ----------------
    kwargs : `~matplotlib.patches.Patch` properties
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0),
        width=ell_radius_x * 2,
        height=ell_radius_y * 2,
        facecolor=facecolor,
        **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate(alpha) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

np.random.seed(1)

phi = 0.0
R = lambda phi: np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])
d = 2.0
D = np.array([[d, 0.0], [0.0, 1.0 / d]])

sigma = 0.2 / d
#x = np.random.uniform(d_inv, 1.0 - d_inv, 50)
#y = np.random.uniform(d_inv, 1.0 - d_inv, 50)
x = np.random.normal(0.55, sigma, 50)
y = np.random.normal(0.4, sigma, 50)
m = np.array([np.mean(x), np.mean(y)])


angle = -0.2 * np.pi
A = R(angle) @ D @ R(-angle)

Z = np.empty((2, len(x)))
Z[0] = x - m[0]
Z[1] = y - m[1]

Z_tilde = A @ Z

x_tilde = Z_tilde[0] + m[0]
y_tilde = Z_tilde[1] + m[1]
#m = np.array([np.mean(x_tilde), np.mean(y_tilde)])

w = np.array([np.cos(angle), np.sin(angle)]) / np.cos(angle)
l = np.linspace(-1.2, 1.2, 10)
v = np.empty((2, len(l)))
v[0] = l * w[0]
v[1] = l * w[1]

plt.figure()
#plt.plot(v[0] + m[0], v[1] + m[1], 'y-', label=r"Affiner Unterraum der Gesichter")
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.plot(x_tilde, y_tilde, 'g.', label=r"Gesichter $\vec{b}_k$")
#plt.plot(v[0], v[1], 'c-', label=r"Unterraum der Differenzgesichter")
plt.plot(x_tilde - m[0], y_tilde - m[1], 'b.', label=r"Differenzgesichter $\vec{a}_k$")
plt.plot(m[0], m[1], 'r.', label=r"Durchschnittsgesicht $\vec{m}$")
plt.xlim(-1.0, 1.0)
plt.ylim(-1.0, 1.0)
#plt.xticks(range(-12, 13, 2))
#plt.yticks(range(-6, 12, 2))
plt.legend(loc='lower left')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid('True')
plt.tight_layout()
plt.savefig('meandiff.pdf', bbox_inches='tight')
plt.close()

fig = plt.figure()
plt.axhline(y=0, color='k', zorder=0)
plt.axvline(x=0, color='k', zorder=1)
plt.plot([0, 0.38 * w[0]], [0, 0.38 * w[1]], 'k--', zorder=2, label="Hauptachsen")
plt.plot([0, -0.09 * w[1]], [0, 0.09 * w[0]], 'k--', zorder=3)
ax = fig.axes[0]
confidence_ellipse(x_tilde - m[0], y_tilde - m[1], ax, 0.235 * np.pi, edgecolor='red', zorder=4)
plt.plot(x_tilde - m[0], y_tilde - m[1], 'b.', label=r"Differenzgesichter $\vec{a}_k$", zorder=5)
plt.arrow(0, 0, 0.04 * w[0], 0.04 * w[1], linewidth=3.0, head_width=0.01, head_length=0.02, fc='c', ec='c', label=r"$\vec{u}_1$ (Hätte eigentlich Länge 1)", zorder=6)
plt.arrow(0, 0, -0.04 * w[1], 0.04 * w[0], linewidth=3.0, head_width=0.01, head_length=0.02, fc='g', ec='g', label=r"$\vec{u}_2$ (Hätte eigentlich Länge 1)", zorder=7)
plt.xlim(-0.4, 0.4)
plt.ylim(-0.4, 0.4)
plt.legend(loc='lower left')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid('True')
plt.tight_layout()
plt.savefig('principal_components.pdf', bbox_inches='tight')
plt.close()
