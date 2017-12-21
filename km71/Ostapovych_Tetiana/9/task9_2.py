a = float(input('a='))
n = int(input('n='))


def power(a, n):
    if n == 0:
        answer = 1
    elif n > 0:
        x1 = a
        while n > 1:
            x1 *= a
            n -= 1
            answer = x1
    elif n < 0:
        x2 = 1 / a
        while n < -1:
            x2 *= 1/a
            n += 1
            answer = x2
    return answer
print(power(a, n))

