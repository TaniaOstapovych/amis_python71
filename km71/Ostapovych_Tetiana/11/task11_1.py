def check(n, x):
    try:
        n = int(n)
        x = float(x)
        if n >= 1 and x !=1:
            a = True
        else:
            a = False
    except:
            a = False
    return a


def calc(n, x):
    sum = 0
    if n == 0:
        return 0
    else:
        n = int(n)
        x = float(x)
        b = ((x + 2)**n) / (x-1)
        return b +calc(n-1, x)

def run():
    n = input('Введіть значення n\n')
    x = input('Введіть значення x\n')
    print(check(n, x))

    if check(n, x) == True:
        print(calc(n, x))
    else:
        print("False")
print(run())