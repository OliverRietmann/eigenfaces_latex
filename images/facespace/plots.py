import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

m = np.array([2.0, 6.0])

phi = 0.0
R = lambda phi: np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])
d = 5.0
D = np.array([[d, 0.0], [0.0, 1.0 / d]])

x = np.random.normal(0.0, 1.0, 50)
y = np.random.normal(0.0, 1.0, 50)

angle = 0.5
A = R(angle) @ D @ R(-angle)

Z = np.empty((2, len(x)))
Z[0] = x
Z[1] = y

Z_tilde = A @ Z

x_tilde = Z_tilde[0]
y_tilde = Z_tilde[1]

w = np.array([np.cos(angle), np.sin(angle)]) / np.cos(angle)
l = np.linspace(-12, 13, 10)
v = np.empty((2, len(l)))
v[0] = l * w[0]
v[1] = l * w[1]

plt.figure()
#plt.plot(v[0] + m[0], v[1] + m[1], 'y-', label=r"Affiner Unterraum der Gesichter")
plt.plot(x_tilde + m[0], y_tilde + m[1], 'g.', label=r"Gesichter $b_k$")
plt.plot(v[0], v[1], 'c-', label=r"Unterraum der Differenzgesichter")
plt.plot(x_tilde, y_tilde, 'b.', label=r"Differenzgesichter $a_k$")
plt.plot(m[0], m[1], 'r.', label=r"Durchschnittsgesicht $m$")
plt.xlim(-12.0, 12.0)
plt.xticks(range(-12, 13, 2))
plt.yticks(range(-6, 12, 2))
plt.legend(loc='lower right')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid('True')
plt.tight_layout()
plt.savefig('meandiff.png')
plt.close()
