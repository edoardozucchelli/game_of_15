import random


def count_inversions(arr, blank):
    n = len(arr)
    inv_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] != blank and arr[i] != blank and arr[i] > arr[j]:
                inv_count += 1

    return inv_count


def is_odd(n):
    return n % 2 != 0


def is_even(n):
    return n % 2 == 0


def aggregate(lst, group_length):
    for i in range(0, len(lst), group_length):
        group = lst[i:i+group_length]
        if len(group) == group_length:
            yield tuple(group)


def blank_index(lst, blank, width):
    aggregate_list = list(aggregate(lst=lst, group_length=width))
    for arr in aggregate_list:
        if blank in arr:
            return aggregate_list.index(arr)


def pattern_is_legit(width, pattern, blank):
    row = blank_index(lst=pattern[::-1], blank=blank, width=width) + 1

    if is_odd(width):
        if is_even(count_inversions(pattern, blank)):
            return True

    elif is_even(width):
        if is_even(row) and is_odd(count_inversions(pattern, blank)):
            return True
        elif is_odd(row) and is_even(count_inversions(pattern, blank)):
            return True

    return False


def pattern_almost_solved(pattern, blank):
    return count_inversions(arr=pattern, blank=blank) < 1


def create_pattern(length):
    number_list = [n for n in range(length)]
    return number_list


def create_legit_pattern(width, height, blank):
    while True:
        pattern = create_pattern(length=width*height)
        random.shuffle(pattern)
        if pattern_is_legit(width, pattern, blank) and not pattern_almost_solved(pattern, blank):
            return pattern


def create_grid(lst, width, height):
    dict_grid = dict()
    iter_lst = iter(lst)

    for y in range(height):
        for x in range(width):
            dict_grid[(x, y)] = next(iter_lst)
    return dict_grid


def create_legit_grid(width, height, blank):
    legit_pattern = create_legit_pattern(width, height, blank)
    legit_grid = create_grid(lst=legit_pattern, width=width, height=height)
    return legit_grid
