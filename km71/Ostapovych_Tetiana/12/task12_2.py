def elements(list, a):
    if len(list) == 1:
        a = list[0]
    else:
        a = max(int(elements(list[:-1])), int(list[-1]))
    return a


def count(list):
    max(list)
    return list.count(str())

print(count(input('Введіть елементи списку\n').split()))