'''Main script from notebooks'''
import pandas as pd
from notebooks.packages import preprocessing

FILE_PATH = 'data/withdrawal_payment.csv'

df = preprocessing.prepare_dataframe(FILE_PATH)
df['close_time'] = pd.to_datetime(
    preprocessing.reverse_date(df['close_time']))

DROP_NAMES = ['LD Rebate', 'Partner Rebate', 'Unknown']
df = preprocessing.drop_names(df, 'name', DROP_NAMES)

FILE_PATH = preprocessing.get_output()
FILE_PATH = preprocessing.df_to_xlsx(df, 'df_cutted', FILE_PATH)
print(FILE_PATH)

RANGER_DICT = preprocessing.get_config('ranger.json')
ranger = preprocessing.CreateRange()
ranger.create_range(df, 'usd', RANGER_DICT)
print(df)
