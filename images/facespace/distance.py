import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'mathtext.fontset': 'stix'})
plt.rcParams.update({'font.family': 'STIXGeneral'})
plt.rcParams.update({'font.size': 12})

u = np.array([4.0, -3.0]) / 5.0

a = np.array([1.0, -2.0])
d = np.inner(a, u) * u

g = lambda x: u[1] / u[0] * x
x = np.linspace(-1.0, 3.0, 2, endpoint=True)
y = g(x)

plt.figure()
plt.axhline(y=0, color='k', zorder=2)
plt.axvline(x=0, color='k', zorder=3)
plt.plot(x, y, 'k--', linewidth=1.0, zorder=4)
plt.plot(a[0], a[1], 'bo', label=r"$\vec{a}$", zorder=5)
plt.plot([a[0], d[0]], [a[1], d[1]], 'b--', zorder=6)
plt.arrow(0.0, 0.0, a[0], a[1], linewidth=1.1, head_width=0.1, head_length=0.1, fc='b', ec='b', label=r"$A$", zorder=7, length_includes_head=True)
#m[0], m[1], m[0] + u[0], m[1] + u[1]
plt.arrow(0.0, 0.0, u[0], u[1], linewidth=1.1, head_width=0.1, head_length=0.1, fc='c', ec='c', label=r"$\vec{u}$", zorder=8, length_includes_head=True)
plt.plot(d[0], d[1], 'ko', label=r"$L$", zorder=9)

plt.text(0.5 * a[0] - 0.05, 0.5 * a[1] - 0.05, r'$\vec{a}$', fontsize='x-large', color='b', horizontalalignment='right', verticalalignment='top')
plt.text(a[0] + 0.1, a[1] - 0.1, r'$A$', fontsize='x-large', color='b', horizontalalignment='left', verticalalignment='center')
plt.text(0.5 * u[0], 0.5 * u[1], r'$\vec{u}$', fontsize='x-large', color='c', horizontalalignment='left', verticalalignment='bottom')
plt.text(d[0] + 0.05, d[1] + 0.05, r'$L$', fontsize='x-large', color='k', horizontalalignment='left', verticalalignment='bottom')
plt.text(0.5 * (a[0] + d[0]) + 0.1, 0.5 * (a[1] + d[1]) - 0.1, r'$d$', fontsize='x-large', color='b', horizontalalignment='center', verticalalignment='center')

plt.xlim(-1.0, 3.0)
plt.ylim(-3.0, 1.0)
plt.xticks(np.arange(-1.0, 3.5, 0.5))
plt.yticks(np.arange(-3.0, 1.5, 0.5))
#plt.legend(loc='lower left')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid('True')
plt.tight_layout()
plt.savefig('distance_simple.pdf', bbox_inches='tight')
plt.close()
