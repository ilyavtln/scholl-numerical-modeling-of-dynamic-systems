import numpy as np
from math import *
import matplotlib.pyplot as plt

#  Интервал интегрирования
a = 0
b = 20

#  Параметры системы
p_atm = 1e5
q_0 = 0.001
l = 1
d = 0.01
ro = 1000
C_snd = 1260
psi = 1 - cos(pi / 4)
S = (pi * d ** 2) / 4
C = (l * S) / (ro * (C_snd ** 2))


#  Функция q**n(t)
def q_n(t):
    if t <= 1:
        return q_0 * t
    else:
        return q_0


# начальные условия
p1_0 = p_atm
q2_0 = 0

#  размеры шагов
h1 = 1e-4
h2 = 1e-5

#  Генерация массивов для сеток
grid_h1 = np.arange(a, b + h1, h1)
grid_h2 = np.arange(a, b + h2, h2)


def f_p(t, q):
    return (q_n(t) - q) / C


def f_q(p, q):
    sq1 = sqrt((psi * abs(p - p_atm)) / (2 * ro))
    sq2 = sqrt((2 * abs(p - p_atm)) / (ro * psi))
    return sq1 * (S * sq2 * np.sign(p - p_atm) - q)


def direct(grid, h):
    p = [p1_0]
    q = [q2_0]
    i = 0
    for t in grid:
        k1_p = f_p(t, q[i])
        k1_q = f_q(p[i], q[i])

        k2_p = f_p(t + h / 2, q[i] + (h / 2) * k1_q)
        k2_q = f_q(p[i] + (h / 2) * k1_p, q[i] + (h / 2) * k1_q)

        k3_p = f_p(t + h / 2, q[i] + (h / 2) * k2_q)
        k3_q = f_q(p[i] + h / 2 * k2_p, q[i] + (h / 2) * k2_q)

        k4_p = f_p(t + h, q[i] + h * k3_q)
        k4_q = f_q(p[i] + h * k3_p, q[i] + h * k3_q)

        p.append(p[i] + (h / 6) * (k1_p + 2 * k2_p + 2 * k3_p + k4_p))
        q.append(q[i] + (h / 6) * (k1_q + 2 * k2_q + 2 * k3_q + k4_q))

        i += 1
    return p, q


def sequential(grid, h):
    p = [p1_0]
    q = [q2_0]
    i = 0
    for t in grid:
        k1_p = f_p(t, q[i])
        k2_p = f_p(t + h / 2, q[i] + (h / 2) * q[i])
        k3_p = f_p(t + h / 2, q[i] + (h / 2) * q[i])
        k4_p = f_p(t + h, q[i] + h * q[i])

        p.append(p[i] + (h / 6) * (k1_p + 2 * k2_p + 2 * k3_p + k4_p))

        k1_q = f_q(p[i + 1], q[i])
        k2_q = f_q(p[i + 1], q[i] + (h / 2) * k1_q)
        k3_q = f_q(p[i + 1], q[i] + (h / 2) * k2_q)
        k4_q = f_q(p[i + 1], q[i] + h * k3_q)

        q.append(q[i] + (h / 6) * (k1_q + 2 * k2_q + 2 * k3_q + k4_q))

        i += 1
    return p, q


def print_t10(grid, n, p, q):
    print(round(grid[n // 2], 15), round(p[n // 2], 15), round(q[n // 2], 15))


def show_plot(h, p, q, text):
    plt.plot(p)
    plt.title(f"{text} интегрирование с разбиением {h} \n p1(t)")
    plt.show()
    plt.plot(q)
    plt.title(f"{text} интегрирование с разбиением {h} \n q2(t)")
    plt.show()


p_res, q_res = direct(grid_h1, h1)
print_t10(grid_h1, len(grid_h1), p_res, q_res)
show_plot(h1, p_res, q_res, "Прямое")

# p_res, q_res = sequential(grid_h2, h2)
# print_t10(grid_h2, len(grid_h2), p_res, q_res)
# show_plot(h2, p_res, q_res, "Последовательное")
