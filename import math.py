import math

#Проверка числа на простоту
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    #Проверяем до корня тк если есть делитель больше корня то есть и меньше
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

#Алгоритм «Решето Эратосфена»
def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return [i for i in range(2, n + 1) if prime[i]]

x = int(input("Введите число для проверки на простоту: "))
if is_prime(x):
    print(f"{x} — простое число")
else:
    print(f"{x} — не простое число")
n = int(input("Введите n для решета Эратосфена: "))
print("Простые числа до", n, ":", sieve_of_eratosthenes(n))

#  Разложение числа на простые множители (факторизация)
def factorize(n):
    factors = []

    d = 2
    # Если число можно разложить на множители
    # то один из них обязательно будет не больше корня
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n = n // d
        d += 1

    if n > 1:
        factors.append(n)

    return factors

num = int(input("Введите число: "))
print("Простые множители:", factorize(num))

# Алгоритм Евклида
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Расширенный алгоритм Евклида (линейное представление ax+by= НОД (a,b))
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return g, x, y

# НОК через НОД НОК(a, b) = (a * b) / НОД(a, b)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("НОД =", gcd(a, b))

g, x, y = extended_gcd(a, b)
print("Расширенный алгоритм Евклида:")
print("НОД =", g)
print("x =", x)
print("y =", y)
print(f"{a} * {x} + {b} * {y} = {g}")

print("НОК =", lcm(a, b))

# Операции по модулю (mod n). Быстрое возведение в степень.

def fast_power(a, b, mod):
    result = 1
    a = a % mod

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod

        a = (a * a) % mod
        b = b // 2

    return result


print(fast_power(2, 10, 7))

#система уравнений
def extended_gcd(a: int, b: int):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


def solve_linear_congruence(a: int, b: int, m: int):
    """
    Решает сравнение: ax ≡ b (mod m)
    Возвращает решение x или None, если решений нет
    """

    # приводим числа по модулю
    a = a % m
    b = b % m

    # находим НОД и коэффициент из расширенного Евклида
    g, p, _ = extended_gcd(a, m)

    # проверяем существование решения
    if b % g != 0:
        return None

    # находим решение
    x = (p * (b // g)) % (m // g)

    return x


# ===== пример использования =====
a = int(input("Введите a: "))
b = int(input("Введите b: "))
m = int(input("Введите модуль m: "))

solution = solve_linear_congruence(a, b, m)

if solution is None:
    print("Решений нет")
else:
    print(f"Решение: x = {solution}")