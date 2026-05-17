import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #1. Проверка числа на простоту
    """)
    return


@app.function
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    #Проверяем до корня тк если есть делитель больше корня то есть и меньше
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


@app.cell
def _():
    is_prime(9)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Алгоритм «Решето Эратосфена»
    """)
    return


@app.function
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


@app.cell
def _():
    sieve_of_eratosthenes(9)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 2. Разложение числа на простые множители (факторизация)
    """)
    return


@app.function
def factorize(n):
    factors = []

    d = 2
    # Если число можно разложить на множители, то один из них обязательно будет не больше корня
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n = n // d
        d += 1

    if n > 1:
        factors.append(n)

    return factors


@app.cell
def _():
    factorize(9)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 3. Алгоритм Евклида
    """)
    return


@app.function
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


@app.cell
def _():
    gcd(24, 18)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Расширенный алгоритм Евклида (линейное представление ax+by= НОД (a,b))
    """)
    return


@app.function
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


@app.cell
def _():
    extended_gcd(24, 18)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # НОК через НОД НОК(a, b) = (a * b) / НОД(a, b)
    """)
    return


@app.function
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


@app.cell
def _():
    lcm(24,18)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 4. Операции по модулю (mod n). Быстрое возведение в степень.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Быстрое возведение в степень:
    #### Если степень чётная

    $$
    a^b = (a^{b/2})^2
    $$

    ---

    #### Если степень нечётная

    $$
    a^b = a \cdot a^{b-1}
    $$
    """)
    return


@app.function
def fast_power(a, b, mod):
    result = 1
    a = a % mod

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod

        a = (a * a) % mod
        b = b // 2

    return result


@app.cell
def _():
    fast_power(3, 5, 7)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #5. Нахождение решения системы линейных сравнений.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    \[
    ax \equiv b \pmod m
    \]
    , то есть:

    \[
    ax - b = mk
    \]

    для некоторого целого \(k\).

    ### Откуда берётся формула для \(x\)

    Из расширенного алгоритма Евклида получаем:

    \[
    ap + mq = g
    \]  где

    \[
    g = \gcd(a, m)
    \]

    Если \(g\) делит \(b\), то можно умножить всё равенство на

    \[
    \frac{b}{g}
    \]

    Получаем:

    \[
    ap \cdot \frac{b}{g} + mq \cdot \frac{b}{g} = b
    \]

    Второе слагаемое кратно \(m\), значит по модулю \(m\) оно исчезает:

    \[
    a\left(p \cdot \frac{b}{g}\right) \equiv b \pmod m
    \]

    Сравнивая с исходным сравнением

    \[
    ax \equiv b \pmod m
    \]

    получаем формулу решения:

    \[
    x \equiv p \cdot \frac{b}{g} \pmod{\frac{m}{g}}
    \]
    """)
    return


@app.function
def solve_linear_congruence(a, b, m):
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


