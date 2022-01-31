__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    if not len(arr):
        return 0

    a = sum([item for item in arr if item % 2 == 1])

    if a == 0:
       return 0
    else:
        return sum([item for item in arr if item % 2 == 0]) / a
