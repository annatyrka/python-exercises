def find_middle(string):
    digits = []
    product_lst = []
    product = 1
    if type(string) == list:
        return -1
    for char in string:
        if (str(char)).isnumeric():
            digits.append(char)
    if digits == []:
        return -1
    for digit in digits:
        product *= int(digit)
    for i in str(product):
        product_lst.append(i)
    if len(product_lst) % 2 == 0:
        return int('{x}{y}'.format(x=int(product_lst[len(product_lst)//2-1]), y=int(product_lst[len(product_lst)//2])))
    else:
        return int(product_lst[((len(product_lst))-1)//2])


print(find_middle([1, 2, 3]))
print(type([1, ]))