@app.cell
def _():
    solution = solve_linear_congruence(6, 3, 9)

    if solution is None:
        print("Решений нет")
    else:
        print("x =", solution)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 6. Вычисление значения функции Эйлера для заданного n.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Два целых числа $a$ и $b$ называются **взаимно простыми**, если их наибольший общий делитель равен единице. Это означает, что у чисел **нет общих простых делителей**. Их разложения на простые множители не пересекаются.

    **Каноническое разложение** числа $n > 1$ — это его единственное представление в виде произведения степеней различных простых чисел, записанных в порядке возрастания:
    $$n = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot \dots \cdot p_k^{\alpha_k}$$

    Если $p$ — простое число, то: $\varphi(p) = p - 1$

    # Лемма 1: Значение функции Эйлера для степени простого числа
    Если $p$ — простое число, а $k \ge 1$ — целое число, то:
    $$\varphi(p^k) = p^k - p^{k-1} = p^{k-1}(p - 1)$$

    # Лемма 2: Мультипликативность функции Эйлера
    Если целые числа $a$ и $b$ взаимно просты ($\gcd(a, b) = 1$), то:
    $$\varphi(a \cdot b) = \varphi(a) \cdot \varphi(b)$$

    # Формула функции Эйлера. Теорема.

    Пусть каноническое разложение натурального числа $n$ имеет вид:
    $$n = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot \dots \cdot p_k^{\alpha_k}$$
    Тогда значение функции Эйлера $\varphi(n)$ (количество натуральных чисел от $1$ до $n$, взаимно простых с $n$) вычисляется по формуле:
    $$\varphi(n) = n \cdot \prod_{i=1}^{k} \left(1 - \frac{1}{p_i}\right) = \prod_{i=1}^{k} p_i^{\alpha_i - 1}(p_i - 1)$$

    | Задача | Время | Память |
    | :--- | :--- | :--- |
    | $\varphi(n)$ | $O(\sqrt{n})$ | $O(1)$ |
    """)
    return


@app.function
def euler_totient(n):
    if n < 1:
        return 0
    if n == 1:
        return 1

    result = n
    p = 2
    # Перебор возможных простых делителей до sqrt(n)
    while p * p <= n:
        if n % p == 0:
            # p - простой делитель, применяем формулу
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    # Если после цикла n > 1, значит оставшийся n - тоже простой множитель
    if n > 1:
        result = result*( n-1) // n
    return result


@app.cell
def _():
    euler_totient(4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 7. Вычисление $a^b \bmod n$ при помощи теоремы Эйлера

    **Теорема Эйлера:** Если натуральные числа a и n взаимно простые, то:
    $$a^{\varphi(n)} \equiv 1 \pmod{n}$$

    ### Почему большую степень $b$ можно заменить на остаток $b \bmod \varphi(n)$?

    **Шаг 1** — запишем $b$ через деление с остатком:
    $$b = \varphi(n) \cdot q + r, \quad r = b \bmod \varphi(n)$$

    **Шаг 2** — подставим в степень:
    $$a^b = a^{\varphi(n) \cdot q\ +\ r}$$

    **Шаг 3** — разобьём по свойству степеней $\left(a^{x+y} = a^x \cdot a^y\right)$:
    $$= a^{\varphi(n) \cdot q} \cdot a^r$$

    **Шаг 4** — перепишем первый множитель $\left(a^{x \cdot y} = (a^x)^y\right)$:
    $$= \left(a^{\varphi(n)}\right)^q \cdot a^r$$

    **Шаг 5** — применяем теорему Эйлера: $a^{\varphi(n)} \equiv 1$, значит:
    $$= \underbrace{1^q}_{=\ 1} \cdot a^r \equiv a^r \pmod{n}$$

    **Вывод:** полные циклы длиной $\varphi(n)$ всегда дают $1$ и не влияют на результат. Имеет значение только хвост $r$.

    | Задача | Время | Память |
    | :--- | :--- | :--- |
    | $a^b \bmod n$ через т. Эйлера | $O(\sqrt{n} + \log b)$ | $O(1)$ |
    """)
    return


@app.function
def euler_theorem_power(a, b, n):
    if gcd(a, n) != 1:
        # Теорема Эйлера неприменима — считаем напрямую
        return fast_power(a, b, n)
    phi = euler_totient(n)   # φ(n) из задачи 6
    r = b % phi              # уменьшаем показатель степени
    return fast_power(a, r, n)


