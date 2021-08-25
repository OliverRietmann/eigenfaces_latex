import numpy as np
import matplotlib.pyplot as plt

x = np.array([-4.0, 9.0, 1.0])
y = np.array([-5.0, -5.0, 7.0])
m = np.array([np.mean(x), np.mean(y)])

x_tilde = np.append(x, [x[0]])
y_tilde = np.append(y, [y[0]])

plt.figure()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.plot(x_tilde, y_tilde, 'go--', label=r"$\vec{b}_k$")
plt.plot(x_tilde - m[0], y_tilde - m[1], 'bo--', label=r"$\vec{a}_k$")
plt.plot(m[0], m[1], 'ro', label=r"$\vec{m}$")
plt.xlim(-10.0, 10.0)
plt.ylim(-10.0, 10.0)
plt.xticks(range(-10, 11, 2))
plt.yticks(range(-10, 11, 2))

plt.text(m[0] - 0.7, m[1], r'$\vec{m}$', color='r', horizontalalignment='center', verticalalignment='center')

caption = [r'$\vec{{b}}_{0}$'.format(i + 1) for i in range(3)]
shift = [(-0.7, -0.5), (0.7, -0.5), (0.0, 0.7)]
for xi, yi, caption, s in zip(x, y, caption, shift):
    plt.text(xi + s[0], yi + s[1], caption, color='g', horizontalalignment='center', verticalalignment='center')

caption = [r'$\vec{{a}}_{0}$'.format(i + 1) for i in range(3)]
for xi, yi, caption, s in zip(x, y, caption, shift):
    plt.text(xi + s[0] - m[0], yi + s[1] - m[1], caption, color='b', horizontalalignment='center', verticalalignment='center')

#plt.legend(loc='lower left')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid('True')
plt.tight_layout()
plt.savefig('meandiff_simple.pdf', bbox_inches='tight')
plt.close()
