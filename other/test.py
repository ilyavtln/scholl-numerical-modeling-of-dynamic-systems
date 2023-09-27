A = [5, 3, 2, 1, 4, 6, 3, 7, 9, 1, 3, 2, 5, 6, 8, 2, 5, 2, 3, 6, 8, 3, 4, 4, 5, 6, 5, 4, 7, 5, 6, 4, 8, 7, 4, 5, 7, 8, 6, 5, 7, 5, 6, 6, 7, 3, 4, 6, 5, 4,]
# список без повторов
A.sort()
AB = list(set(A))
AB.sort()
su = 0
for i in AB:
    print(i, A.count(i))
    su += i*i * A.count(i)
su /= 50
print(su)
k = 0
dd = 0.0
for i in AB:
    dd += ((i - su)**2) * A.count(i)
    print(((i - su)**2) * A.count(i))
dd /= 50
print(dd)