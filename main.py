'''Main script from notebooks'''
import pandas as pd
from notebooks.packages import preprocessing

FILE_PATH = 'data/withdrawal_payment.csv'

df = preprocessing.prepare_dataframe(FILE_PATH)
df['close_time'] = pd.to_datetime(
    preprocessing.reverse_date(df['close_time']))

DROP_NAMES = ['LD Rebate', 'Partner Rebate', 'Unknown']
df = preprocessing.drop_names(df, 'name', DROP_NAMES)
# --- Export
FILE_PATH = preprocessing.get_output()
FILE_PATH = preprocessing.df_to_xlsx(df, 'df_cutted', FILE_PATH)
print(FILE_PATH)

# Load ranger dict and apply range with chosen col for df given
RANGER_DICT = preprocessing.get_config('ranger.json')
ranger = preprocessing.CreateRange()
df_ranged = df.copy()
ranger.apply_range(df_ranged, 'usd', RANGER_DICT)
# --- Export
FILE_PATH = preprocessing.get_output()
FILE_PATH = preprocessing.df_to_xlsx(df_ranged, 'df_ranged', FILE_PATH)


RANGER_DICT = preprocessing.get_config('ranger.json')['small']
START, END, STEP = [x for x in RANGER_DICT.values()]

# Create accumalitive columns in range
RANGER_DICT = preprocessing.get_config('ranger.json')['small']
ranger_uwp = preprocessing.CreateUWP()
df_acc = df.copy()
usd_list = ranger_uwp.range_columns(df_acc, 'usd', START, END, STEP, 'usd')
ranger_uwp.range_columns_modify(df_acc, 'usd', usd_list)
# --- Export
FILE_PATH = preprocessing.get_output()
FILE_PATH = preprocessing.df_to_xlsx(df_acc, 'df_acc', FILE_PATH)
