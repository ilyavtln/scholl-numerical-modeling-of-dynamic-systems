def find_uniq(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] != arr[j]:
                n = arr[i]
            else:
                break
    return n   # n: unique number in the array