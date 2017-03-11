import random

__author__ = 'hiseh'
__datetime__ = 2017 / 3 / 9


def gen_schulte_grid(grid):
    """
    出N宫舒尔特
    :param grid:
    :return:
    """
    if grid <= 0:
        return

    nums = set(map(str, [i+1 for i in range(grid * grid)]))
    for e in zip(*[iter(random.sample(nums, len(nums)))] * grid):
        print('\t'.join(e))


if __name__ == '__main__':
    gen_schulte_grid(6)
