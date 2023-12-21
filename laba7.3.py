def sum_of_divisors(num):
    div_sum = 0
    for i in range(1, num):
        if num % i == 0:
            div_sum += i
    return div_sum

def are_friendly_numbers(num1, num2):
    return sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1

def find_friendly_pairs(limit):
    friendly_pairs = []
    for i in range(2, limit + 1):
        for j in range(i + 1, limit + 1):
            if are_friendly_numbers(i, j):
                friendly_pairs.append((i, j))
    return friendly_pairs

limit = int(input("Введите натуральное число: "))
result = find_friendly_pairs(limit)

if result:
    print("Дружественные числа:")
    for pair in result:
        print(pair)
else:
    print("Дружественные числа не найдены.")