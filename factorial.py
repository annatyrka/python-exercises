def decomp(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i

    factorials = {}
    print(factorial)

    for i in range(2, factorial+1):
        if factorial < 2:
            break
        print(factorial)
        if factorial % i == 0:
            factorials.setdefault(i, 0)
        while factorial % i == 0:
            factorials[i] += 1
            factorial = factorial // i
    result = ""
    for key in factorials.keys():
        if factorials[key] != 1:
            result += f"{key}^{factorials[key]} * "
        else:
            result += f"{key} * "

    return result[:-3]


print(decomp(12))
