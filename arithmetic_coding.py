import re
import itertools
from decimal import Decimal

probabilities = ('.3', '.6', '.1')


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def parse_intervals(ints: str):
    between_parens_all = re.findall('\[(.*?)\)', ints.replace('(', '['))
    print(between_parens_all)

    intervals = []
    for start, _, end in (x.partition(',') for x in between_parens_all):
        start_d = Decimal(start.strip())
        end_d = Decimal(end.strip())
        intervals.append((start_d, end_d, end_d - start_d))

    return intervals


def make_intervals(probabilities):
    decimal_probabilities = [Decimal(x) for x in probabilities]
    if sum(decimal_probabilities) != 1:
        print(f"[WARN] Probabilities do not sum to 1")

    intervals = []
    for p in decimal_probabilities:
        start = intervals[-1][1] if len(intervals) else 0
        end = start + p
        intervals.append((start, end, p))

    return intervals


def validate_intervals(intervals) -> bool:
    if intervals[0][0] != 0:
        print("First interval does not start at 0")
        return False

    if intervals[-1][1] != 1:
        print("Last interval does not end at 1")
        return False

    for i in intervals:
        interval_start, interval_end, sym_prob = i
        if interval_end - interval_start != sym_prob:
            print(f"Interval has incorrect probability (or bounds): {i}")

    for interval_0, interval_1 in pairwise(intervals):
        interval_0_start, interval_0_end, sym_0_probability = interval_0
        interval_1_start, interval_1_end, sym_1_probability = interval_1

        if interval_0_end != interval_1_start:
            return False

    print(f"Intervals validated: {intervals}")
    return True


def prompt_intervals():
    raw = input("Intervals or probabilities: ")
    if '(' in raw or '[' in raw:
        return parse_intervals(raw)

    probs = (x.strip() for x in raw.split() if x)
    return make_intervals(probs)


def encode(symbols: str, intervals):
    symbol_indices = tuple(int(x) for x in symbols.strip().split('s') if x)
    print(symbol_indices)

    sym_indices_zero = (x - 1 for x in symbol_indices)

    starting = Decimal(0)
    width = Decimal(1)

    for sym_i in sym_indices_zero:
        interval_start, interval_end, sym_probability = intervals[sym_i]
        starting = starting + interval_start * width
        width *= sym_probability

    print(f"starting={starting}, width={width}")
    print(f"encoding_interval=[{starting}, {starting + width})")
    return starting, width


def match_interval(n: Decimal, intervals):
    for i, interval in enumerate(intervals):
        if interval[0] <= n < interval[1]:
            return i, interval
    return None


def decode(n: Decimal, stop_symbol: int, intervals):
    if stop_symbol < len(intervals):
        print("Not enough intervals to arrive at stop symbol")
        return None

    rescaled = n
    initial_match = match_interval(n, intervals)
    matched_intervals = [initial_match[1]]
    symbol_indices = [initial_match[0]]

    for i in range(256):
        last_start, last_end, last_prob = matched_intervals[-1]
        rescaled = (rescaled - last_start) / last_prob

        current_symbol_index, current_interval = match_interval(rescaled, intervals)
        symbol_indices.append(current_symbol_index)
        matched_intervals.append(current_interval)

        if current_symbol_index + 1 == stop_symbol:
            break

    symbols = (x + 1 for x in symbol_indices)

    print('\nMatched Intervals: ')
    print(matched_intervals)

    print('\nDecoded Symbols: ')
    formatted_symbols = tuple(f"s{i}" if i != stop_symbol else '*' for i in symbols)
    print(' '.join(formatted_symbols))
    print(''.join(formatted_symbols))

    return symbols, matched_intervals


def main():
    mode = input('[E]ncode or [D]ecode: ').strip().lower()
    i = input('Input: ')

    intervals = prompt_intervals()
    if not validate_intervals(intervals):
        exit(1)

    if mode == 'e':
        encode(i, intervals)
    elif mode == 'd':
        stop_symbol_raw = input('Stop symbol ("3" or "s3"): ')
        stop_symbol = int(''.join(c for c in stop_symbol_raw if c.isdigit()))
        decode(Decimal(i), stop_symbol, intervals)
    else:
        main()


if __name__ == '__main__':
    # print(validate_intervals(make_intervals(['0.4', '.3', '.2', '.1'])))
    # decode(Decimal('0.12345'), 4, make_intervals(['0.4', '.3', '.2', '.1']))
    # print(encode('s2s1s1s3', make_intervals(probabilities)))
    main()
