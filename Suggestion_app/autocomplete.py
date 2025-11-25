from .models import KatahoWord
from .trie import Trie

# Global Trie (for all Nepali/Hindi words)
TRIE = Trie()


def load_trie():
    """
    Loads trie with roman_code as key and kataho_code as value.
    """
    global TRIE
    TRIE = Trie()

    words = KatahoWord.objects.values_list("roman_code", "kataho_code")

    for roman, devanagari in words:
        if roman:  # skip empty roman codes
            TRIE.insert_key_value(roman, devanagari)

    print("Trie loaded with words:", KatahoWord.objects.count())


def get_suggestions(prefix):
    """
    prefix: typed roman letters, e.g. 'ka', 'pra', 'bi'
    returns: list of devanagari words
    """
    return TRIE.suggest(prefix)
