import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from string import punctuation

russian_stopwords = stopwords.words("russian")
punctuation = punctuation.replace('@', '') + '\n'
tt = str.maketrans(dict.fromkeys(punctuation))

def prepareString(text):
    tokens = text.lower().split(' ')
    tok = []
    for token in tokens:
        t = token.translate(tt)
        if t not in russian_stopwords and t != ' ' and t != '':
            tok.append(t)
    return ' '.join(tok)

