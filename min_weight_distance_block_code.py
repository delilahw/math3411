import itertools


def hamming_distance(chaine1, chaine2):
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))


digits = {"0", "1"}

all_codewords = list(itertools.product(list(digits), repeat=3))
all_codewords = tuple("".join(i) for i in all_codewords)
print(all_codewords)


def min_dist(cs):
    return min(hamming_distance(c1, c2) for (c1, c2) in itertools.combinations(cs, 2))


def weight(c: str):
    return sum(1 for x in c if x != "0")


def min_weight(cs):
    return min(weight(c) for c in cs)


for cs in itertools.combinations(all_codewords, 3):
    w = min_weight(cs)
    d = min_dist(cs)
    print(cs, w, d)
