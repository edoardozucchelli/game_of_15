from src.grid_generator import (count_inversions,
                                is_odd,
                                is_even,
                                pattern_is_legit,
                                aggregate,
                                blank_index,
                                pattern_almost_solved,
                                create_pattern,
                                create_grid)

test_1 = [2, 3, 1, 0]
test_2 = [1, 0, 3, 2]
test_2_not_legit = [1, 0, 2, 3]
test_3 = [6, 13, 7, 10, 8, 9, 11, 0, 15, 2, 12, 5, 14, 3, 1, 4]
test_4 = [12, 1, 10, 2, 7, 11, 4, 14, 5, 0, 9, 15, 8, 13, 6, 3]
test_5 = [1, 8, 2, 0, 4, 3, 7, 6, 5]
test_6_not_legit = [3, 9, 1, 15, 14, 11, 4, 6, 13, 0, 10, 12, 2, 7, 8, 5]


def test_count_inversions():
    assert count_inversions(test_1, 0) == 2
    assert count_inversions(test_2, 0) == 1
    assert count_inversions(test_2_not_legit, 0) == 0
    assert count_inversions(test_3, 0) == 62
    assert count_inversions(test_4, 0) == 49
    assert count_inversions(test_5, 0) == 10
    assert count_inversions(test_6_not_legit, 0) == 56


def test_is_odd():
    assert is_odd(3) is True
    assert is_odd(2) is False


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False


def test_aggregate():
    odd_lst = [1, 2, 3, 4]
    odd_aggr_generator = aggregate(odd_lst, 2)

    assert next(odd_aggr_generator) == (1, 2)
    assert next(odd_aggr_generator) == (3, 4)

    even_lst = [1, 2, 3, 4, 5, 6]
    even_aggr_generator = aggregate(even_lst, 3)

    assert next(even_aggr_generator) == (1, 2, 3)
    assert next(even_aggr_generator) == (4, 5, 6)


def test_blank_index():
    lst = [1, 2, 3, 4]
    assert blank_index(lst, 4, 2) == 1

    assert blank_index(test_1, 3, 2) == 0
    assert blank_index(test_1[::-1], 3, 2) == 1

    assert blank_index(test_3, 15, 4) == 2
    assert blank_index(test_3[::-1], 15, 4) == 1


def test_pattern_almost_solved():
    lst_1 = [0, 1, 2, 3]
    assert pattern_almost_solved(lst_1, 3) is True

    lst_2 = [0, 1, 3, 2]
    assert pattern_almost_solved(lst_2, 3) is True

    lst_3 = [3, 1, 0, 2]
    assert pattern_almost_solved(lst_3, 3) is False


def test_create_pattern():
    assert create_pattern(length=4) == [0, 1, 2, 3]


def test_pattern_is_legit_0():
    assert pattern_is_legit(4, test_4, 0) is True

    assert pattern_is_legit(2, test_2, 0) is True
    assert pattern_is_legit(2, test_2_not_legit, 0) is False

    assert pattern_is_legit(4, test_3, 0) is True

    assert pattern_is_legit(3, test_5, 0) is True
    assert pattern_is_legit(2, test_6_not_legit, 0) is False


def test_pattern_is_legit_blank_first():
    lst_legit = [
        (0, 1, 3, 2),
        (0, 2, 1, 3),
        (0, 3, 2, 1),
        (1, 0, 3, 2),
        (1, 2, 0, 3),
        (1, 2, 3, 0),
        (2, 0, 1, 3),
        (2, 3, 0, 1),
        (2, 3, 1, 0),
        (3, 0, 2, 1),
        (3, 1, 0, 2),
        (3, 1, 2, 0)
    ]

    for tpl in lst_legit:
        assert pattern_is_legit(2, tpl, 0) is True

    lst_not_legit = [
        (0, 1, 2, 3),
        (0, 2, 3, 1),
        (0, 3, 1, 2),
        (1, 0, 2, 3),
        (1, 3, 0, 2),
        (1, 3, 2, 0),
        (2, 0, 3, 1),
        (2, 1, 0, 3),
        (2, 1, 3, 0),
        (3, 0, 1, 2),
        (3, 2, 0, 1),
        (3, 2, 1, 0)
    ]

    for tpl in lst_not_legit:
        assert pattern_is_legit(2, tpl, 0) is False


