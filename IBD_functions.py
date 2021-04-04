import pandas as pd
import glob
import re

abcde_map = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1
}

abcde_plus_map = {
    'A+': 13, 'A': 12, 'A-': 11,
    'B+': 10, 'B': 9, 'B-': 8,
    'C+': 7, 'C': 6, 'C-': 5,
    'D+': 4, 'D': 3, 'D-': 2,
    'E': 1
}

numeric_list = [
    'Price',
    'Price $ Change',
    'Price % Change',
    'Comp. Rating',
    'EPS Rating',
    'RS Rating',
    'Vol. % Change',
    'Vol. (1000s)',
    # 'Industry Group Rank',
    # '# of Funds - last reported qrtr',
    # 'Pretax Margin',
    # 'Curr Yr EPS Est. % Chg.',
    # 'Curr Qtr EPS Est. % Chg.',
    # 'Last Qtr EPS % Chg.',
    # 'Last Qtr Sales % Chg.',
    # 'Div Yield',
    # 'PE Ratio',
    # 'Vol- 50 Day Avg. (1000s)'
]

abcde_list = [
    'SMR Rating',
    'Spon Rating'
]

abcde_plus_list = [
    'Ind Grp RS',
    'Acc/Dis Rating'
]


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

    # df['IPO Date'] = pd.to_datetime(df['IPO Date'])

    return df


def latest_file():
    """
    find latest file from the IBD_Excel directory
    :return: filename
    """

    file_list = glob.glob("assets/IBD_Excel/*.xlsx")

    combined_str = ''.join(file_list)

    file_date = re.findall(r'Excel\/(.*?)\_', combined_str)
    filename = 'assets/IBD_Excel/' + max(file_date) + '_IBD.xlsx'
    
    print(filename)
    
    return filename
