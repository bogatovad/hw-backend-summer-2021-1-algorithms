from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    res = []
    if not len(arr1) or not len(arr2):
        return res
    for index in range(len(arr1)):
        for index_ in range(len(arr2)):
            res.append((arr1[index], arr2[index_]))
    return res
