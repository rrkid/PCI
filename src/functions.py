"""@package functions
Документация для модуля functions
 
Модуль используется для обработки данных для работы с vowpalwabbit
"""

import pandas as pd
import numpy as np
import string
import re
from vowpalwabbit import pyvw

phone = r'((8\D{0,2}9|7\D{0,2}9|9)\D{0,2}(\d\D{0,2}){9,9})'
nik = r'(@\S*)'
vk = r'(vk\.com\/\w*)'
i_d = r'(id\/\d*)'
site = r'(\w*\.(ru|com|net|org|biz|edu|gov|info|by|рф|бел|ua|укр))'
dis = r'(\w*#\d*)'
CONTACT = '|'.join([phone, nik, vk, i_d, site, dis])


def fill_nan(df):
    """Документация для функции fill_nan

    Используется для заполнения отстутствующих фрагментов данных. Для заполнения
    берется усредненное значение.
 
    Входные данные - объект, содержащий фрагменты данных
    Выходные данные - объект, в котором заполнены пропуски
    """
    median_by_subcat = df.groupby('subcategory').median()
    for sbct in set(df['subcategory']):
        df.loc[(df['subcategory'] == sbct) & (df['price'].isna()), 'price'] = median_by_subcat.loc[sbct]['price']
    return df


def del_out_lognorm(df):
    """Документация для функции del_out_lognorm

    Используется для логарифмирования исходных данных
 
    Входные данные - объект, содержащий данные, предназначенные для логарифмирования
    Выходные данные - объект, содержащий преобразованные данные
    """
    df = df[df['price'] < 10**7]
    df['price'] = np.log1p(df['price'])
    return df


def get_hour(df):
    """Документация для функции get_hour

    Используется для получения часа из даты
 
    Входные данные - объект, содержащий информацию о дате
    Выходные данные - объект datetime, содержащий информацию только о часах
    """
    df['datetime_submitted'] = pd.to_datetime(df['datetime_submitted'], yearfirst=True)
    df['hour'] = [d.hour for d in df['datetime_submitted']]
    return df.drop('datetime_submitted', axis=1)


def make_logistic(df):
    df['is_bad'] = df['is_bad'].map({1: 1, 0: -1})
    return df


def to_vw_format(text, subcat, cat, price, region, city, hour, label=None):
    text = text.lower()
    table = str.maketrans({key: ' ' for key in string.punctuation + '\n'})

    text = text.translate(table)
    text = re.sub(CONTACT, ' контакт ', text, 0)

    subcat = subcat.replace(' ', '')
    cat = cat.replace(' ', '')
    region = region.replace(' ', '')
    city = city.replace(' ', '')
    return str(label or '') + ' |t ' + text + ' |price:' + str(price) + ' |s ' + subcat \
                            + ' |c ' + cat + ' |r ' + region + ' |ct ' + city + ' |h ' + str(hour) + '\n'


def find_start_end(text):
    m = re.search(CONTACT, text)
    if m:
        return m.start(), m.end()
    else:
        return None, None
        
if __name__ == '__main__':
    train = pd.read_csv('../tmp/data/train.csv')
    val = pd.read_csv('../tmp/data/val.csv')
    
    train = get_hour(train)
    train = fill_nan(train)
    train = del_out_lognorm(train)
    train = make_logistic(train)
    val = get_hour(val)
    val = fill_nan(val)
    val = del_out_lognorm(val)
    val = make_logistic(val)
    
    val, test = train_test_split(val, test_size=0.5, random_state = 42)
    
    with open('../tmp/prepared_vw/train.txt', 'w', encoding='utf-8') as f:
        for text, subcat, cat, price, region, city, hour, target in zip(train['description'], train['subcategory'],
                                                                        train['category'], train['price'], train['region'],
                                                                        train['city'], train['hour'], train['is_bad']):
            f.write(to_vw_format(text, subcat, cat, price, region, city, hour, target))

    with open('../tmp/prepared_vw/test.txt', 'w', encoding='utf-8') as f:
        for text, subcat, cat, price, region, city, hour, target in zip(test['description'], test['subcategory'],
                                                                        test['category'], test['price'], test['region'],
                                                                        test['city'], test['hour'], test['is_bad']):
            f.write(to_vw_format(text, subcat, cat, price, region, city, hour, target))

    with open('../tmp/prepared_vw/val.txt', 'w', encoding='utf-8') as f:
        for text, subcat, cat, price, region, city, hour, target in zip(val['description'], val['subcategory'],
                                                                        val['category'], val['price'], val['region'],
                                                                        val['city'], val['hour'], val['is_bad']):
            f.write(to_vw_format(text, subcat, cat, price, region, city, hour, target))
