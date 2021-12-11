def order(m: int, a: int) -> int:
    i = 1
    while pow(a, i, m) != 1:
        i += 1
    return i


if __name__ == '__main__':
    while 1:
        print('ord_m(a)')
        m = int(input('m: '))
        a = int(input('a: '))
        print(f"ord_{m}({a}) = {order(m, a)}\n")
