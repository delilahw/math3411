from math import gcd


def phi(n):
    return len(units(n))


def units(modulo):
    return {num for num in range(1, modulo) if gcd(num, modulo) == 1}


def prim(modulo):
    u = units(modulo)
    return [
        g for g in range(1, modulo)
        if u == {pow(g, powers, modulo) for powers in range(1, modulo)}
    ]


if __name__ == '__main__':
    m = int(input('Modulus: '))
    print()

    u = units(m)
    print(f"φ({m}) = {len(u)}\n")
    print(f"Units:\n{u}\n")

    print(f"Primitive Elements:\n{prim(m)}\n")
