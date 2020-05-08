"""@package string_parser
Документация для модуля string_parser
 
Модуль используется для удаления лишних слов и символов из строки. Заранее
генерируется набор удаляемых наборов символов. (Стоп-слова на русском и пунктуация)
"""

import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from string import punctuation

russian_stopwords = stopwords.words("russian")
punctuation = punctuation.replace('@', '') + '\n'
tt = str.maketrans(dict.fromkeys(punctuation))

def prepareString(text):
    """Документация для функции prepareString

    Используется для удаления лишних наборов символов из строки
 
    Входные данные - строка для обработки
    Выходные данные - исходная строка с удаленными стоп-словами и пунктуацией
    """
    tokens = text.lower().split(' ')
    tok = []
    for token in tokens:
        t = token.translate(tt)
        if t not in russian_stopwords and t != ' ' and t != '':
            tok.append(t)
    return ' '.join(tok)

