def longest2(a1, a2):
    distinct = set(a1 + a2)
    distinct_sorted = sorted(distinct)
    return "".join(distinct_sorted)


a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"

print(longest2(a1, a2))


def array_diff(a, b):
    # your code here
    for i in len(a):

        for j in b:
            if j in a:
                a.remove(i)
                b.remove(j)
    return a + b


a = [-2, 16, 19, -18, 6, 14, 8, -1, 13, -15, 5, 5, 10, 14, 1, 0, -19, -16]
b = [20, 15, -4, 11, -16, -19, -7]
print(array_diff(a, b))


duplicate_count("indivisibility")
