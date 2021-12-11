import re


def find_max_prefix(string: str, d):
    max_len = -1
    max_match = None
    for i, p in enumerate(d):
        if len(p) <= max_len:
            continue
        if string.startswith(p):
            max_len = len(p)
            max_match = (i, p)
    return max_match


def print_dictionary(d):
    print('dict: ', end='')
    for i, a in enumerate(d):
        print((i,) + tuple(a), end=' ')
    print()


def encode(input_word: str):
    dictionary = ['']
    current_input = input_word
    output = []
    while current_input:
        matched_prefix = find_max_prefix(current_input, dictionary)
        if matched_prefix is not None:
            prefix_key, prefix = matched_prefix
            current_input = current_input[len(prefix):]

            next_chr = current_input[0]
            current_input = current_input[1:]

            dictionary.append(prefix + next_chr)
            output.append((prefix_key, next_chr))
        print_dictionary(dictionary)

    print('\nEncoded: ')
    print(output)
    return output


def parse_encoded(dict_str: str):
    o = []
    between_parens_all = re.findall('\((.*?)\)', dict_str)
    print(between_parens_all)
    for b in between_parens_all:
        n, _, c_raw = b.partition(',')
        # Default to space if there is no char, assume the stripped space is literal
        c_stripped = c_raw.strip()
        o.append((int(n.strip()), c_stripped if c_stripped else ' '))
    for e in o:
        if len(e[1]) != 1:
            print(f"[WARN] Parsed input is not one char: {e}")
    return o


def decode(input_raw: str):
    parsed_input = parse_encoded(input_raw)
    print(parsed_input)

    d = ['']
    for d_key, char in parsed_input:
        d_entry = d[d_key]
        d.append(d_entry + char)

    print('\nDecoded: ')
    print(''.join(d))
    return d


def main():
    mode = input('[E]ncode or [D]ecode: ').strip().lower()
    i = input('Input: ')

    if mode == 'e':
        encode(i)
    elif mode == 'd':
        decode(i)
    else:
        main()


if __name__ == '__main__':
    main()
