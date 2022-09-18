list = [ 50, 40, 30, 45, 33]


def my_func(arg):
    return abs(arg -5)

# print([my_func(x) for x in list])
list.sort(key=my_func)
print(list)