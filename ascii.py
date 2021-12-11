from typing import Sequence

message = input('Input message blocks: ')

chars = tuple(message.split())
print()


def vertical_parity(chars):
    digits = list(zip(*chars))
    return (v_digits[:-1].count('1') % 2 == int(v_digits[-1]) for v_digits in digits)


def parity(bits: Sequence[str]):
    first = bits[0]
    rest = bits[1:]
    return rest.count('1') % 2 == int(first)


def correct_char(bit):
    return "0" if bit == "1" else "1"


def decode(chars):
    return (chr(int(x, 2)) for x in (y[1:] for y in chars))


def check_and_correct(chars):
    hp_pos = None
    for i, char in enumerate(chars):
        p = parity(char)
        print(f"{char}  Parity {'OK' if p else '*'}")
        if not p:
            hp_pos = i

    vp = tuple(vertical_parity(chars))
    print(''.join(' ' if col_valid else '*' for col_valid in vp))

    vp_pos = vp.index(False)

    arr_2d = list(chars)
    if hp_pos is not None:
        r = list(arr_2d[hp_pos])
        err_char = r[vp_pos]
        r[vp_pos] = correct_char(err_char)
        arr_2d[hp_pos] = ''.join(r)
        print(f"Error Char: {err_char} -> {arr_2d[hp_pos][vp_pos]}")

    else:
        print("No error detected")

    print("Corrected:")
    print('\n'.join(arr_2d))
    print()
    print("Decoded:")
    print('\n'.join(decode(arr_2d[:-1])))


if __name__ == '__main__':
    check_and_correct(chars)
