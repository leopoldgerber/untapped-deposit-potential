'''
This module provides methods for preprocessing data
'''
import numpy as np
import warnings
warnings.filterwarnings(action='ignore')


class CreateRange():
    '''
    Create categorical ranges between two numbers
    and range given
    '''
    def get_range(self, start: int, end: int, step: int, num: int):
        '''Find range num falls in within step'''
        temp_ = np.array(range(start, end+step, step))
        if float(num) > end:
            return 'x > ' + str(end)
        elif float(num) < start:
            return 'x < ' + str(start)
        else:
            return str(temp_[num > temp_][-1])\
                + ' < x <= ' + str(temp_[num <= temp_][0])

    def get_last_range(self, start: int, end: int, step: int, num: int):
        '''Find last range num falls in within step'''
        temp_ = np.array(range(start, end+step, step))
        if float(num) > end:
            return 'x > ' + str(end)
        elif float(num) < start:
            return 'x < ' + str(start)
        else:
            return str(start) + ' < x <= ' + str(temp_[num <= temp_][0])


class ColumnProcessor:
    '''
    Get column types [numeric, string]
    or change if needed
    '''
    def __init__(self, df):
        self.df = df
        columns_type_dict = {}
        self.columns_type_dict = columns_type_dict

    def get_datetime(self, col: str):
        '''Change date order inside datetime'''
        splt_date = self.df[col].apply(lambda x: str(x).split(' ')[0])
        splt_time = self.df[col].apply(lambda x: str(x).split(' ')[1])
        splt_day = splt_date.apply(lambda x: str(x).split('.')[0])
        splt_month = splt_date.apply(lambda x: str(x).split('.')[1])
        splt_year = splt_date.apply(lambda x: str(x).split('.')[2])
        splt = splt_year+'.'+splt_month+'.'+splt_day+' '+splt_time
        return splt

    def get_type(self):
        '''Get the column type'''
        for col in self.df.columns.values:
            # Column to numeric within given DataFrame
            try:
                self.df[col] = self.df[col].apply(
                    lambda x: str(x).replace(',', '.'))
                self.df[col] = pd.to_numeric(self.df[col], errors='ignore')
            except TypeError:
                print(f'Cannot convert [{col}]')

            # Add column type to dictionary
            if pd.api.types.is_string_dtype(self.df[col]):
                self.columns_type_dict[col] = 'string'
            elif pd.api.types.is_numeric_dtype(self.df[col]):
                self.columns_type_dict[col] = 'numeric'
            else:
                print(f'[{col}] - unknown type - [{self.df[col].dtype}]')
                self.columns_type_dict[col] = 'unknown'
        return self.columns_type_dict

    def get_changed_dict(self, col_list=None, col_type=None):
        '''Change type of given column in returned dictionary'''
        temp_dict = ColumnProcessor(self.df).get_type()
        if col_list is None or col_type is None:
            return self.df, temp_dict
        else:
            for col in col_list:
                temp_dict[col] = col_type
            return self.df, temp_dict


if __name__ == '__main__':
    import os
    import pandas as pd

    PATH = os.path.join(os.getcwd(), 'data/withdrawal.csv')
    df = pd.read_csv(PATH, sep=';', encoding='cp1251')

    get_column = ColumnProcessor(df)
    df['close_time'] = get_column.get_datetime('close_time')
    df['close_time'] = pd.to_datetime(df['close_time'])
    df['date_month'] = df['close_time'].dt.date
    data_dict_types = get_column.get_type()

    COLUMNS_LIST, TYPES = ['close_time', 'date_month'], 'datetime'
    df, data_dict_types = get_column.get_changed_dict(COLUMNS_LIST, TYPES)
    print(df['date_month'])

    print(CreateRange().get_range(0, 500, 100, 220))
    print(CreateRange().get_last_range(0, 500, 100, 220))
