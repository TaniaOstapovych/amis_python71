print ('Эта программа решает сколько столов надо закупить для каждого класса.')
x1 = int(input('Введите количество учеников в первом классе: '))
x2 = int(input('Введите количество учеников во втором классе: '))
x3 = int(input('Введите количество учеников в третьем классе: '))
print ('Нужно закупить ', x1 // 2 + x1 % 2 + x2 // 2 + x2 % 2 + x3 // 2 + x3 % 2 , ' столов.')
