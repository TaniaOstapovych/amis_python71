def elements(list, a):
    if len(list) == 1:
        a = list[0]
    else:
        a = max(int(elements(list[:-1], a)), int(list[-1]))
    return a


def max_elements(list, a):
    max(list)
    list.remove(str(a))
    max(list)
    return (str(a))


print(max_elements(input('Введіть елементи списку').split()))