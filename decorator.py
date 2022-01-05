
def title_decorator(print_name_function):
    def wrapper(*arg, **kwargs):
        print('Professor:')
        print_name_function(*arg, **kwargs)
    return wrapper


@title_decorator
def print_my_name(name, age):
    print(name + " you are " + str(age))


print_my_name("Anna", 28)


# decorared_function = title_decorator(print_my_name) - this is what comes after @
# decorared_function()
