import math
from primitive_elements_units import phi


class RSA:
    def __init__(self, ne: tuple[int, int] = None, pq: tuple[int, int] = None):
        if ne is None and pq is None:
            # Input is sum type `(Int x Int) + (Int x Int)`
            raise ValueError('One of `n, e` or `p, q` must be supplied')

        phi_n = None

        if ne is not None:
            n, e = ne
        else:
            if pq is None:
                raise ValueError('No value supplied for n, expected tuple (p, q).')
            p, q = pq
            if not p or not q:
                raise ValueError('No value supplied for n, expected two primes p and q.')

            n = p * q
            phi_n = (p - 1) * (q - 1)

            e = None
            for i in range(1, phi_n + 1):
                if math.gcd(i, phi_n) == 1:
                    e = i
                    break
            if e is None:
                # Should not happen
                raise ValueError('Could not find e ∈ {1, ..., φ(n)} with gcd(e, φ(n)) = 1')

        self.e = e
        self.n = n
        self.d = pow(e, -1, phi_n if phi_n is not None else phi(n))

    def get_public_key(self) -> (int, int):
        return self.n, self.e

    def get_private_key(self) -> (int, int):
        return self.n, self.d

    def encipher(self, m):
        return pow(m, self.e, self.n)

    def decipher(self, c):
        return pow(c, self.d, self.n)

    def encipher_seq(self, ms):
        return tuple(self.encipher(m) for m in ms)

    def decipher_seq(self, cs):
        return tuple(self.decipher(c) for c in cs)


def standard_encode(s: str) -> list[int]:
    o = []
    for c in s:
        if c.isalpha():
            o.append(3 + ord(c.upper()) - 65)
        else:
            o.append(2)
    return o


def standard_decode(c: list[int] or tuple[int]) -> str:
    o = ''
    for char in (x % 29 for x in c):
        if char <= 2:
            o += ' '
        else:
            o += chr(char - 3 + 65)
    return o


def test():
    assert standard_encode("Hi") == [10, 11]
    assert standard_decode(standard_encode("hi")) == "HI"

    scheme = RSA(ne=(551, 55))
    assert scheme.get_public_key() == (551, 55)
    assert scheme.get_private_key() == (551, 55)

    assert scheme.encipher_seq([10, 11]) == (409, 182)
    assert scheme.decipher_seq((409, 182)) == (10, 11)


def main():
    mode = input('ne or pq: ')
    if 'n' in mode or 'e' in mode:
        n = int(input('n: '))
        e = int(input('e: '))
        scheme = RSA(ne=(n, e))
    else:
        p = int(input('p: '))
        q = int(input('q: '))
        scheme = RSA(pq=(p, q))

    print("\nPublic key:")
    print(scheme.get_public_key())
    print()
    print("Private key:")
    print(scheme.get_private_key())
    print()

    mode = (input('[E]ncipher or [D]ecipher: ').strip().lower())[0]

    if mode == 'e':
        d = input('Data: ')
        print(scheme.encipher_seq(standard_encode(d.rstrip())))
    elif mode == 'd':
        cs_raw = input('Ints: ')
        print()
        cs = (int(x) for x in cs_raw.replace(',', ' ').split() if x.isnumeric())
        seq = scheme.decipher_seq(cs)
        print("Deciphered:")
        print(seq)
        print()
        print("Standard encoding:")
        print(standard_decode(seq))

    print("\n")


if __name__ == '__main__':
    while True:
        main()
