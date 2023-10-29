import numpy as np

# Размер матрицы
n = 10

# Вектор x
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Генерация случайной матрицы
A = np.random.choice([0, np.random.randint(1, 5)], size=(n, n), p=[0.8, 0.2])

# Умножение на транспонированную
A = np.dot(A, A.T)

# Добавление n для положительной определенности
np.fill_diagonal(A, A.diagonal() + n)

# Ax = b
b = np.dot(A, x)

# Вывод матрицы A и вектора b
print("Матрица A:")
print(A)
print()
print("Вектор b: ")
print(*b, sep=" ")
print()

# Массив di
di = []

# Массив элементов
gg = []

# Массив индексов столбцов
jg = []

# Массив количества элементов
ig = [0, 0]

# Массив элементов в строках
elem = []

for i in range(0, n):
    row = []
    for j in range(0, n):
        if i == j:
            di.append(A[i][j])
        elif i > j and A[i][j] != 0:
            gg.append(A[i][j])
            jg.append(j)
            row.append(A[i][j])
        else:
            continue
    elem.append(row)

print("Массив di: ")
print(*di, sep=" ")
print()
print("Массив gg: ")
print(*gg, sep=" ")
print()
print("Массив jg: ")
print(*jg, sep=" ")
for i in range(1, n):
    ig.append(len(elem[i]) + ig[i])
print()
print("Массив ig: ")
print(*ig, sep=" ")
