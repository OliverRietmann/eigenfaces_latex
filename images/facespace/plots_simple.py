import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'mathtext.fontset': 'stix'})
plt.rcParams.update({'font.family': 'STIXGeneral'})
plt.rcParams.update({'font.size': 12})

x = np.array([-4.0, 9.0, 1.0])
y = np.array([-5.0, -5.0, 7.0])
m = np.array([np.mean(x), np.mean(y)])

x_tilde = np.append(x, [x[0]])
y_tilde = np.append(y, [y[0]])

plt.figure()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.plot(x_tilde, y_tilde, 'go--', label=r"$B_k$")
plt.plot(x_tilde - m[0], y_tilde - m[1], 'bo--', label=r"$A_k$")
plt.plot(m[0], m[1], 'ro', label=r"$M$")
plt.xlim(-10.0, 10.0)
plt.ylim(-10.0, 10.0)
plt.xticks(range(-10, 11, 2))
plt.yticks(range(-10, 11, 2))

plt.text(m[0] - 0.7, m[1], r'$M$', color='r', horizontalalignment='center', verticalalignment='center')

caption = [r'$B_{0}$'.format(i + 1) for i in range(3)]
shift = [(-0.7, -0.5), (0.7, -0.5), (0.0, 0.7)]
for xi, yi, caption, s in zip(x, y, caption, shift):
    plt.text(xi + s[0], yi + s[1], caption, fontsize='x-large', color='g', horizontalalignment='center', verticalalignment='center')

caption = [r'$A_{0}$'.format(i + 1) for i in range(3)]
for xi, yi, caption, s in zip(x, y, caption, shift):
    plt.text(xi + s[0] - m[0], yi + s[1] - m[1], caption, fontsize='x-large', color='b', horizontalalignment='center', verticalalignment='center')

#plt.legend(loc='lower left')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid('True')
plt.tight_layout()
plt.savefig('meandiff_simple.pdf', bbox_inches='tight')
plt.close()
