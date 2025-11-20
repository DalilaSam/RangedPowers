from typing import Dict


def letterCounter(text: str) -> Dict[str, int]:
    counter: Dict[str, int] = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            counter[letter] = counter.get(letter, 0) + 1
    return counter