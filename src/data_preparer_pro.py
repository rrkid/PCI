import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import string_parser_pro

df_train = pd.read_csv('../tmp/data/train.csv')
df_val = pd.read_csv('../tmp/data/val.csv')

df_val.description = df_val.description.apply(string_parser.prepareString)
df_train.description = df_train.description.apply(string_parser.prepareString)

df_val.to_csv('../tmp/prepared_data/prepared_val.csv', index = False)
df_train.to_csv('../tmp/prepared_data/prepared_train.csv', index = False)
