from textblob import TextBlob
from collections import namedtuple
import operator


__constants__ = namedtuple("Constants", ['polarity', 'subjectivity'])(0, 0.2)

# Yes, I know this is bad practice - what can you do? -- No time to write a proper classifier
SCORE_MIN = 10
_temp_wordlist_ = {
    'rape': 10,
    'molest': 10,
    'report': 8,
    'help': 6,
    'what': -1,
    'lol': -10,
    'wtf': -10,
    'gay': -10,
}


def _tuplesum(tuple_list):
    c_sum = (0, 0)
    for tuple in tuple_list:
        c_sum = tuple(map(operator.add, c_sum, tuple))
    return c_sum


def analyze(text):
    blob = TextBlob(text)
    polarity, subjectivity, score = 0, 0, 1
    for sentence in blob.sentences:
        polarity += sentence.polarity
        subjectivity += sentence.subjectivity
    for word in blob.words:
        for word_test in _temp_wordlist_:
            if word_test in word:
                score += _temp_wordlist_[word_test]
    return polarity < __constants__.polarity and subjectivity > __constants__.subjectivity and score >= SCORE_MIN


