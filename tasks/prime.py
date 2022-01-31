__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number == 1:
        return False
    
    if number == 0:
        return False

    if number % 2 == 0:
        return number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number

# a = [(1, False),
#     (0, False),
#     (2, True),
#     (3, True),
#     (4, False),
#     (5, True),
#     (113, True),
#     (199, True),
#     (1999, True),
#     (2000, False)]

# for i in a:
#     print(is_prime(i[0]))