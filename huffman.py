from typing import Sequence, List
from fractions import Fraction


class Node:
    def __init__(self, probability, name=None, children=None):
        self.probability = probability
        self.name = name
        self.children: List[Node] = [] if children is None else children
        self.codeword_digit = ''

    def __repr__(self):
        return f"{self.name}:{self.probability}"


def huffman(symbols: Sequence[Node], radix: int):
    nodes: List[Node] = list(symbols)

    # Add dummy symbols
    if radix > 2:
        dummy_count = 1
        while len(nodes) % (radix - 1) != 1:
            dummy = Node(0, f"d{dummy_count}")
            nodes.append(dummy)
            dummy_count += 1
            print(nodes)
    print(nodes)

    nodes = sorted(nodes, key=lambda x: x.probability, reverse=True)

    while len(nodes) > 1:
        # Combine `r` smallest nodes
        to_combine = nodes[-radix:]
        total_probability = 0
        combined_name = []
        for i in range(radix):
            node = to_combine[i]
            node.codeword_digit = str(i)
            total_probability += node.probability
            combined_name.append(node.name)

        combined_node = Node(total_probability, '_'.join(combined_name), to_combine)

        # Insert combined node with place-high strategy
        without_nodes = nodes[:-radix]
        pos = len(without_nodes)
        print(without_nodes, combined_node)
        # Reverse but keep original indices
        for i, node in reversed(list(enumerate(without_nodes))):
            print(combined_node.probability, node.probability, i, pos)
            if node.probability <= combined_node.probability:
                pos = i
            else:
                break
        print(pos)
        without_nodes.insert(pos, combined_node)

        nodes = without_nodes
        print(nodes)

    return nodes


def traverse_root_node(node: Node):
    avg_codeword_len = 0

    def traverse_node(node: Node, codeword=''):
        nonlocal avg_codeword_len

        codeword = codeword + node.codeword_digit

        if node.children:
            avg_codeword_len += node.probability
            for i, v in enumerate(node.children):
                traverse_node(v, codeword)
        else:
            print(f"{node.name} -> p: {node.probability} -> c: {codeword}")

    traverse_node(node)
    print(f'L_avg = {avg_codeword_len}')


def do_huffman(symbols: Sequence[Node], radix: int):
    result_nodes = huffman(symbols, radix)
    print()
    traverse_root_node(result_nodes[0])


if __name__ == '__main__':
    input_probs = '8/17 2/17 2/17 2/17 2/17 1/17'
    input_probs = input('Probabilities: ')
    input_probs = input_probs.replace(',', '')
    radix = int(input('Radix: '))

    symbols = tuple(Node(Fraction(x), f"s{i}") for i, x in enumerate(input_probs.split(), 1))
    print(symbols)

    do_huffman(symbols, radix)
