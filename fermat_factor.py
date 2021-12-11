import math


def is_square(i: int) -> (bool, int):
    isqrt = math.isqrt(i)
    return i == isqrt ** 2, isqrt


def fermat_factor(n: int):
    sqrt_n = math.sqrt(n)
    t_start = math.ceil(sqrt_n)

    for t in range(t_start, n + 1):
        s2 = t ** 2 - n
        sInZ, s = is_square(s2)
        if sInZ:
            return t - s, t + s, s, t
        t += 1

    return math.nan, math.nan, math.nan


def main():
    n = int(input('Number to factorize: '))

    a, b, s, t = fermat_factor(n)
    print(f"{n} = ab = (t - s)(t + s)")
    print(f"  = {a} * {b}")
    print(f"s = 1/2 * (b - a)\n  = {s}")
    print(f"2s = b - a\n   = {2 * s}")
    print(f"t = {t}")
    print()


if __name__ == '__main__':
    while 1:
        main()
