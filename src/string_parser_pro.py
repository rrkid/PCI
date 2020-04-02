import re

digitsDict = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9}

def replaceDigit(value):
    return value if digitsDict.get(value) == None else str(digitsDict.get(value))

def deleteJunk(word):
    reg = re.compile('[^a-zA-Z0-9а-яА-Я@.+-]')
    return reg.sub('', word)
    
def deleteRussian(word):
    reg = re.compile('[^a-zA-Z0-9@.+-]')
    return reg.sub('', word)

def prepareString(text):
    tokens = text.lower().split(' ')
    tok = []
    for token in tokens:
        t = deleteJunk(token)
        t = replaceDigit(t)
        t = deleteRussian(t)
        if t != ' ' and t != '':
            tok.append(t)
    return ' '.join(tok)

if __name__ == '__main__':
    pass
