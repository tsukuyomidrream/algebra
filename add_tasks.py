new_cells = r"""

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 1. Деление полиномов над целостным кольцом

    **Полином** над целыми числами представляем как список коэффициентов от старшего к младшему:
    $$f(x) = a_n x^n + \dots + a_1 x + a_0 \quad \leftrightarrow \quad [a_n, \dots, a_1, a_0]$$

    **Деление с остатком:** для любых полиномов $f$ и $g$ существуют $q$ и $r$ такие что:
    $$f(x) = g(x) \cdot q(x) + r(x), \quad \deg(r) < \deg(g)$$

    **Алгоритм (столбик):**
    1. Делим старший член делимого на старший член делителя — получаем очередной коэффициент частного
    2. Вычитаем произведение из делимого
    3. Повторяем пока $\deg(\text{остаток}) < \deg(\text{делитель})$

    | Задача | Время | Память |
    | :--- | :--- | :--- |
    | Деление полиномов степеней $n$ и $m$ | $O(n \cdot m)$ | $O(n)$ |
    """)
    return


@app.function
def poly_div(dividend, divisor):
    a = list(dividend)
    b = list(divisor)
    while len(a) > 1 and a[0] == 0: a.pop(0)   # убираем ведущие нули
    while len(b) > 1 and b[0] == 0: b.pop(0)

    if b == [0]:
        raise ValueError("Деление на нулевой полином")
    if len(a) < len(b):
        return [0], a   # степень делимого меньше — частное 0, остаток = делимое

    quotient = [0] * (len(a) - len(b) + 1)
    remainder = a[:]

    for i in range(len(quotient)):
        coeff = remainder[i] // b[0]   # коэффициент очередного члена частного
        quotient[i] = coeff
        for j in range(len(b)):        # вычитаем coeff * делитель
            remainder[i + j] -= coeff * b[j]

    remainder = remainder[len(quotient):]   # хвост — это остаток
    while len(remainder) > 1 and remainder[0] == 0:
        remainder.pop(0)

    return quotient, remainder


@app.cell
def _():
    q, r = poly_div([3, 2, 1, 5], [1, 1, 1])
    print(f"(3x^3 + 2x^2 + x + 5) / (x^2 + x + 1)")
    print(f"Частное:  {q}")
    print(f"Остаток:  {r}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 2. Вычисления в простых конечных полях GF(p) через битовые операции

    $GF(p)$ — поле остатков по модулю простого $p$. Элементы: $0, 1, \dots, p-1$.

    ## Умножение через биты — «Русский крестьянин»

    Разбиваем $b$ по битам. Если бит = 1 — добавляем $a$ к результату, затем удваиваем $a$ и сдвигаем $b$ вправо:
    $$a \cdot b = \sum_{i:\ \text{бит}\ i\ \text{числа}\ b = 1} a \cdot 2^i$$

    Вместо `b % 2` — `b & 1`, вместо `b // 2` — `b >> 1`, вместо `a * 2` — `a << 1`.

    ## Возведение в степень через биты

    Аналогично умножению, но на каждом шаге возводим в квадрат вместо удвоения.

    | Операция | Время | Память |
    | :--- | :--- | :--- |
    | Умножение $a \cdot b$ | $O(\log b)$ | $O(1)$ |
    | Возведение $a^b$ | $O(\log b)$ | $O(1)$ |
    """)
    return


@app.function
def gfp_mul(a, b, p):
    result = 0
    a = a % p
    while b > 0:
        if b & 1:                  # если младший бит b равен 1
            result = (result + a) % p
        a = (a << 1) % p           # a * 2 mod p через сдвиг влево
        b >>= 1                    # сдвигаем b вправо
    return result


@app.function
def gfp_pow(a, b, p):
    result = 1
    a = a % p
    while b > 0:
        if b & 1:                  # если младший бит степени равен 1
            result = gfp_mul(result, a, p)
        a = gfp_mul(a, a, p)       # возводим основание в квадрат
        b >>= 1                    # сдвигаем степень вправо
    return result


@app.cell
def _():
    p = 7
    print(f"3 * 5 mod {p} = {gfp_mul(3, 5, p)}")
    print(f"3 ^ 10 mod {p} = {gfp_pow(3, 10, p)}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 3. Построение поля GF(256)

    $GF(256) = GF(2^8)$ — поле из 256 элементов, используется в **AES-шифровании**.

    Элементы — полиномы степени $< 8$ над $GF(2)$, представленные как **байт** (8 бит):
    $$a_7 x^7 + \dots + a_1 x + a_0 \quad \leftrightarrow \quad \underbrace{a_7 a_6 \dots a_0}_{8 \text{ бит}}$$

    **Сложение** = XOR, т.к. в $GF(2)$: $1 + 1 = 0$

    **Умножение** = умножение полиномов по модулю неприводимого полинома степени 8.

    Стандартный для AES: $x^8 + x^4 + x^3 + x + 1$ = `0x11b`

    Если при умножении результат выходит за 8 бит (9-й бит = 1) — делаем XOR с `0x11b`.

    | Операция | Время | Память |
    | :--- | :--- | :--- |
    | Сложение | $O(1)$ | $O(1)$ |
    | Умножение | $O(\log a)$ | $O(1)$ |
    """)
    return


