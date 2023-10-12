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
    t = grid[2]
    f_y_n, f_y_n1, f_y_n2 = f(t, y_n), f(t - h, y_n1), f(t - 2 * h, y_n2)  # сохраняем f для начала
    print(f_y_n2, f_y_n1, f_y_n)

    for t in grid[2:-1]:
        y_next = y_n + (h / 12) * (23 * f_y_n - 16 * f_y_n1 + 5 * f_y_n2)
        y_analytic = round(analytic(t + h), 14)
        error = abs(y_next - y_analytic)
        #print(round(t + h, 14), round(y_next, 14), y_analytic, '%.2E' % error)
        y_n2, y_n1, y_n = y_n1, y_n, y_next  # сдвиг значений
        f_y_n, f_y_n1, f_y_n2 = f(t, y_n), f(t - h, y_n1), f(t - 2 * h, y_n2)  # сдвиг значений f
        #print(f_y_n, f_y_n1, f_y_n2, "test")