from math import *
import numpy as np

h1, h2, h3 = 0.2, 0.1, 0.05  # размеры шагов


def f(t, y):  # исходная функция
    return -25 * y + cos(t) + 25 * sin(t)


def analytic(t):  # аналитическое значение
    return exp(-25 * t) * (1 + exp(25 * t) * sin(t))


eps = 1
a = 0
b = 2
y0 = 1.0  # начальное условие

# Генерация массивов для сеток
grid_h1 = np.arange(a, b + h1, h1)
grid_h2 = np.arange(a, b + h2, h2)
grid_h3 = np.arange(a, b + h3, h3)

y = 1
t = 0.5


def method_1(y, grid, h):
    print("Сетка методом Эйлера с разбиением", h)
    for t in grid:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        x = y + h * f(t, y)
        x1 = y + h * f(t + h, x)
        while abs(x - x1) > eps:
            x = x1
            x1 = y + h * f(t + h, x)
        y = x


def method_2(y, grid, h):
    print("Сетка методом трапеции с разбиением", h)
    for t in grid:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        x = y + h / 2.0 * (f(t, y) + f(t, y))
        x1 = y + h / 2.0 * (f(t, y) + f(t + h, x))
        while abs(x - x1) > eps:
            x = x1
            x1 = y + h / 2.0 * (f(t, y) + f(t + h, x))
        y = x


# Вывод таблицы
method_1(y0, grid_h1, h1)
method_2(y0, grid_h1, h1)