@app.function
def gf256_add(a, b):
    return a ^ b                   # сложение = XOR в GF(2)


@app.function
def gf256_mul(a, b):
    IRREDUCIBLE = 0x11b            # x^8 + x^4 + x^3 + x + 1
    result = 0
    while b > 0:
        if b & 1:                  # если младший бит b = 1 — добавляем a
            result ^= a
        a <<= 1                    # умножаем a на x (сдвиг влево)
        if a & 0x100:              # вышли за 8 бит — берём по модулю
            a ^= IRREDUCIBLE
        b >>= 1
    return result


@app.function
def gf256_pow(a, b):
    result = 1
    while b > 0:
        if b & 1:
            result = gf256_mul(result, a)
        a = gf256_mul(a, a)
        b >>= 1
    return result


@app.cell
def _():
    print(f"0x53 + 0xCA = {hex(gf256_add(0x53, 0xCA))}")
    print(f"0x53 * 0xCA = {hex(gf256_mul(0x53, 0xCA))}")
    print(f"0x02 ^ 8    = {hex(gf256_pow(0x02, 8))}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 4. Нахождение неприводимых полиномов в конечном поле

    **Неприводимый полином** — полином, который нельзя разложить в произведение полиномов меньшей степени. Аналог простого числа для полиномов.

    Над $GF(2)$ полином представляется как целое число (каждый бит — коэффициент):
    $$x^4 + x + 1 = \underbrace{10011}_{2} = 19$$

    **Проверка неприводимости** полинома $f$ степени $n$:
    1. $f(0) \neq 0$ — нет корня 0 (константный член = 1, число нечётное)
    2. $f(1) \neq 0$ — нет корня 1 (количество единичных битов нечётно)
    3. Не делится ни на один полином степени от $1$ до $\lfloor n/2 \rfloor$

    | Задача | Время | Память |
    | :--- | :--- | :--- |
    | Проверка степени $n$ | $O(2^{n/2} \cdot n)$ | $O(1)$ |
    """)
    return


@app.function
def gf2_degree(p):
    if p == 0:
        return -1
    deg = 0
    while p >> (deg + 1):
        deg += 1
    return deg


@app.function
def gf2_div(a, b):
    # деление полиномов над GF(2): вычитание = XOR
    remainder = a
    deg_b = gf2_degree(b)
    quotient = 0
    while gf2_degree(remainder) >= deg_b:
        shift = gf2_degree(remainder) - deg_b
        quotient ^= (1 << shift)
        remainder ^= (b << shift)
    return quotient, remainder


@app.function
def gf2_is_irreducible(p):
    n = gf2_degree(p)
    if n < 1:
        return False
    if p & 1 == 0:                         # f(0) = 0 — есть корень 0
        return False
    if bin(p).count('1') % 2 == 0:         # f(1) = 0 — есть корень 1
        return False
    for d in range(1, n // 2 + 1):        # пробуем делители степени d
        for cand in range(1 << d, 1 << (d + 1)):
            if cand & 1 == 0:              # делитель должен иметь свободный член
                continue
            _, rem = gf2_div(p, cand)
            if rem == 0:                   # делится — не неприводимый
                return False
    return True


@app.function
def find_irreducible(degree):
    result = []
    for p in range(1 << degree, 1 << (degree + 1)):
        if gf2_is_irreducible(p):
            result.append(p)
    return result


@app.cell
def _():
    polys = find_irreducible(4)
    print("Неприводимые степени 4 над GF(2):")
    for p in polys:
        print(f"  {bin(p)} = {p}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 5. Решение квадратных уравнений в конечных полях GF(p)

    **Уравнение:** $ax^2 + bx + c \equiv 0 \pmod{p}$

    **Дискриминант:** $D = b^2 - 4ac \pmod{p}$

    **Три случая:**
    - $D = 0$: одно решение $\;x = -b \cdot (2a)^{-1} \bmod p$
    - $D$ — квадратичный вычет: два решения $\;x = (-b \pm \sqrt{D}) \cdot (2a)^{-1} \bmod p$
    - $D$ — не квадратичный вычет: решений нет

    **Критерий Эйлера** — $D$ является квадратичным вычетом тогда и только тогда, когда:
    $$D^{(p-1)/2} \equiv 1 \pmod{p}$$

    **Квадратный корень mod p:**
    - Если $p \equiv 3 \pmod 4$: $\sqrt{D} = D^{(p+1)/4} \bmod p$
    - Иначе: алгоритм Тонелли-Шенкса

    | Задача | Время | Память |
    | :--- | :--- | :--- |
    | Решение уравнения | $O(\log^2 p)$ | $O(1)$ |
    """)
    return


