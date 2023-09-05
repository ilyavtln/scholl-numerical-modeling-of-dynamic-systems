import numpy as np
import pandas as pd

h1, h2, h3 = 0.1, 0.05, 0.025  # step sizes
y = 1.0  # initial condition

# creating grids
grid1 = np.arange(0, 1 + h1, h1)
grid2 = np.arange(0, 1 + h2, h2)
grid3 = np.arange(0, 1 + h3, h3)


# defining functions
def f(t, y):
    return 2 * t * y


def f_solve(t):
    return np.exp(t * t)


num_result, real_result = [], []

num_result.append(y)

for i in grid1:
    y_new = y + h1 * f(i, y)
    num_result.append(y_new)

    y_new_real = f_solve(i)
    real_result.append(y_new_real)
    y = y_new

y_new_real = f_solve(1)
real_result.append(y_new_real)

error = np.absolute(np.array(num_result) - np.array(real_result))

error_scientific = []
for x in error:
    error_scientific.append('{:.2e}'.format(x))

df1 = pd.DataFrame([grid1, real_result, num_result, error_scientific]).T
df1.columns = ['t', 'y_real', 'y_num (M1)', '|y_num-y_real| (M1)']

print(df1)
num_result = []
y = 1.0
num_result.append(y)

for i in grid1:
    y_new = y + (h1 / 2.0) * (f(i, y) + f(i + h1, y + h1 * f(i, y)))
    num_result.append(y_new)
    y = y_new

error = np.absolute(np.array(num_result) - np.array(real_result))

error_scientific = []
for x in error:
    error_scientific.append('{:.2e}'.format(x))

df2 = pd.DataFrame([num_result, error_scientific]).T
df2.columns = ['y_num (M2)', '|y_num-y_real| (M2)']

print(df2)
