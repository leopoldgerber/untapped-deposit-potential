'''
This module provides methods for preprocessing data
'''
import numpy as np


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


if __name__ == '__main__':
    print(CreateRange().get_range(0, 500, 100, 220))
    print(CreateRange().get_last_range(0, 500, 100, 220))

# # Group Functions
# class preprocessing_dataframe:
#     def agg(df, main_column, agg_column
#         # Choose agg functions: If True then agg_column. If str type then choosen column. Else False.
#         , agg_count = True , agg_sum = True , agg_mean = True , agg_unique = True):

#         main_column = [[i for i in set(main_column)] if type(main_column) == list else [main_column]][0]

#         # Get list of main & agg columns
#         column_list = [[main_column] + [i for i in set(agg_column)]
#                        if type(agg_column) == list else [main_column + [agg_column]][0]][0]

#         # Get columns for agg functions
#         agg_columns = [column for column in [agg_count, agg_sum, agg_mean, agg_unique] if type(column) == str]

#         # Drop duplicates
#         agg_columns = list(dict.fromkeys(agg_columns))

#         column_list = (column_list + agg_columns)
#         column_list = list(dict.fromkeys(column_list))

#         temp_df = df.sort_values(agg_column, ascending = False)[column_list]

#         temp_list = []

#         if agg_count != False:
#             choosen_column = [agg_count if type(agg_count) == str else agg_column][0]
#             data_count = pd.DataFrame(temp_df.groupby(main_column)[choosen_column].count()
#                                      ).rename(columns = {choosen_column:'count'})
#             temp_list.append(data_count['count'])

#         if agg_sum != False:
#             choosen_column = [agg_sum if type(agg_sum) == str else agg_column][0]
#             data_sum = pd.DataFrame(temp_df.groupby(main_column)[choosen_column].sum()
#                                    ).rename(columns = {choosen_column:'sum'})
#             temp_list.append(data_sum['sum'])

#         if agg_mean != False:
#             choosen_column = [agg_mean if type(agg_mean) == str else agg_column][0]
#             data_mean = pd.DataFrame(temp_df.groupby(main_column)[choosen_column].mean()
#                                     ).rename(columns = {choosen_column:'mean'})
#             temp_list.append(data_mean['mean'])

#         if agg_unique != False:
#             choosen_column = [agg_unique if type(agg_unique) == str else agg_column][0]
#             data_unique = pd.DataFrame(temp_df.groupby(main_column)[choosen_column].nunique()
#                                       ).rename(columns = {choosen_column:'unique'})
#             temp_list.append(data_unique['unique'])

#         return pd.concat(temp_list, axis = 1, ignore_index = False).reset_index()