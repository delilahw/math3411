def split_parse_ints(s: str, divider: str):
    a, _, b = (x.strip() for x in s.partition(divider))
    if not (a.isnumeric() and b.isnumeric()):
        raise ValueError(f'Values not numeric: {a}, {b}')
    return int(a), int(b)


def get_input():
    raw = input('n[^p] [mod q]: ').strip().lower()

    modulus = None
    if 'mod' in raw:
        np, _, suf = (x.strip() for x in raw.partition('mod'))
        modulus = int(suf)
    else:
        np = raw

    if '^' in np:
        base, power = split_parse_ints(np, '^')
    else:
        base = int(np)
        power = 1

    if modulus is None:
        modulus = int(input('Modulus: '))

    return base, power, modulus


def main():
    base, power, modulus = get_input()
    res = pow(base, power, modulus)
    print(f"{base}^{power} ≡ {res} (mod {modulus})\n")


if __name__ == '__main__':
    while True:
        try:
            main()
        except ValueError as e:
            print(e)
            print()
