def square_root(a, xn, epsilon=1e-10):
    x_next = 0.5 * (xn + a / xn)

    if abs(x_next - xn) < epsilon:
        return x_next
    else:
        return square_root(a, x_next, epsilon)

def calculate_square_root(a):
    x0 = (1 + a) / 2
    return square_root(a, x0)
a = float(input("Введите число a для вычисления корня: "))
result = calculate_square_root(a)
print(f"Корень числа {a} равен: {result}")