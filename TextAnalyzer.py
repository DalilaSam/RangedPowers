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

def result(text: str) -> None:
    letters = letterCounter(text)
    words = wordCounter(text)
    sentences = sentencesCounter(text)
    common_word, frequency = mostCommonWord(text)

    print("Letter Counting:")
    for letter, amount in sorted(letters.items()):
        print(f"'{letter}': {amount}")
    print("\nWord Counting:")
    for word, amount in sorted(words.items()):
        print(f"'{word}': {amount}")
    print(f"\nNumber of sentences: {sentences}")
    if common_word:
        print(f"\nThe most common word is '{common_word}' with a frequency of {frequency}.")
    else:
        print("\nThere are no words in the text.")

text = "The Industrial Revolution marked a significant turning point in human history. It began in the late 18th century and continued into the 19th century, bringing about profound changes in agriculture, manufacturing, mining, transportation, and technology. The shift from agrarian and handcrafted economies to industrial and machine-based ones had far-reaching consequences for society. One of the key catalysts for the Industrial Revolution was the invention of the steam engine, which revolutionised transportation and allowed for the mechanisation of various industries. Factories emerged, creating urbanisation as people moved from rural areas to work in these new industrial centres. The impact on the labour force was dramatic, with a shift from manual labour to machine-based production. The Industrial Revolution also had social and cultural implications. It led to the rise of the middle class, changes in family structures, and the spread of new ideas and philosophies. While it brought about economic prosperity and technological advancements, it also led to social inequalities, poor working conditions, and environmental challenges."

result(text)
