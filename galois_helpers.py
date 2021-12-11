import numpy as np
import galois


def minimal_polynomial(order: int, power: int = 1):
    GF = galois.GF(order)
    e = GF.primitive_element
    m_e = galois.minimal_poly(e ** power)
    return m_e


def powers(order: int):
    GF = galois.GF(order)
    alpha = GF.primitive_element
    pretty_data = []
    for i in range(1, order):
        with GF.display("poly"):
            pretty_data.append((f"α^{i}", GF._print_poly(element=alpha ** i), str(alpha ** i)))
    max_pow_len = max(len(x[0]) for x in pretty_data)
    max_col_1_len = max(len(x[1]) for x in pretty_data) + 4
    for line in pretty_data:
        print(f'{line[0]:{max_pow_len}} = {line[1]:{max_col_1_len}} {line[2]}')


if __name__ == '__main__':
    print('1. Minimal polynomial of GF(ord)')
    print('2. Power table of GF(ord)')
    op = int(input('Operation: '))

    if op == 1:
        ord = int(input('Order GF(p^n): '))
        p = int(input('Power (a^p): '))
        print(minimal_polynomial(ord, p))
    elif op == 2:
        ord = int(input('Order GF(p^n): '))
        print()
        powers(ord)
    print("\n")
