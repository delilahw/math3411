from itertools import combinations
from math import comb

def main():
    raw = input('Elements: ')

    els = raw.strip().replace(',', ' ').split()
    n = len(els)

    r_raw = input('r: ')
    if r_raw:
        r = int(r_raw)
    else:
        r = None

    for i in ((r,) if r is not None else range(1, n + 1)):
        print(f"{n}C{i} = {comb(n, i)}")
        cs = combinations(els, i)
        print('  '.join('(' + ', '.join(c) + ')' for c in cs))
        print()


if __name__ == '__main__':
    while 1:
        main()
