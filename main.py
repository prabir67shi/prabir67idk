LEXICON={
    "good": 2, "great": 3, "amazing": 3, "love": 3, "fast": 1, "worth": 2, "awesome": 3, "excellent": 3, "nice": 2, "perfect": 3, "bad": -2, "terrible": -3, "slow": -1, "broke": -2, "disappointed": -2, "awful": -3, "hate": -3, "poor": -2, "useless": -3,

}

NEGATIONS = {"not", "no", "never", "hardly"}
INTENSIFIERS = {"very": 2, "really": 2, "so": 2, "extremely": 3}

USE_BUT_RULE = False
USE_NEGATION_WINDOW = False
USE_NEGATION_WINDOW = 3
PUNCTUATION =  ".,!?:;\"'()"


def clean_word(word):
    return word.lower().strip(PUNCTUATION)

def is_negative