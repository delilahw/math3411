import galois


m1 = galois.Poly.Degrees([4, 3, 0])
# print(m1)
#
# m = galois.GF2([1, 1, 1, 0, 0, 0, 1])

def main():
    n = int(input("n (Codeword bits): "))
    k = int(input("k (Information bits): "))
    bch = galois.BCH(n, k, primitive_poly=m1)
    print(bch)
    print(f"t = {bch.t}")
    print(f"Generator Poly: m(x) = {bch.generator_poly}")

    while True:
        print()
        d = input("Data: ").strip()
        d_arr = galois.GF2([int(x) for x in reversed(d) if x.isdigit()])

        mode = input('[E]ncode or [D]ecode: ').strip().lower()
        if mode == 'e':
            encode = bch.encode(d_arr)
            print(encode)
            print(galois.GF2([x for x in reversed(encode)]))

        elif mode == 'd':
            print(bch.decode(d_arr, errors=True))


if __name__ == '__main__':
    main()
