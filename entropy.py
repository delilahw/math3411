import math
from fractions import Fraction
from decimal import Decimal


def parse_exact(nums_raw: str):
    nums = tuple(x for x in nums_raw.split())
    return tuple(Fraction(x) for x in nums) if '/' in nums_raw else tuple(Decimal(x) for x in nums)


def validate_probabilities(ps: tuple[int]):
    if len(ps) == 1:
        print("Assuming H(x) = −xlog_r(x)−(1−x)log_r(1−x)")
        return ps + (1 - ps[0],)

    if not sum(ps) == 1:
        print("[WARN] Probabilities do not sum to 1")

    return ps


def entropy(ps, radix) -> float:
    ps = (float(p) for p in ps)
    logs = (-p * math.log(p, radix) for p in ps)
    return float(sum(logs))


if __name__ == '__main__':
    radix = int(input('Radix: '))

    while True:
        print()
        raw = input('Probabilities: ')
        if not raw:
            break

        try:
            ps = validate_probabilities(parse_exact(raw))
            e = entropy(ps, radix)
            print(f"Entropy: {e}")
        except:
            pass
