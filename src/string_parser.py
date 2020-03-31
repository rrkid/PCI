import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from string import punctuation

russian_stopwords = stopwords.words("russian")
punctuation = punctuation.replace('@', '') + '\n'
tt = str.maketrans(dict.fromkeys(punctuation))

def prepareString(text):
    res_text = []
    text = text.lower().split()

    for word in text:
        res_str = ""
        for i in range(len(word)):
            if (word[i] >= '0' and word[i] <= '9') or (word[i] >= 'a' and word[i] <= 'z'):
                res_str += word[i]
        if (res_str != ''):
            res_text.append(res_str)
            
    return ' '.join(res_text)
