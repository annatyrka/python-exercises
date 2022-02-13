spam = ["apples", "bananas", "tofu", "cats"]


def conv(x):
    for item in range(len(x)-1):
        print(x[item], end=", ")
    print("and " + x[-1])


(conv(spam))