def test_pattern_is_legit_blank_last():
    lst_legit = [
        (0, 1, 2, 3),
        (0, 1, 3, 2),
        (0, 3, 2, 1),
        (1, 2, 0, 3),
        (1, 2, 3, 0),
        (1, 3, 0, 2),
        (2, 0, 1, 3),
        (2, 0, 3, 1),
        (2, 3, 1, 0),
        (3, 0, 2, 1),
        (3, 1, 0, 2),
        (3, 2, 1, 0)
    ]

    for tpl in lst_legit:
        assert pattern_is_legit(2, tpl, 3) is True

    lst_not_legit = [
        (0, 2, 1, 3),
        (0, 2, 3, 1),
        (0, 3, 1, 2),
        (1, 0, 2, 3),
        (1, 0, 3, 2),
        (1, 3, 2, 0),
        (2, 1, 0, 3),
        (2, 1, 3, 0),
        (2, 3, 0, 1),
        (3, 0, 1, 2),
        (3, 1, 2, 0),
        (3, 2, 0, 1),
    ]

    for tpl in lst_not_legit:
        assert pattern_is_legit(2, tpl, 3) is False


def test_pattern_is_legit_3_x_3():
    lst_legit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert pattern_is_legit(4, lst_legit, 9) is True

    lst_legit_2 = [1, 2, 3, 4, 5, 6, 7, 9, 8]
    assert pattern_is_legit(4, lst_legit_2, 9) is True

    lst_not_legit = [8, 7, 2, 1, 4, 6, 3, 5, 9]
    assert pattern_is_legit(4, lst_not_legit, 9) is False

    lst_not_legit_2 = [1, 2, 3, 4, 5, 6, 8, 7, 9]
    assert pattern_is_legit(4, lst_not_legit_2, 9) is False


def test_pattern_is_legit_4_x_2():
    lst_legit = [1, 2, 3, 4, 5, 6, 7, 8]
    assert pattern_is_legit(4, lst_legit, 8) is True

    lst_legit_2 = [1, 2, 3, 4, 5, 6, 8, 7]
    assert pattern_is_legit(4, lst_legit_2, 8) is True

    lst_not_legit = [8, 7, 2, 1, 4, 6, 3, 5]
    assert pattern_is_legit(4, lst_not_legit, 8) is False

    lst_not_legit_2 = [1, 2, 3, 4, 5, 7, 6, 8]
    assert pattern_is_legit(4, lst_not_legit_2, 8) is False


def test_create_grid():
    lst_1 = [0, 1, 2, 3]
    grid_2_x_2 = {
        (0, 0): 0, (1, 0): 1,
        (0, 1): 2, (1, 1): 3
    }

    assert create_grid(lst_1, 2, 2) == grid_2_x_2

    lst_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    grid_3_x_3 = {
        (0, 0): 0, (1, 0): 1, (2, 0): 2,
        (0, 1): 3, (1, 1): 4, (2, 1): 5,
        (0, 2): 6, (1, 2): 7, (2, 2): 8
    }

    assert create_grid(lst_2, 3, 3) == grid_3_x_3

    lst_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    grid_4_x_4 = {
        (0, 0): 0,  (1, 0): 1,  (2, 0): 2,  (3, 0): 3,
        (0, 1): 4,  (1, 1): 5,  (2, 1): 6,  (3, 1): 7,
        (0, 2): 8,  (1, 2): 9,  (2, 2): 10, (3, 2): 11,
        (0, 3): 12, (1, 3): 13, (2, 3): 14, (3, 3): 15
    }

    assert create_grid(lst_3, 4, 4) == grid_4_x_4
