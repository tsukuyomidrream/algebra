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


@app.cell(hide_code=True)
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

    ## Частный случай — малая теорема Ферма

    **Малая теорема Ферма:** если $p$ — простое число и $\gcd(a, p) = 1$, то:

    $$a^{p-1} \equiv 1 \pmod{p}$$

    Это **частный случай теоремы Эйлера** при $n = p$ (простое), потому что $\varphi(p) = p - 1$.

    Перепишем теорему: $a \cdot a^{p-2} \equiv 1 \pmod{p}$. Получаем формулу обратного:

    $$a^{-1} \equiv a^{p-2} \pmod{p}$$

    То есть **если модуль простой — обратный считается как $a^{p-2}$**. Это удобнее, чем считать $\varphi(n)$, потому что не нужно факторизовать $n$.

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Деление полиномов над целостным кольцом

    #### Постановка задачи

    Для многочленов $a(x), b(x)$ над целостным кольцом $R$ ($b \ne 0$) найти такие $q(x), r(x) \in R[x]$, что:

    $$
    a(x) = q(x) \cdot b(x) + r(x), \quad \deg r < \deg b
    $$

    Деление возможно не всегда: на каждом шаге старший коэффициент $b$ должен делить текущий старший коэффициент остатка.
    В кольце многочленов над полем деление возможно всегда.

    ---

    #### Алгоритм «школьного» деления

    1. Пока $\deg a \ge \deg b$:
        - Берём $c = \dfrac{a_{\text{старш}}}{b_{\text{старш}}}$, $k = \deg a - \deg b$.
        - Прибавляем $c \cdot x^k$ к частному.
        - Вычитаем $c \cdot x^k \cdot b(x)$ из $a(x)$.
    2. Остаток — то, что получилось от $a(x)$.

    Многочлен хранится списком коэффициентов: p[i] — коэффициент при $x^i$.
    """)
    return


@app.function
def poly_trim(p):
    # Убираем ведущие нули, чтобы старший коэффициент был не нулевой
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


@app.function
def poly_divmod(a, b):
    """
    Делит многочлен a на b в целостном кольце.
    Возвращает (q, r): a = q*b + r, deg(r) < deg(b).
    Бросает ValueError, если деление в кольце невозможно.
    """
    a = poly_trim(a[:])
    b = poly_trim(b[:])

    if b == [0]:
        raise ValueError("Деление на нулевой многочлен")

    deg_b = len(b) - 1
    lead_b = b[-1]

    # Частное заранее не знаем по длине — будем дополнять
    q = [0] * max(1, len(a) - deg_b)

    # Пока степень остатка не меньше степени делителя
    while len(a) - 1 >= deg_b and a != [0]:
        lead_a = a[-1]

        # Деление старших коэффициентов должно быть точным
        if lead_a % lead_b != 0:
            raise ValueError("Деление невозможно в данном кольце")

        coef = lead_a // lead_b
        shift = len(a) - 1 - deg_b
        q[shift] = coef

        # Вычитаем coef * x^shift * b(x) из a(x)
        for i in range(deg_b + 1):
            a[shift + i] -= coef * b[i]

        poly_trim(a)

    return poly_trim(q), a


@app.cell
def _():
    # (x^3 - 1) : (x - 1) = x^2 + x + 1
    poly_divmod([-1, 0, 0, 1], [-1, 1])
    return


@app.cell
def _(mo):
    mo.md(r"""
    # 11.  Вычисления в простых конечных полях (произведение и возведение в степень через битовые операции).

    **Поле Галуа** $\mathrm{GF}(q)$ — это поле из конечного числа элементов, причём количество элементов всегда:

    $$q = p^n$$

    где $p$ — простое число, $n$ — натуральное ($n \ge 1$).


    ## Идея алгоритма умножения в $\mathrm{GF}(p)$

    Хотим посчитать $a \cdot b \bmod p$.

    1. Приводим `a` и `b` по модулю `p` — чтобы остаться в поле.
    2. Заводим `result = 0` — сюда копим ответ.
    3. **Пока в `b` остались биты** (`b > 0`), идём по битам справа налево:
       - Если **последний бит `b` = 1** → прибавляем текущее `a` к `result` (по модулю `p`).
       - Если **последний бит `b` = 0** → пропускаем.
       - **В любом случае:** удваиваем `a` (по модулю `p`) — готовим к следующей степени двойки.
       - Сдвигаем `b` вправо на 1 бит — открываем следующий бит.
    4. Когда все биты `b` обработаны (`b = 0`) — возвращаем `result`.
    """)
    return


@app.function
def gfp_mul(a, b, p):
    # умножение в GF(p) сдвигами и сложениями
    a %= p
    b %= p
    result = 0
    while b > 0:
        if b & 1:                    # младший бит b
            result = (result + a) % p
        a = (a + a) % p              # «сдвиг» a влево
        b >>= 1                      # сдвиг b вправо
    return result


@app.function
def gfp_pow(a, e, p):
    # бинарное возведение в степень в GF(p)
    a %= p
    result = 1
    while e > 0:
        if e & 1:
            result = gfp_mul(result, a, p)
        a = gfp_mul(a, a, p)         # возводим основание в квадрат
        e >>= 1
    return result


@app.cell
def _(mo):
    mo.md(r"""
    ## Обратный элемент в $\mathrm{GF}(p)$ — малая теорема Ферма

    **Малая теорема Ферма:** если $p$ — простое и $\gcd(a, p) = 1$, то:

    $$a^{p-1} \equiv 1 \pmod{p}$$

    Перепишем: $a \cdot a^{p-2} \equiv 1 \pmod{p}$. Сравниваем с определением обратного ($a \cdot a^{-1} = 1$):

    $$a^{-1} \equiv a^{p-2} \pmod{p}$$

    Поэтому, чтобы найти обратный к `a` в $\mathrm{GF}(p)$, достаточно возвести `a` в степень $p - 2$ — что мы уже умеем быстро через `gfp_pow`.
    """)
    return


@app.function
def gfp_inv(a, p):
    # обратный по малой теореме Ферма: a^(p-2) ≡ a^(-1) (mod p)
    return gfp_pow(a, p - 2, p)


@app.cell
def _(mo):
    mo.md(r"""
    # 12. Построение поля GF(256)

    ## $\mathrm{GF}(2^n)$ — расширенное поле из $2^n$ элементов

    $\mathrm{GF}(256) = \mathrm{GF}(2^8) = \mathrm{GF}(2)[x] / f(x)$, где $f(x)$ — неприводимый многочлен степени 8 над $\mathrm{GF}(2)$.

    Стандартный выбор (AES): $f(x) = x^8 + x^4 + x^3 + x + 1$, в двоичном виде $0\mathtt{x11B}$.

    Элементы поля — байты $0\ldots 255$: байт $b_7 b_6 \dots b_0$ кодирует многочлен $b_7 x^7 + \dots + b_0$.

    - **Сложение** — побитовое XOR (коэффициенты складываются по модулю 2).
    - **Умножение** — умножение многочленов плюс редукция по модулю $f(x)$.

    **Трюк редукции:** при сдвиге $a \ll 1$, если выскочил 9-й бит, делаем XOR с $f(x) = 0\mathtt{x11B}$. Старший бит обнулится, остаётся XOR с $0\mathtt{x1B}$.

    ## Обратный элемент в $\mathrm{GF}(256)$ — теорема Лагранжа

    **Теорема Лагранжа (следствие для конечных групп):** в любой конечной группе порядка $n$ для каждого элемента $a$ выполняется:

    $$a^n = e$$

    где $e$ — нейтральный элемент группы.

    **Применение к $\mathrm{GF}(256)$.** Ненулевые элементы $\mathrm{GF}(256)$ образуют **мультипликативную группу** $\mathrm{GF}(256)^*$ порядка $255 = 2^8 - 1$. Нейтральный элемент относительно умножения — это $1$. По теореме Лагранжа, для любого ненулевого $a$:

    $$a^{255} = 1$$

    Перепишем: $a \cdot a^{254} = 1$. Сравниваем с определением обратного:

    $$a^{-1} = a^{254}$$

    Это **обобщение малой теоремы Ферма** на расширенные поля. В $\mathrm{GF}(p^n)$ мультипликативная группа имеет порядок $p^n - 1$, и обратный считается как $a^{p^n - 2}$. Для $\mathrm{GF}(256)$ это $a^{254}$.
    """)
    return


@app.function
def gf256_add(a, b):
    # сложение и вычитание в GF(256) — это XOR
    return a ^ b


@app.function
def gf256_mul(a, b):
    mod = 0x11B
    result = 0
    deg_mod = mod.bit_length() - 1

    while b > 0:
        if b & 1:
            result ^= a
        a <<= 1
        if a.bit_length() > deg_mod:
            a ^= mod
        b >>= 1

    return result


@app.function
def gf256_pow(a, e):
    # бинарное возведение в степень в GF(256)
    result = 1
    while e > 0:
        if e & 1:
            result = gf256_mul(result, a)
        a = gf256_mul(a, a)
        e >>= 1
    return result


@app.function
def gf256_inv(a):
    # порядок мультипликативной группы равен 255, значит a^254 = a^(-1)
    if a == 0:
        raise ZeroDivisionError("0 в GF(256) необратим")
    return gf256_pow(a, 254)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 13. Нахождение неприводимых многочленов над GF(p)

    ## Теория

    **Критерий неприводимости через $x^{p^k}$.** Многочлен $f$ степени $n$ над $\mathrm{GF}(p)$ неприводим тогда и только тогда, когда
    $$\gcd\bigl(f(x),\ x^{p^k} - x\bigr) = 1 \quad \text{для всех } k = 1, 2, \dots, \lfloor n/2 \rfloor.$$

    **Объяснение.** Многочлен $x^{p^k} - x$ — это произведение **всех** неприводимых многочленов над $\mathrm{GF}(p)$, степени которых делят $k$. Если у $f$ есть собственный неприводимый множитель степени $\le n/2$, он обязательно «всплывёт» в каком-то $x^{p^k} - x$ и проявится в $\gcd$.

    Нужны: арифметика в $\mathrm{GF}(p)[x]$ — деление с остатком, НОД, возведение в степень по модулю многочлена.
    """)
    return


