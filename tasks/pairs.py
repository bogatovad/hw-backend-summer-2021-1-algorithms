from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    res = []
    if not len(arr1) or not len(arr2):
        return res
    for index in range(min(len(arr1), len(arr2))):
        res.append((arr1[index], arr2[index]))
    return res
