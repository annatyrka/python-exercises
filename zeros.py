def zeros(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
    zero = 0
    lst = list(str(number))
    lst.reverse()
    for item in lst:
        if item == '0':
            zero += 1
        else:
            break
    return zero


print(zeros(7))
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
