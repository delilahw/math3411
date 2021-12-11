import math

from primitive_elements_units import phi


def other_primitives(p: int, r: int) -> set:
    phi_r = phi(r)
    pows = (i for i in range(1, phi_r + 1) if math.gcd(i, phi_r) == 1)
    return set(pow(p, x, r) for x in pows)


if __name__ == '__main__':
    p = int(input("Known primitive: "))
    r = int(input("Radix: "))
    print(list(other_primitives(p, r)))
