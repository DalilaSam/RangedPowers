from typing import Dict, Tuple, Optional


def letterCounter(text: str) -> Dict[str, int]:
    """
    Count the frequency of each letter in the given text.
    This function ignores non-letter characters and transforms all letters
    to lowercase. Each occurrence of a letter increments its count.
    Parameters:
        text (str): The input text to analyze.
    Returns:
        Dict[str, int]: A dictionary mapping each letter to its frequency.
    """
    counter: Dict[str, int] = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            counter[letter] = counter.get(letter, 0) + 1
    return counter

def wordCounter(text: str) -> Dict[str, int]:
    """
    Count the frequency of each word in the given text.
    The function transforms all text to lowercase, splits it into words,
    removes punctuation from each word, and counts occurrences.
    Parameters:
        text (str): The input text to analyze.
    Returns:
        Dict[str, int]: A dictionary mapping each word to its frequency.
    """
    text = text.lower()
    words = text.split()
    counter: Dict[str, int] = {}
    for word in words:
        word = word.strip('.,!?;"\'()[]{}')
        counter[word] = counter.get(word, 0) + 1
    return counter

def sentencesCounter(text: str) -> int:
    """
    Count the number of sentences in the given text.
    The function uses regular expressions to split the text by punctuation
    marks that typically end a sentence (period, exclamation mark, question mark).
    Empty entries are filtered out.
    Parameters:
        text (str): The input text to analyze.
    Returns:
        int: The total number of detected sentences.
    """
    import re
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return len(sentences)

def mostCommonWord(text: str) -> Tuple[Optional[str], int]:
    """
    Find the most common word in the given text.
    The function uses `wordCounter()` to get word frequencies,
    then returns the word with the highest frequency along with its count.
    Parameters:
        text (str): The input text to analyze.
    Returns:
        Tuple[Optional[str], int]: The most frequent word and its occurrence count.
                                   Returns (None, 0) if no words exist.
    """
    words = wordCounter(text)
    if not words:
        return None, 0
    most_common_word = max(words, key=words.get)
    return most_common_word, words[most_common_word]

def result(text: str) -> None:
    """
    Display the results of the text analysis.
    This includes:
      - Letter frequency
      - Word frequency
      - Sentence count
      - Most common word and its frequency
    Parameters:
        text (str): The text to analyze.
    """
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
