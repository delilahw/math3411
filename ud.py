"""
The Sardinas-Patterson Algorithm
Taken from https://towardsdatascience.com/the-sardinas-patterson-algorithm-in-simple-python-9718242752c3
"""


def generate_cn(c: set[str], n):
    if n == 0:
        return set(c)
    else:
        # create a set to hold our new elements
        cn = set()

        # generate c_(n-1)
        cn_minus_1 = generate_cn(c, n - 1)

        for u in c:
            for v in cn_minus_1:
                if (len(u) > len(v)) and u.find(v) == 0:
                    cn.add(u[len(v):])
        for u in cn_minus_1:
            for v in c:
                if len(u) > len(v) and u.find(v) == 0:
                    cn.add(u[len(v):])
        return cn


def generate_c_infinity(c: set[str]):
    cs = []
    c_infinity = set()
    n = 1
    cn = generate_cn(c, n)
    # print('c_{}'.format(n), cn)

    while len(cn) > 0:
        if cn in cs:
            print('Cycle detected. Halting algorithm.')
            break
        else:
            cs.append(cn)
            c_infinity = c_infinity.union(cn)
            n += 1
            cn = generate_cn(c, n)
            # print('c_{}'.format(n), c_infinity)
    return c_infinity


def sardinas_patterson_theorem(c: set[str]):
    """
    Returns True if c is uniquely decodable
    """
    c_infinity = generate_c_infinity(c)
    return len(c.intersection(c_infinity)) == 0


def main():
    raw = input('Codewords: ')
    codewords = set(x.strip() for x in raw.split())
    print(codewords)

    uniquely_decodable = sardinas_patterson_theorem(codewords)
    print(f"is{' ' if uniquely_decodable else ' not '}uniquely decodable")
    print()


if __name__ == '__main__':
    while True:
        main()
