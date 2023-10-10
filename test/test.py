import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

interval = [0, 1]


def make_grid(h):
    return np.arange(interval[0], interval[1], h)


def analytical(h):
    analytical = []
    grid = make_grid(h)
    for tn in grid:
        yn_1 = f_solve(tn)
        analytical.append(yn_1)
    analytical.append(f_solve(grid[-1] + grid[1]))
    return analytical


def make_results(grid, analytical, numerical):
    error = np.absolute(np.array(numerical) - np.array(analytical))
    error_scientific = []
    for x in error:
        error_scientific.append('{:.2e}'.format(x))
    df = pd.DataFrame([grid, analytical, numerical, error_scientific]).T
    df_middle = pd.DataFrame(['...', '...', '...', '...']).T.rename(index={0: '...'})
    df_middle.columns = ['t', 'analytical', 'numerical', '|numerical-analytical|']
    df.columns = ['t', 'analytical', 'numerical', '|numerical-analytical|']
    df.loc[len(grid), 't'] = grid[-1] + grid[1]
    make_plots(grid, analytical, numerical, error)
    return pd.concat([df.head(), df_middle, df.tail()])


def make_plots(grid, analytical, numerical, error):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    grid = np.append(grid, grid[-1] + grid[1])
    ax1.plot(error, grid,
             marker='s', markersize=9, markerfacecolor='blue',
             linestyle='-', linewidth=5,
             color='cyan')
    ax1.grid(color='grey', linestyle='dotted')
    ax1.set_xlabel('error', fontsize=15)
    ax1.set_ylabel('t', fontsize=15)
    ax2.plot(grid, numerical, 'b-', label='numerical', alpha=0.50, linewidth=2)
    ax2.plot(grid, analytical, 'g:', label='analytical', alpha=0.75, linewidth=5)
    ax2.legend(loc='upper center', frameon=False)
    ax2.set_xlabel('y', fontsize=15)
    ax2.set_ylabel('t', fontsize=15)


# computes first n numerical values using classical runge-kutta method
def compute_first_elements(h, n):
    yn = 1.0
    elements = []
    grid = make_grid(h)
    elements.append(yn)
    for tn in grid[:n - 1]:
        kn1 = f(tn, yn)
        kn2 = f(tn + h / 2, yn + kn1 * h / 2)
        kn3 = f(tn + h / 2, yn + kn2 * h / 2)
        kn4 = f(tn + h, yn + kn3 * h)
        kn = (1 / 6) * (kn1 + 2 * kn2 + 2 * kn3 + kn4)
        yn_new = yn + h * kn
        elements.append(yn_new)
        yn = yn_new
    return elements


def f(t, y):
    return 2 * t * y


def f_solve(t):
    return np.exp( t * t)


def explicit_adams_3(h):
    numerical = []
    grid = make_grid(h)
    yn_2, yn_1, yn = compute_first_elements(h, 3)
    print(yn_2, yn_1, yn)
    numerical.extend([yn_2, yn_1, yn])  # append multiple elements
    for tn in grid[2:]:
        yn_new = yn + (h / 12) * (23 * f(tn, yn) - 16 * f(tn - h, yn_1) + 5 * f(tn - 2 * h, yn_2))
        numerical.append(yn_new)
        yn_2, yn_1, yn = yn_1, yn, yn_new
    return make_results(grid, analytical(h), numerical)

def explicit_adams_4(h):
    numerical = []
    grid = make_grid(h)
    yn_3, yn_2, yn_1, yn = compute_first_elements(h, 4)
    numerical.extend([yn_3, yn_2, yn_1, yn])
    for tn in grid[3:]:
        yn_new = yn + (h/24)*(55*f(tn, yn)-59*f(tn-h, yn_1)+37*f(tn-2*h, yn_2)-9*f(tn-3*h, yn_3))
        numerical.append(yn_new)
        yn_3, yn_2, yn_1, yn = yn_2, yn_1, yn, yn_new
    return make_results(grid, analytical(h), numerical)


def implicit_adams_3(h, eps):
    numerical = []
    grid = make_grid(h)
    yn_2, yn_1, yn = compute_first_elements(h, 3)
    numerical.extend([yn_2, yn_1, yn])
    for tn in grid[2:]:
        yk = yn + (h/12)*(23*f(tn, yn)-16*f(tn-h, yn_1)+5*f(tn-2*h, yn_2)) # explicit adams
        while True:
            yk_1 = yn + (h/12)*(5*f(tn+h, yk)+8*f(tn, yn)-f(tn-h, yn_1))
            if abs(yk_1-yk) < eps:
                break
            yk = yk_1
        yn_new = yn + (h/12)*(5*f(tn+h, yk_1)+8*f(tn, yn)-f(tn-h, yn_1))
        numerical.append(yn_new)
        yn_1, yn = yn, yn_new
    return make_results(grid, analytical(h), numerical)



print(implicit_adams_3(0.1, 1e-14))

