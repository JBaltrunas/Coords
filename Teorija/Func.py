a = [14, 2, 3, 4, 5]
b = [1, 25, 3, 4, 5, 7, 8]
c = [10, 2, 3, 4, 5, 9]


def sum_2_nums(a, b):

    return a + b


def sum(arr):
    s = 0
    for i in range(len(arr)):
        s += arr[i]
    return s


def find_max(arr):
    m = arr[0]
    for i in range(len(arr)):
        if arr[i] > m:
            m = arr[i]
    return m


print(sum_2_nums(4, 5))
print(sum_2_nums(45, 55))
print(sum_2_nums(b[4], a[1]))
