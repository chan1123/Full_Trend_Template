import pandas as pd
import glob
import re
from IBD_variables import abcde_map, abcde_plus_map
from IBD_variables import abcde_plus_list, abcde_list, numeric_list


def read_ibd(filename):
    """
    Cleaning the IBD datatables
    :param filename:
    :return: df
    """

    df = pd.read_excel(filename, index_col=0)

    first_row_index = df.index.get_loc('Symbol')
    last_row_index = df.index.get_loc(df.last_valid_index()) + 1
    df = df.iloc[first_row_index:last_row_index]

    df.columns = df.iloc[0]
    df = df.iloc[1:]
    return df


def convert_datatypes_ibd(df):
    """
    Convert the letter rankings to numbers
    Covert numeric values
    Convert IPO dates to datetime
    :param df:
    :return: df
    """
    df[numeric_list] = df[numeric_list].apply(pd.to_numeric, errors='coerce')

    for item in abcde_list:
        df[item] = df[item].map(abcde_map)

    for item in abcde_plus_list:
        df[item] = df[item].map(abcde_plus_map)

    df['IPO Date'] = pd.to_datetime(df['IPO Date'])

    return df


def latest_file():
    """
    find latest file from the IBD_Excel directory
    :return: filename
    """

    file_list = glob.glob("IBD_Excel/*.xlsx")
    combined_str = ''.join(file_list)

    file_date = re.findall(r'\/(.*?)\_', combined_str)
    filename = 'IBD_Excel/' + max(file_date) + '_IBD.xlsx'
    
    print(filename)
    
    return filename
