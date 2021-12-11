from typing import Sequence

MOD = 11


def make_ordinal(n):
    """
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    """
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix


def checksum(digits: Sequence[int]):
    s = 0
    for i, v in enumerate(digits):
        s += (i + 1) * v
    return s


def convert_digit(s: str):
    if s.isdigit():
        return int(s)
    if s.lower() == 'X':
        return 10
    return None


def mod_inverse(x, mod):
    return pow(x, -1, mod)


def verify_isbn(digits):
    c_mod = checksum(digits[:-1]) % MOD
    return c_mod == digits[-1]


def format_isbn(digits):
    return ''.join(str(x) if x != 10 else 'X' for x in digits)


isbn = input('Input ISBN-10: ')
check_digit_input = input('Input digit to correct: ').strip()
check_digit_i = int(check_digit_input) - 1 if len(check_digit_input) else None

digits = tuple(convert_digit(x) for x in isbn if convert_digit(x) is not None)
if len(digits) != 10:
    raise ValueError(f"Input ISBN has {len(digits)} digits, expected 10.")

c = checksum(digits[:-1])
cMod = c % MOD
sD = sum(digits[:-1])
sdMod = sD % MOD

print(digits)
print(format_isbn(digits))
print()

print(f"Checksum: {c} ≡ {cMod} mod {MOD}")
print(f"Sum digits: {sD} ≡ {sdMod} mod {MOD}")
# print(f"Inverse of {sD} mod {MOD}: {mod_inverse(sdMod, MOD)}")

if verify_isbn(digits):
    print('Valid checksum')
else:
    print('Invalid checksum')
    print()

    if check_digit_i is None:
        print('Skipping digit correction')
    else:
        for i in range(10):
            print(f'Trying {make_ordinal(check_digit_i + 1)} digit = {i}')
            new_digits = list(digits)
            new_digits[check_digit_i] = i
            if verify_isbn(new_digits):
                print(f"Correct digit is {i}")
                print(f"Correct ISBN is {format_isbn(new_digits)}")
                break