@app.function
def sqrt_mod(n, p):
    n = n % p
    if n == 0:
        return 0
    if gfp_pow(n, (p - 1) // 2, p) != 1:  # критерий Эйлера
        return None                        # квадратный корень не существует

    if p % 4 == 3:                         # простой случай: p ≡ 3 (mod 4)
        return gfp_pow(n, (p + 1) // 4, p)

    # Тонелли-Шенкс: p ≡ 1 (mod 4)
    q, s = p - 1, 0
    while q % 2 == 0:                      # p-1 = 2^s * q, q нечётное
        q //= 2
        s += 1
    z = 2                                  # ищем квадратичный невычет
    while gfp_pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m = s
    c = gfp_pow(z, q, p)
    t = gfp_pow(n, q, p)
    r = gfp_pow(n, (q + 1) // 2, p)
    while True:
        if t == 1:
            return r
        i, temp = 1, (t * t) % p
        while temp != 1:
            temp = (temp * temp) % p
            i += 1
        b = gfp_pow(c, 1 << (m - i - 1), p)
        m, c = i, (b * b) % p
        t, r = (t * c) % p, (r * b) % p


@app.function
def solve_quadratic_gfp(a, b, c, p):
    a, b, c = a % p, b % p, c % p
    if a == 0:                             # вырождается в линейное bx + c = 0
        if b == 0:
            return []
        return [((-c) * mod_inverse_euclid(b, p)) % p]

    D = (b * b - 4 * a * c) % p           # дискриминант
    inv_2a = mod_inverse_euclid((2 * a) % p, p)

    if D == 0:
        return [(-b * inv_2a) % p]        # одно решение

    sq = sqrt_mod(D, p)
    if sq is None:
        return []                          # решений нет

    x1 = ((-b + sq) * inv_2a) % p
    x2 = ((-b - sq) * inv_2a) % p
    return [x1] if x1 == x2 else [x1, x2]


@app.cell
def _():
    p = 7
    s1 = solve_quadratic_gfp(1, 2, 1, p)
    s2 = solve_quadratic_gfp(1, 0, 1, p)
    s3 = solve_quadratic_gfp(1, 1, 2, p)
    print(f"x^2 + 2x + 1 = 0 mod {p}: x = {s1}")
    print(f"x^2 + 1 = 0 mod {p}:      x = {s2}")
    print(f"x^2 + x + 2 = 0 mod {p}:  x = {s3}")
    return

"""

with open('notebook.py', 'r', encoding='utf-8') as f:
    content = f.read()

insert_pos = content.rfind('\nif __name__ == "__main__":')
new_content = content[:insert_pos] + new_cells + content[insert_pos:]

with open('notebook.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

import ast
ast.parse(new_content)
print("OK — синтаксис верный")