@app.cell
def _():
    euler_theorem_power(3, 100, 7)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # 8. Мультипликативное обратное по $\bmod n$

    Число $x$ называется **мультипликативным обратным элементом** к $a$ по модулю $n$, если $a \cdot x \equiv 1 \pmod{n}$

    Обозначается $a^{-1} \bmod n$. Существует **тогда и только тогда**, когда $\gcd(a, n) = 1$.


    ---

    ## Метод 1 — через теорему Эйлера

    Из теоремы Эйлера знаем: $a^{\varphi(n)} \equiv 1 \pmod{n}$

    Перепишем:
    $$a \cdot a^{\varphi(n)-1} \equiv 1 \pmod{n}$$

    Значит:
    $$a^{-1} \equiv a^{\varphi(n)-1} \pmod{n}$$

    Обратный элемент — это $a$ в степени $\varphi(n) - 1$.

    ---

    ## Метод 2 — через расширенный алгоритм Евклида

    Расширенный Евклид находит $x, y$ такие что:
    $$a \cdot x + n \cdot y = \gcd(a, n)$$

    Если $\gcd(a, n) = 1$, то:
    $$a \cdot x + n \cdot y = 1 \quad \Rightarrow \quad a \cdot x \equiv 1 \pmod{n}$$

    Значит $x$ — и есть мультипликативное обратное.

    ---

    ## Сравнение методов

    | Метод | Время | Память | Когда использовать |
    | :--- | :--- | :--- | :--- |
    | Теорема Эйлера | $O(\sqrt{n} + \log n)$ | $O(1)$ | Когда $n$ простое — формула упрощается до $a^{n-2}$ |
    | Расширенный Евклид | $O(\log n)$ | $O(\log n)$ | Универсальный способ, работает для любого $n$ |
    """)
    return


@app.function
def mod_inverse_euler(a, n):
    if gcd(a, n) != 1:
        return None
    phi = euler_totient(n)
    return fast_power(a, phi - 1, n)


@app.function
def mod_inverse_euclid(a, n):
    g, x, _ = extended_gcd(a % n, n)
    if g != 1:
        return None
    return x % n


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 9. Китайская теорема об остатках (КТО)

    **Задача:** найти $x$, удовлетворяющее системе сравнений:
    $$x \equiv a_1 \pmod{n_1}, \quad x \equiv a_2 \pmod{n_2}, \quad \dots, \quad x \equiv a_k \pmod{n_k}$$
    где все $n_i$ **попарно взаимно просты** ($\gcd(n_i, n_j) = 1$ при $i \ne j$).

    **Теорема:** при этом условии решение существует и **единственно** по модулю $N = n_1 \cdot n_2 \cdot \ldots \cdot n_k$.

    **Формула решения:**
    $$N = \prod_{i=1}^{k} n_i, \qquad N_i = \frac{N}{n_i}, \qquad y_i = N_i^{-1} \pmod{n_i}$$
    $$x = \left(\sum_{i=1}^{k} a_i \cdot N_i \cdot y_i\right) \bmod N$$

    **Почему работает?** Рассмотрим один слагаемый $a_i \cdot N_i \cdot y_i$:

    - По модулю $n_i$: $\;N_i \cdot y_i \equiv 1 \pmod{n_i}$, поэтому слагаемое $\equiv a_i \pmod{n_i}$ ✓
    - По модулю $n_j$ ($j \ne i$): $\;N_i$ содержит $n_j$ как множитель, поэтому слагаемое $\equiv 0 \pmod{n_j}$ ✓

    Итого: каждый слагаемый «отвечает» ровно за одно уравнение системы.

    | Метод | Время | Память |
    | :--- | :--- | :--- |
    | КТО ($k$ уравнений) | $O(k \cdot \log N)$ | $O(k)$ |
    """)
    return


@app.function
def chinese_remainder_theorem(remainders, moduli):
    # Шаг 1: N = произведение всех модулей
    N = 1
    for n in moduli:
        N *= n

    x = 0
    for i in range(len(remainders)):
        ai = remainders[i]
        ni = moduli[i]
        Ni = N // ni                    # Ni = N / ni
        yi = mod_inverse_euclid(Ni, ni) # yi = Ni^(-1) mod ni
        x += ai * Ni * yi

    return x % N


@app.cell
def _():
    # Система: x ≡ 2 (mod 3),  x ≡ 3 (mod 5),  x ≡ 2 (mod 7)
    remainders = [2, 3, 2]
    moduli = [3, 5, 7]
    x = chinese_remainder_theorem(remainders, moduli)
    print(f"x = {x}")
    for a, n in zip(remainders, moduli):
        print(f"  {x} mod {n} = {x % n}  (ожидалось {a})")
    return


if __name__ == "__main__":
    app.run()
