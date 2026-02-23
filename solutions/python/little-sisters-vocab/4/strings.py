"""Functions for creating, transforming, and adding prefixes to strings."""

from collections.abc import Sequence

def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return "un" + word


def make_word_groups(vocab_words: Sequence[str]) -> str:
    """Transform a sequence containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: Sequence[str] - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` sequence and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words[0]
    words_with_prefix = [prefix + word for word in vocab_words[1:]]
    return " :: ".join([prefix, *words_with_prefix])


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word.endswith("iness"):
        return word[:-5] + "y"
    if word.endswith("ness"):
        return word[:-4]
    raise ValueError("Word does not end with 'ness'")


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    words = sentence.split()
    if not (-len(words) <= index < len(words)):
        raise IndexError("Index out of range.")
    word = words[index].rstrip(".")
    return word + "en"
