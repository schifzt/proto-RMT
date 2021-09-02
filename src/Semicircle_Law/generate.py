#!/usr/bin/env python3

import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


n = 5000

params = np.array([n])
np.savetxt('params.csv', params, delimiter=',', fmt='%.3f')

# Generate a Gaussian Orthogonal Ensemble(GOE)
# X: n x n matrices
#     X_ij: N(0,4)
# Y: n x n symmetric matrices
#     Y_ij: N(0,1)
#     Y_ii: N(0,2)

mean = np.zeros(n)
cov = np.identity(n)*4
X = np.random.multivariate_normal(mean, cov, n)
M = (X + X.T)/2
M[np.diag_indices(n)] = np.diag(M)/np.sqrt(2)
Y = X / np.sqrt(n)

eigenvals = np.linalg.eigvals(Y)

# eigenvals must be 2 x n array
eigenvals = np.array([eigenvals.real, eigenvals.imag])

np.savetxt('eigenvals.csv', eigenvals, delimiter=',', fmt='%.3f')


# Generate p.d.f. points
#     y = 1/(2*pi)*np.sqrt(4-x**2)

step = 0.025
x = np.arange(-3.0, 3.0, step)
y = np.arange(0.0, 1.0, step)
x, y = np.meshgrid(x, y)
z = x**2 + (2*np.pi*y)**2

fig, ax = plt.subplots()
cs = ax.contour(x, y, z, [4])

p = cs.collections[0].get_paths()[0]
v = p.vertices
x = v[:, 0]
y = v[:, 1]

points = np.array([x, y])

np.savetxt('density.csv', points, delimiter=',', fmt='%.3f')
