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
eps = 1e-14  # точность

# Генерация массивов для сеток
grid_h1 = np.arange(a, b + h1, h1)
grid_h2 = np.arange(a, b + h2, h2)
grid_h3 = np.arange(a, b + h3, h3)


# Нахождение отсутствующих значений с помощью Рунге - Кутта
def kn(y, t, h):
    k1 = f(t, y)
    k2 = f(t + h / 2, y + (h / 2) * k1)
    k3 = f(t + h / 2, y + (h / 2) * k2)
    k4 = f(t + h, y + h * k3)
    return (1 / 6) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)


def find_explicit_3(y_n, y_n1, y_n2, h, t):
    return y_n + (h / 12) * (23 * f(t, y_n) - 16 * f(t - h, y_n1) + 5 * f(t - 2 * h, y_n2))


def find_explicit_4(y_n, y_n1, y_n2, y_n3, h, t):
    return y_n + (h / 24) * (55 * f(t, y_n) - 59 * f(t - h, y_n1) + 37 * f(t - 2 * h, y_n2) - 9 * f(t - 3 * h, y_n3))


def explicit_3(y, grid, h):
    print("Явный метод Адамса 3-го порядка с разбиением", h)
    y_find = [y]  # добавляем первый элемент в массив
    y_analytic = round(analytic(0.0), 14)
    error = abs(y - y_analytic)
    print(round(0.0, 14), round(y, 14), y_analytic, '%.2E' % error)
    for t in grid[:2]:
        y_next = y + h * kn(y, t, h)  # находим новый y
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_next - y_analytic)
        print(round(t + h, 14), round(y_next, 14), y_analytic, '%.2E' % error)
        y_find.append(y_next)  # добавляем первые найденные элементы в массив
        y = y_next

    y_n2, y_n1, y_n = y_find[0], y_find[1], y_find[2]  # сохраняем в переменные найденные значения

    for t in grid[2:-1]:
        f_y_n = f(t, y_n)
        f_y_n1 = f(t - h, y_n1)
        f_y_n2 = f(t - 2 * h, y_n2)
        print(f_y_n, f_y_n1, f_y_n2, "t")
        y_next = y_n + (h / 12) * (23 * f_y_n - 16 * f_y_n1 + 5 * f_y_n2)
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_next - y_analytic)
        # print(round(t + h, 14), round(y_next, 14), y_analytic, '%.2E' % error)
        y_n2, y_n1, y_n = y_n1, y_n, y_next  # сдвиг значений


def explicit_4(y, grid, h):
    print("Явный метод Адамса 4-го порядка с разбиением", h)
    y_find = [y]  # добавляем первый элемент в массив
    y_analytic = round(analytic(0.0), 14)
    error = abs(y - y_analytic)
    print(round(0.0, 14), round(y, 14), y_analytic, '%.2E' % error)
    for t in grid[:3]:
        y_next = y + h * kn(y, t, h)  # находим новый y
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_next - y_analytic)
        print(round(t + h, 14), round(y_next, 14), y_analytic, '%.2E' % error)
        y_find.append(y_next)  # добавляем первые найденные элементы в массив
        y = y_next

    y_n3, y_n2, y_n1, y_n = y_find[0], y_find[1], y_find[2], y_find[3]  # сохраняем в переменные найденные значения

    for t in grid[3:-1]:
        y_next = find_explicit_4(y_n, y_n1, y_n2, y_n3, h, t)
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_next - y_analytic)
        print(round(t + h, 14), round(y_next, 14), y_analytic, '%.2E' % error)
        y_n3, y_n2, y_n1, y_n = y_n2, y_n1, y_n, y_next  # сдвиг значений


def implicit_3(y, grid, h):
    print("Неявный метод Адамса 3-го порядка с разбиением", h)
    y_find = [y]  # добавляем первый элемент в массив
    y_analytic = round(analytic(0.0), 14)
    error = abs(y - y_analytic)
    print(round(0.0, 14), round(y, 14), y_analytic, '%.2E' % error)
    for t in grid[:2]:
        y_next = y + h * kn(y, t, h)  # находим новый y
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_next - y_analytic)
        print(round(t + h, 14), round(y_next, 14), y_analytic, '%.2E' % error)
        y_find.append(y_next)  # добавляем первые найденные элементы в массив
        y = y_next

    y_n2, y_n1, y_n = y_find[0], y_find[1], y_find[2]  # сохраняем в переменные найденные значения

    for t in grid[2:-1]:
        x = find_explicit_3(y_n, y_n1, y_n2, h, t)
        x1 = y_n + (h / 12) * (5 * f(t + h, x) + 8 * f(t, y_n) - (f(t - h, y_n1)))
        while abs(x1 - x) > eps:
            x = x1
            x1 = y_n + (h / 12) * (5 * f(t + h, x) + 8 * f(t, y_n) - (f(t - h, y_n1)))
        y_n2, y_n1, y_n = y_n1, y_n, x1
        y_analytic = round(analytic(t + h), 14)
        error = abs(x1 - y_analytic)
        print(round(t + h, 14), round(x1, 14), y_analytic, '%.2E' % error)


