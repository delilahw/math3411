import math
from fractions import Fraction
from decimal import Decimal


def parse_exact(nums_raw: str):
    nums = tuple(x for x in nums_raw.split())
    return tuple(Fraction(x) for x in nums) if '/' in nums_raw else tuple(Decimal(x) for x in nums)


def parse_floats(nums_raw):
    nums = (x for x in nums_raw.split())
    return (float(x) for x in nums)


def validate_probabilities(ps):
    if sum(ps) != 1:
        print("[WARN] Probabilities do not sum to 1")
    return ps


def get_lengths(ps, radix):
    ps = tuple(float(x) for x in ps)
    return tuple(math.ceil(-math.log(p, radix)) for p in ps)


def codewords(ps, radix):
    enumerated = enumerate(ps, start=1)
    ps_sorted = sorted(enumerated, key=lambda x: x[1])
    print(ps_sorted)


if __name__ == '__main__':
    raw = input('Probabilities: ')
    radix = int(input('Radix: '))
    ps = validate_probabilities(parse_exact(raw))
    lengths = get_lengths(ps, radix)

    for i, (p, l) in enumerate(zip(ps, lengths), start=1):
        print(f"p{i} = {p}, l{i} = {l}")

    avg_len = sum(p_i * l_i for (p_i, l_i) in zip(ps, lengths))
    print(f"Avg Length = {avg_len}")

    # codewords(ps, radix)
