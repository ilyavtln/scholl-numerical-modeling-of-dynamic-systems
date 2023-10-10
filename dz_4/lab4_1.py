import numpy as np
from math import *

h1, h2, h3 = 0.1, 0.05, 0.025


def f(t, y):  # исходная функция
    return 2 * t * y


def analytic(t):  # аналитическое значение
    return exp(t ** 2)


a = 0
b = 1
y0 = 1.0  # начальное условие
eps = 1e-14

# Генерация массивов для сеток
grid_h1 = np.arange(a, b + h1, h1)
grid_h2 = np.arange(a, b + h2, h2)
grid_h3 = np.arange(a, b + h3, h3)


# Вычисление значений для первых элементов
def kn(t, y, h):
    k1 = f(t, y)
    k2 = f(t + h / 2, y + h / 2 * k1)
    k3 = f(t + h / 2, y + h / 2 * k2)
    k4 = f(t + h, y + h * k3)
    return 1.0 / 6 * (k1 + 2.0 * k2 + 2.0 * k3 + k4)


# Явный метод Адамса 3-го порядка
def explicit_adams_3(y, grid, h):
    print("Сетка методом Адамса 3-го порядка с разбиением", h)
    num = []
    for t in grid[:3]:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        y_new = y + h * kn(t, y, h)
        num.append(y)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        y = y_new
    for t in grid[3:]:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        print(y)
        y_new = y + (h / 12) * (23 * f(t, num[2]) - 16 * f(t - h, num[1]) + 5 * f(t - 2 * h, num[0]))
        for i in range(2):
            num[i] = num[i + 1]
        num[2] = y_new
        print(num)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        y = y_new


# Явный метод Адамса 4-го порядка
def explicit_adams_4(y, grid, h):
    print("Сетка методом Адамса 4-го порядка с разбиением", h)
    num = []
    for t in grid[:4]:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        y_new = y + h * kn(t, y, h)
        num.append(y)
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        y = y_new
    for t in grid[4:]:
        y_analytic = round(analytic(t), 14)
        error = abs(y - y_analytic)
        y_new = y + (h / 24) * (
                    55 * f(t, num[3]) - 59 * f(t - h, num[2]) + 37 * f(t - 2 * h, num[1]) - 9 * f(t - 3 * h, num[0]))
        for i in range(3):
            num[i] = num[i + 1]
        num[3] = y_new
        print(round(t, 14), round(y, 14), y_analytic, '%.2E' % error)
        y = y_new


# Неявный метод Адамса 3-го порядка

# Неявный метод Адамса 4-го порядка
# Вывод таблицы
explicit_adams_3(y0, grid_h2, h2)
# explicit_adams_4(y0, grid_h3, h3)
