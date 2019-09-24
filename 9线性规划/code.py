import numpy as np

z = np.array([2, 3, 1])

a = np.array([[1, 4, 2], [3, 2, 0]])

b = np.array([8, 6])

x1_bound = x2_bound = x3_bound =(0, None)

from scipy import optimize

res = optimize.linprog(z, A_ub=-a, b_ub=-b,bounds=(x1_bound, x2_bound, x3_bound))

print(res)