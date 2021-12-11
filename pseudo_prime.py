import math


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def pseudo_prime(n: int, a: int) -> bool:
    """
    :param n: Number to test
    :param a: Base
    :return: False corresponds to "No!"
    """

    if math.gcd(a, n) != 1:
        return False

    if pow(a, n - 1, n) != 1:
        return False

    return True


def lucas_test(n: int, a: int) -> bool or None:
    if not pseudo_prime(n, a):
        return False

    ps = prime_factors(n - 1)
    for p in ps:
        if pow(a, (n - 1) // p, n) != 1:
            return True

    return None


def miller_rabin_test(n: int, a: int):
    if math.gcd(a, n) != 1:
        return False

    def factor(n: int):
        target = n - 1
        p = 0
        while target % 2 == 0:
            p += 1
            target //= 2
        return p, target

    s, t = factor(n)
    print(f"n = 2^s * t + 1\n{n} = 2^{s} * {t} + 1")

    if pow(a, t, n) == 1:
        return True

    for r in range(0, s):
        print(f"Testing a^(2^{r} * {t}) ≡ -1 (mod {n})")
        if pow(a, (2 ** r) * t, n) == -1:
            return True

    return False


def main():
    n = int(input("n: "))
    a = int(input("a (base): "))

    print("[1] Pseudo Prime")
    print("[2] Lucas' Test")
    print("[3] Miller-Rabin Probabilistic Primality Test")
    op = int(input('Operation: '))
    print()

    if op == 1:
        print(f"pseudo_prime: {pseudo_prime(n, a)}")
    elif op == 2:
        res = lucas_test(n, a)
        print(f"lucas_test: {res}")
        if res is None:
            print(res)
        else:
            print("Yes!" if res else "No!")
    elif op == 3:
        print("Probably prime!" if miller_rabin_test(n, a) else "No!")
    else:
        print("Invalid operation!")


if __name__ == '__main__':
    while 1:
        main()
