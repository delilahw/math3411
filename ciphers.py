import string
import itertools


def caesar(plaintext: str, shift: int, alphabets: tuple[str] = (string.ascii_lowercase, string.ascii_uppercase)):
    return plaintext.translate(make_caesar_trans(shift, alphabets))


def make_caesar_trans(shift: int,
                      alphabets: tuple[str] = (string.ascii_lowercase, string.ascii_uppercase),
                      reverse: bool = False):
    shifted_alphabets = tuple(map(lambda alphabet: alphabet[shift:] + alphabet[:shift], alphabets))
    alphabets_str = ''.join(alphabets)
    shifted_str = ''.join(shifted_alphabets)
    return str.maketrans(alphabets_str, shifted_str) if not reverse else str.maketrans(shifted_str, alphabets_str)


def make_caesar_trans_from_letter(letter: str, *args, **kwargs):
    if len(letter) != 1 or not letter.isalpha():
        raise ValueError(f'Invalid key letter: {letter}')
    shift = ord(letter.lower()) - ord('a')
    return make_caesar_trans(shift, *args, **kwargs)


def print_vigenere_table():
    for i in range(26):
        print(chr(ord('a') + i) + " | " + caesar(string.ascii_lowercase, i))


def vigenere(plaintext: str, key: str, decipher: bool = False):
    tables = tuple(make_caesar_trans_from_letter(x, reverse=decipher) for x in key)
    table_iter = itertools.cycle(tables)
    ciphertext = ''
    for plain_chr in plaintext:
        if plain_chr.isalpha():
            table = next(table_iter)
            ciphertext += plain_chr.translate(table)
        else:
            ciphertext += plain_chr
    return ciphertext


def feedback(plaintext: str, starting_key: str, feedback_encipher_strategy):
    tables = [make_caesar_trans_from_letter(x) for x in starting_key]
    table_iter = iter(tables)
    ciphertext = ''
    for i, plain_chr in enumerate(plaintext):
        if plain_chr.isalpha():
            table = next(table_iter)
            ciphertext += plain_chr.translate(table)
            feedback_encipher_strategy(tables, i, plaintext, ciphertext)
        else:
            ciphertext += plain_chr
    return ciphertext


def plaintext_feedback_encipher_strategy(tables: list, i: int, plaintext: str, _: str) -> None:
    tables.append(make_caesar_trans_from_letter(plaintext[i]))


def ciphertext_feedback_encipher_strategy(tables: list, i: int, _: str, ciphertext: str) -> None:
    tables.append(make_caesar_trans_from_letter(ciphertext[i]))


def feedback_decipher(ciphertext: str, starting_key: str, feedback_decipher_strategy):
    tables = [make_caesar_trans_from_letter(x, reverse=True) for x in starting_key]
    table_iter = iter(tables)
    plaintext = ''
    for i, cipher_chr in enumerate(ciphertext):
        if cipher_chr.isalpha():
            table = next(table_iter)
            plaintext += cipher_chr.translate(table)
            feedback_decipher_strategy(tables, i, plaintext, ciphertext)
        else:
            plaintext += cipher_chr
    return plaintext


def plaintext_feedback_decipher_strategy(tables: list, i: int, plaintext: str, _: str) -> None:
    tables.append(make_caesar_trans_from_letter(plaintext[i], reverse=True))


def ciphertext_feedback_decipher_strategy(tables: list, i: int, _: str, ciphertext: str) -> None:
    tables.append(make_caesar_trans_from_letter(ciphertext[i], reverse=True))


def test():
    assert vigenere("T H I S I S A N E X A M P L E",
                    "CODECODECODECODECODECODEFGJDHGEGUDFHGJDFG") == "V V L W K G D R G L D Q R Z H"

    assert vigenere("V V L W K G D R G L D Q R Z H", "CODECODE", decipher=True) == "T H I S I S A N E X A M P L E"

    assert feedback("T H I S I S A N E X A M P L E", "CODE",
                    plaintext_feedback_encipher_strategy) == "V V L W B Z I F M P A Z T I E"
    assert feedback("T H I S I S A N E X A M P L E", "CODE",
                    ciphertext_feedback_encipher_strategy) == "V V L W D N L J H K L V W V P"

    assert feedback_decipher("V V L W B Z I F M P A Z T I E", "CODE",
                             plaintext_feedback_decipher_strategy) == "T H I S I S A N E X A M P L E"
    assert feedback_decipher("V V L W D N L J H K L V W V P", "CODE",
                             ciphertext_feedback_decipher_strategy) == "T H I S I S A N E X A M P L E"


def sanitise_key(key: str):
    return ''.join(c.lower() for c in key.strip() if c.isalpha())


def print_output(output: str):
    print(output)
    print(output.replace(' ', ''))
    print()


def main():
    # data = input('Data: ').rstrip()
    print('Input data:')
    raw_data = []
    while True:
        try:
            line = input()
        except EOFError:
            # Done on Ctrl d
            break
        raw_data.append(line)

        if len(raw_data) >= 2:
            # Done on two empty lines
            if all(x == "" or x.isspace() for x in raw_data[-2:]):
                break

    if not raw_data:
        raise ValueError("No data supplied")
    data = '\n'.join(raw_data).strip()

    mode = (input('[E]ncipher, [D]ecipher, or [I]nteractive Vigenère: ').strip().lower() or 'h')[0]
    print()

    if mode == 'h':
        print('Ciphers!\nCopyright (c) 2021 David Wu (@hellodavie). See LICENSE for further details.')
        exit(1)

    key = None
    if mode == 'e' or mode == 'd':
        key = get_key_input()

    if mode == 'e':
        print('Vigenère cipher:')
        print_output(vigenere(data, key))

        print('Plaintext Feedback:')
        print_output(feedback(data, key, plaintext_feedback_encipher_strategy))

        print('Ciphertext Feedback:')
        print_output(feedback(data, key, ciphertext_feedback_encipher_strategy))

    elif mode == 'd':
        print('Vigenère cipher:')
        print_output(vigenere(data, key, decipher=True))

        print('Plaintext Feedback:')
        print_output(feedback_decipher(data, key, plaintext_feedback_decipher_strategy))

        print('Ciphertext Feedback:')
        print_output(feedback_decipher(data, key, ciphertext_feedback_decipher_strategy))

    elif mode == 'i':
        while True:
            print(f"Data:\n{data}")
            key = get_key_input()
            print(f'Vigenère cipher using key "{key}":')
            print_output(vigenere(data, key, decipher=True))
            print()


def get_key_input():
    while True:
        key = sanitise_key(input('Key: '))
        if key:
            break
    if not key:
        raise ValueError("No key supplied")
    return key


test()

if __name__ == '__main__':
    main()
