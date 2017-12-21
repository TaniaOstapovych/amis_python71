def numbers(list):
    if len(list) == 1:
      return list[0]
    else:
     a = min(numbers(list[:-1]), list[-1])
     return a

print(numbers(input('Введіть елементи списку\n').split()))