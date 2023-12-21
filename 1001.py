def ln(x):

    if x <= 0:
        raise ValueError("Натуральный логарифм определен только для положительных чисел")

    epsilon = 1e-10
    a, b = 0.5, x

    while b - a > epsilon:
        mid = 0.5 * (a + b)
        if mid * mid > x:
            b = mid
        else:
            a = mid

    return a

def exp(x):

    n = 20
    result = 1.0
    term = 1.0

    for i in range(1, n):
        term *= x / i
        result += term

    return result

def sin(x):
    n = 10
    result = 0.0
    sign = 1

    for i in range(1, n * 2, 2):
        result += sign * (x ** i) / factorial(i)
        sign *= -1

    return result

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_u(x, y):
    return x - y

def calculate_v(x, y):
    return x * x + sin(y)

def calculate_F(u, v):
    return exp(u * v) + v

def calculate_R(x, y):
    u = calculate_u(x, y)
    v = calculate_v(x, y)
    F = calculate_F(u, v)

    return ln(abs(F)) + (u * v) ** 0.5

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

result = calculate_R(x, y)
print(f"Результат вычислений R: {result}")