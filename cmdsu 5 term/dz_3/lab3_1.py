import math

import numpy as np
from math import *

# размеры шагов для Рунге-Кутты
# h1, h2, h3, h4 = 0.5, 0.25, 0.125, 0.1

# размеры шагов для явного и неявного Эйлера
h1, h2, h3 = 0.1, 0.05, 0.025


# размеры шагов для модифицированного Эйлера и трапеции
# h1, h2, h3 = 0.2, 0.1, 0.05

def f(t, y):  # исходная функция
    return (-25) * y + math.cos(t) + 25 * math.sin(t)


def analytic(t):  # аналитическое значение
    return sin(t) + 1 / exp(25 * t)


a = 0
b = 2
y0 = 1.0  # начальное условие
eps = 1e-14

# Генерация массивов для сеток
grid_h1 = np.arange(a, b + h1, h1)
grid_h2 = np.arange(a, b + h2, h2)
grid_h3 = np.arange(a, b + h3, h3)


# grid_h4 = np.arange(a, b + h4, h4)

# Явный метод Эйлера
def explicit_method(y, grid, h):
    print("Сетка методом Эйлера с разбиением", h)
    for t in grid:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        y = y + h * f(t, y)


# Неявный метод Эйлера
def implicit_method(y, grid, h):
    print("Сетка неявным методом Эйлера с разбиением", h)
    for t in grid:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        x = y + h * f(t, y)
        x1 = x - (y + h * f(t + h, x) - x) / ((-25.0 * h) - 1.0)
        while abs(x - x1) > eps:
            x = x1
            x1 = x - (y + h * f(t + h, x) - x) / ((-25.0 * h) - 1.0)
        y = x


# Модифицированный метод Эйлера
def modified_method(y, grid, h):
    print("Сетка модифицированным методом Эйлера с разбиением", h)
    for t in grid:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        y = y + (h / 2) * (f(t, y) + f(t + h, y + h * f(t, y)))


# Метод Трапеции
def trapezoid(y, grid, h):
    print("Сетка методом трапеции с разбиением", h)
    for t in grid:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        x = y + h / 2.0 * (f(t, y) + f(t + h, y))
        x1 = x - (y + (h / 2) * (f(t, y) + f(t + h, x)) - x) / ((-25.0 * h) - 1.0)
        while abs(x - x1) > eps:
            x = x1
            x1 = x - (y + (h / 2) * (f(t, y) + f(t + h, x)) - x) / ((-25.0 * h) - 1.0)
        y = x


# Метод Рунге-Кутты
def runge_kutta(y, grid, h):
    print("Сетка методом Рунге-кутты с разбиением", h)
    for t in grid:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        k1 = f(t, y)
        k2 = f(t + h / 2, y + (h / 2) * k1)
        k3 = f(t + h / 2, y + (h / 2) * k2)
        k4 = f(t + h, y + h * k3)
        kn = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y = y + h * kn


# Вывод таблицы
# explicit_method(y0, grid_h1, h1)
# implicit_method(y0, grid_h1, h1)
# modified_method(y0, grid_h1, h1)
# trapezoid(y0, grid_h1, h1)
# runge_kutta(y0, grid_h1, h1)
