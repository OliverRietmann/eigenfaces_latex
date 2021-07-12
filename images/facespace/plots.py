import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

phi = 0.0
R = lambda phi: np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])
d = 10.0
D = np.array([[d, 0.0], [0.0, 1.0 / d]])

d_inv = 1.0 / d
#x = np.random.uniform(d_inv, 1.0 - d_inv, 50)
#y = np.random.uniform(d_inv, 1.0 - d_inv, 50)
x = np.random.normal(0.55, 0.25 * d_inv, 50)
y = np.random.normal(0.4, 0.25 * d_inv, 50)
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
plt.plot(v[0], v[1], 'c-', label=r"Unterraum der Differenzgesichter")
plt.plot(x_tilde - m[0], y_tilde - m[1], 'b.', label=r"Differenzgesichter $\vec{a}_k$")
plt.plot(m[0], m[1], 'r.', label=r"Durchschnittsgesicht $\vec{m}$")
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
#plt.xticks(range(-12, 13, 2))
#plt.yticks(range(-6, 12, 2))
plt.legend(loc='lower left')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid('True')
plt.tight_layout()
plt.savefig('meandiff.png')
plt.close()
