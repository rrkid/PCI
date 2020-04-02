import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from string import punctuation

russian_stopwords = stopwords.words("russian")
russian_stopwords[:] = ['' if x in ['один', 'два', 'три'] else x for x in russian_stopwords]
punctuation = punctuation.replace('@', '') + '\n'
tt = str.maketrans(dict.fromkeys(punctuation))

digitsDict = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9}

def replaceDigit(value):
    return value if digitsDict.get(value) == None else str(digitsDict.get(value))

def prepareString(text):
    tokens = text.lower().split(' ')
    tok = []
    for token in tokens:
        t = token.translate(tt)
        if t not in russian_stopwords and t != ' ' and t != '':
            t = replaceDigit(t)
            tok.append(t)
    return ' '.join(tok)


if __name__ == '__main__':
    pass


