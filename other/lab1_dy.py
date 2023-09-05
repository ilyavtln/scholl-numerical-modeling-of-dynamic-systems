import numpy as np
from math import *

h1, h2, h3 = 0.1, 0.05, 0.025  # размеры шагов


def f(t, y):  # исходная функция
    return 2 * t * y


def analytic(t):  # аналитическое значение
    return exp(t ** 2)


a = 0
b = 1
y0 = 1.0  # начальное условие

# Генерация массивов для сеток
grid_h1 = np.arange(a, b + h1, h1)
grid_h2 = np.arange(a, b + h2, h2)
grid_h3 = np.arange(a, b + h3, h3)


def method_1(y, h, t):
    return y + h * f(t, y)


def method_2(y, h, t):
    return y + (h / 2) * (f(t, y) + f(t + h, y + h * f(t, y)))


def method_3(y, h, t):
    return y + h * f(t + (h / 2), y + (h / 2) * f(t, y))


def find_values(y, grid, h):
    print("Сетка с разбиением", h)
    k = 0
    for t in grid:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        print(k, round(t, 7), round(y, 14), y_analytic, '%.2E' % error)
        y = method_1(y, h, t)  # Номер метода


find_values(y0, grid_h1, h1)   # Вывод таблицы
