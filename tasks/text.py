from tkinter import N, W
from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    words = sorted([(len(item), item)for item in text.split()])
    if not len(words): 
        return (None, None)
    return words[0][1], words[-1][1]