@app.function
def poly_add_mod(a, b, p):
    n = max(len(a), len(b))
    r = []
    for i in range(n):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        r.append((ai + bi) % p)
    return r


@app.function
def poly_sub_mod(a, b, p):
    n = max(len(a), len(b))
    r = []
    for i in range(n):
        ai = a[i] if i < len(a) else 0
        bi = b[i] if i < len(b) else 0
        r.append((ai - bi) % p)
    return r


@app.cell
def _(poly_deg):
    def poly_mul_mod(a, b, p):
        if poly_deg(a) < 0 or poly_deg(b) < 0:
            return [0]
        r = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            if ai == 0:
                continue
            for j, bj in enumerate(b):
                r[i + j] = (r[i + j] + ai * bj) % p
        return r

    return (poly_mul_mod,)


@app.cell
def _(poly_deg):
    def poly_divmod_mod(f, g, p):
        # деление с остатком в GF(p)[x]
        f = list(f)
        g = list(g)
        dg = poly_deg(g)
        if dg < 0:
            raise ZeroDivisionError
        lc_inv = mod_inverse_euclid(g[dg], p)
        df = poly_deg(f)
        if df < dg:
            return [0], poly_trim(f)
        q = [0] * (df - dg + 1)
        while poly_deg(f) >= dg:
            d = poly_deg(f)
            c = (f[d] * lc_inv) % p
            q[d - dg] = c
            for i in range(dg + 1):
                f[d - dg + i] = (f[d - dg + i] - c * g[i]) % p
        return poly_trim(q), poly_trim(f)

    return (poly_divmod_mod,)