def implicit_4(y, grid, h):
    print("Неявный метод Адамса 4-го порядка с разбиением", h)
    y_find = [y]  # добавляем первый элемент в массив
    y_analytic = round(analytic(0.0), 14)
    error = abs(y - y_analytic)
    print(round(0.0, 14), round(y, 14), y_analytic, '%.2E' % error)
    for t in grid[:3]:
        y_next = y + h * kn(y, t, h)  # находим новый y
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_next - y_analytic)
        print(round(t + h, 14), round(y_next, 14), y_analytic, '%.2E' % error)
        y_find.append(y_next)  # добавляем первые найденные элементы в массив
        y = y_next

    y_n3, y_n2, y_n1, y_n = y_find[0], y_find[1], y_find[2], y_find[3]  # сохраняем в переменные найденные значения

    for t in grid[3:-1]:
        x = find_explicit_4(y_n, y_n1, y_n2, y_n3, h, t)
        x1 = y_n + (h / 24) * (9 * f(t + h, x) + 19 * f(t, y_n) - 5 * (f(t - h, y_n1)) + f(t - h * 2, y_n2))
        while abs(x1 - x) > eps:
            x = x1
            x1 = y_n + (h / 24) * (9 * f(t + h, x) + 19 * f(t, y_n) - 5 * (f(t - h, y_n1)) + f(t - h * 2, y_n2))
        y_n3, y_n2, y_n1, y_n = y_n2, y_n1, y_n, x1
        y_analytic = round(analytic(t + h), 14)
        error = abs(x1 - y_analytic)
        print(round(t + h, 14), round(x1, 14), y_analytic, '%.2E' % error)


def prediction_correction_3(y, grid, h):
    print("Метод прогноза - коррекции 3-го порядка с разбиением", h)
    y_find = [y]  # добавляем первый элемент в массив
    y_analytic = round(analytic(0.0), 14)
    error = abs(y - y_analytic)
    print(round(0.0, 14), round(y, 14), y_analytic, '%.2E' % error)
    for t in grid[:2]:
        y_next = y + h * kn(y, t, h)  # находим новый y
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_next - y_analytic)
        print(round(t + h, 14), round(y_next, 14), y_analytic, '%.2E' % error)
        y_find.append(y_next)  # добавляем первые найденные элементы в массив
        y = y_next

    y_n2, y_n1, y_n = y_find[0], y_find[1], y_find[2]  # сохраняем в переменные найденные значения

    for t in grid[2:-1]:
        y_pred = find_explicit_3(y_n, y_n1, y_n2, h, t)
        y_corr = y_n + (h / 12) * (5 * f(t + h, y_pred) + 8 * f(t, y_n) - (f(t - h, y_n1)))
        y_n2, y_n1, y_n = y_n1, y_n, y_corr
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_corr - y_analytic)
        print(round(t + h, 14), round(y_corr, 14), y_analytic, '%.2E' % error)


def prediction_correction_4(y, grid, h):
    print("Метод прогноза - коррекции 4-го порядка с разбиением", h)
    y_find = [y]  # добавляем первый элемент в массив
    y_analytic = round(analytic(0.0), 14)
    error = abs(y - y_analytic)
    print(round(0.0, 14), round(y, 14), y_analytic, '%.2E' % error)
    for t in grid[:3]:
        y_next = y + h * kn(y, t, h)  # находим новый y
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_next - y_analytic)
        print(round(t + h, 14), round(y_next, 14), y_analytic, '%.2E' % error)
        y_find.append(y_next)  # добавляем первые найденные элементы в массив
        y = y_next

    y_n3, y_n2, y_n1, y_n = y_find[0], y_find[1], y_find[2], y_find[3]  # сохраняем в переменные найденные значения

    for t in grid[3:-1]:
        y_pred = find_explicit_4(y_n, y_n1, y_n2, y_n3, h, t)
        y_corr = y_n + (h / 24) * (9 * f(t + h, y_pred) + 19 * f(t, y_n) - 5 * (f(t - h, y_n1)) + f(t - h * 2, y_n2))
        y_n3, y_n2, y_n1, y_n = y_n2, y_n1, y_n, y_corr
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_corr - y_analytic)
        print(round(t + h, 14), round(y_corr, 14), y_analytic, '%.2E' % error)

explicit_3(y0, grid_h1, h1)
# explicit_4(y0, grid_h1, h1)
# implicit_3(y0, grid_h1, h1)
# implicit_4(y0, grid_h1, h1)
# prediction_correction_3(y0, grid_h1, h1)
# prediction_correction_4(y0, grid_h1, h1)
