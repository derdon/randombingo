import random
from itertools import zip_longest


# copied from https://docs.python.org/library/itertools.html#itertools-recipes
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def bingo_from_iterable(values, num_cols):
    filtered_values = list(filter(
        lambda value: value is not None and value.strip(), values))
    random.shuffle(filtered_values)
    return grouper(filtered_values, num_cols, '[BLANK]')