@app.cell
def _(poly_deg, poly_divmod_mod):
    def poly_gcd_mod(a, b, p):
        # НОД двух многочленов в GF(p)[x] (нормированный)
        a = poly_trim(a)
        b = poly_trim(b)
        while poly_deg(b) >= 0:
            _, r = poly_divmod_mod(a, b, p)
            a, b = b, r
        d = poly_deg(a)
        if d < 0:
            return [0]
        inv = mod_inverse_euclid(a[d], p)
        return [(c * inv) % p for c in a[: d + 1]]

    return (poly_gcd_mod,)


@app.cell
def _(poly_divmod_mod, poly_mul_mod):
    def poly_powmod(base, e, mod, p):
        # base^e mod (многочлен mod), коэффициенты в GF(p)
        result = [1]
        _, base = poly_divmod_mod(base, mod, p)
        while e > 0:
            if e & 1:
                _, result = poly_divmod_mod(poly_mul_mod(result, base, p), mod, p)
            _, base = poly_divmod_mod(poly_mul_mod(base, base, p), mod, p)
            e >>= 1
        return result

    return (poly_powmod,)


@app.cell
def _(poly_deg, poly_gcd_mod, poly_powmod):
    def is_irreducible(f, p):
        # проверка неприводимости через критерий x^(p^k)
        n = poly_deg(f)
        if n <= 0:
            return False
        if n == 1:
            return True
        x = [0, 1]                       # многочлен x
        xpk = x[:]                       # будет хранить x^(p^k) mod f
        for _ in range(1, n // 2 + 1):
            xpk = poly_powmod(xpk, p, f, p)   # возводим в степень p — получаем x^(p^k)
            diff = poly_sub_mod(xpk, x, p)
            g = poly_gcd_mod(f, diff, p)
            if poly_deg(g) > 0:
                return False
        return True

    return (is_irreducible,)


@app.cell
def _(is_irreducible):
    def find_irreducibles(n, p, limit=None):
        # перебор нормированных многочленов степени n над GF(p)
        found = []
        total = p ** n
        for code in range(total):
            coeffs = []
            c = code
            for _ in range(n):
                coeffs.append(c % p)
                c //= p
            coeffs.append(1)             # старший коэффициент = 1
            if is_irreducible(coeffs, p):
                found.append(coeffs)
                if limit and len(found) >= limit:
                    break
        return found

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 14. Квадратные уравнения в GF(p)

    Решаем $a x^2 + b x + c = 0$ в $\mathrm{GF}(p)$, $p$ — нечётное простое.

    ## Теория

    Формула та же, что в школе: $x = \dfrac{-b \pm \sqrt{D}}{2a}$, где $D = b^2 - 4ac$. Но всё считается в $\mathrm{GF}(p)$:

    - **«Деление»** на $2a$ — это умножение на обратный по модулю.
    - **Извлечение $\sqrt{D}$** возможно тогда и только тогда, когда $D$ — квадратичный вычет: $D^{(p-1)/2} \equiv 1 \pmod{p}$ (**критерий Эйлера**).
    - Если $D = 0$ — один корень кратности 2.
    - Если $D$ не вычет — корней в $\mathrm{GF}(p)$ нет.

    Извлечение квадратного корня — **алгоритм Тонелли–Шенкса**:
    1. Записать $p - 1 = q \cdot 2^s$ с нечётным $q$.
    2. Найти неквадратичный вычет $z$.
    3. Через итерации «гасить» 2-компоненту в выражении.

    > **О характеристике 2.** В $\mathrm{GF}(2^n)$ делить на $2a$ нельзя, и формула выше не работает. Там используют замену $x = b y / a$, после которой задача сводится к $y^2 + y = d$; решение существует тогда и только тогда, когда $\mathrm{Tr}(d) = 0$.
    """)
    return


@app.function
def is_qr(a, p):
    # квадратичный вычет по критерию Эйлера
    a %= p
    if a == 0:
        return True
    return gfp_pow(a, (p - 1) // 2, p) == 1


@app.function
def tonelli_shanks(n, p):
    # извлечение квадратного корня из n по модулю простого p; None — корня нет
    n %= p
    if n == 0:
        return 0
    if not is_qr(n, p):
        return None
    if p % 4 == 3:                   # быстрый случай
        return gfp_pow(n, (p + 1) // 4, p)

    # представляем p - 1 = q * 2^s, q — нечётное
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1

    # ищем неквадратичный вычет z
    z = 2
    while is_qr(z, p):
        z += 1

    m = s
    c = gfp_pow(z, q, p)
    t = gfp_pow(n, q, p)
    r = gfp_pow(n, (q + 1) // 2, p)

    while True:
        if t == 1:
            return r
        # ищем наименьшее i, при котором t^(2^i) = 1
        i, temp = 0, t
        while temp != 1:
            temp = gfp_mul(temp, temp, p)
            i += 1
        b = gfp_pow(c, 1 << (m - i - 1), p)
        m = i
        c = gfp_mul(b, b, p)
        t = gfp_mul(t, c, p)
        r = gfp_mul(r, b, p)


@app.function
def solve_quadratic_gfp(a, b, c, p):
    # решает a*x^2 + b*x + c = 0 в GF(p), p — нечётное простое
    a, b, c = a % p, b % p, c % p
    if a == 0:                       # вырожденный случай — линейное уравнение
        if b == 0:
            return "любое x" if c == 0 else []
        return [(-c * mod_inverse_euclid(b, p)) % p]

    D = (b * b - 4 * a * c) % p
    inv_2a = mod_inverse_euclid((2 * a) % p, p)

    if D == 0:
        return [(-b * inv_2a) % p]
    if not is_qr(D, p):
        return []                    # корней в GF(p) нет
    sD = tonelli_shanks(D, p)
    x1 = ((-b + sD) * inv_2a) % p
    x2 = ((-b - sD) * inv_2a) % p
    return sorted({x1, x2})


@app.cell
def _():
    # x^2 + x + 1 = 0 в GF(7): корни {2, 4}, проверка 4+2+1=7≡0, 16+4+1=21≡0
    print("x^2 + x + 1 = 0  в GF(7):  ", solve_quadratic_gfp(1, 1, 1, 7))
    # x^2 - 3 = 0 в GF(7) — нет корней (3 не квадратичный вычет mod 7)
    print("x^2 - 3 = 0      в GF(7):  ", solve_quadratic_gfp(1, 0, -3, 7))
    # x^2 + 4x + 4 = 0 в GF(11): двойной корень x = -2 = 9
    print("x^2 + 4x + 4 = 0 в GF(11): ", solve_quadratic_gfp(1, 4, 4, 11))
    # в большом поле
    p = 10 ** 9 + 7
    print(f"x^2 + 3x + 2 = 0 в GF({p}): {solve_quadratic_gfp(1, 3, 2, p)}")
    return


if __name__ == "__main__":
    app.run()
