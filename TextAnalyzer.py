from typing import Dict, Tuple, Optional


def letterCounter(text: str) -> Dict[str, int]:
    counter: Dict[str, int] = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            counter[letter] = counter.get(letter, 0) + 1
    return counter

def wordCounter(text: str) -> Dict[str, int]:
    text = text.lower()
    words = text.split()
    counter: Dict[str, int] = {}
    for word in words:
        word = word.strip('.,!?;"\'()[]{}')
        counter[word] = counter.get(word, 0) + 1
    return counter

def sentencesCounter(text: str) -> int:
    import re
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)

def mostCommonWord(text: str) -> Tuple[Optional[str], int]:
    words = wordCounter(text)
    if not words:
        return None, 0
    most_common_word = max(words, key=words.get)
    return most_common_word, words[most_common_word]