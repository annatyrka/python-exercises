print("Enter integer")
number = int(input())
prime_factors = []
divisor = 2
while divisor <= number:
    while number % divisor == 0:
        number = number // divisor
        prime_factors.append(divisor)
    else:
        divisor += 1

print(prime_factors)
