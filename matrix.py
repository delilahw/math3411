def transform(matrix):
    if '&' in matrix:
        return transformTeX(matrix)
    else:
        return transformNondelim(matrix)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def transformNondelim(n):
    n_rows = int(input('Num rows (RxC matrix): '))
    # n_cols = int(input('Num cols (RxC matrix): '))
    cols = chunks(list(n), n_rows)
    col_vectors = [f"<{', '.join(x)}>" for x in cols]
    return f"< {' | '.join(col_vectors)} >"


def transformTeX(tex: str):
    rows = [x.strip() for x in tex.replace('&', '|').split('\\')]
    rows = [f"<{x}>" for x in rows if x and x[0].isdigit()]

    return f"< {', '.join(rows)} >"


if __name__ == '__main__':
    message = input('Input matrix: ')
    print(transform(message.strip()))
