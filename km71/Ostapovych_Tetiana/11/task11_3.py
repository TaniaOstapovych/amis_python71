def numbers(list):
    if len(list) < 2:
        return list
    else:
        x = len(list) // 2
        return numbers(list[x:]) + numbers(list[:x])

print(numbers(input('Введіть елементи списку').split()))