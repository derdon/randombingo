import random
from collections import namedtuple
from itertools import zip_longest

DICT_FILENAME = 'words-de.txt'


Point = namedtuple('Point', ['x', 'y'])


# copied from https://docs.python.org/library/itertools.html#itertools-recipes
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def generate_words(count):
    with open(DICT_FILENAME) as f:
        lines = list(f)
    return [random.choice(lines).strip() for _ in range(count)]
