from textblob import TextBlob
import operator


# Yes, I know this is bad practice - what can you do? -- No time to write a proper classifier
SCORE_MIN = 10
_temp_wordlist_ = {
    'rape': 10,
    'molest': 10,
    'attack': 10,
    'harass': 10,
    'leering': 10,
    'whistl': 10,
    'inadequate': 10,
    'exploit': 10,
    'sex': 10,
    'stranger': 10,
    'touchy': 5,
    'stop': 3,
    'hurt': 10,
    'report': 8,
    'help': 6,
    'what': -1,
    'away': -5,
    'fatal': -10,
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
    blob = TextBlob(text.lower())
    polarity, subjectivity, score = 0, 0, 0
    for sentence in blob.sentences:
        polarity += sentence.polarity
        subjectivity += sentence.subjectivity
    for word in set(blob.words):
        for word_test in _temp_wordlist_:
            if word_test in word:
                score += _temp_wordlist_[word_test]
    print((score * (1 - polarity) * (1 + subjectivity)))
    return (score * (1 - polarity) * (1 + subjectivity)) > SCORE_MIN


while True:
    print(analyze(input(">> ")))
