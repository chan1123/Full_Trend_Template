# Libraries required

import datetime
import glob
import re
import numpy as np
import pandas as pd
import requests

# Variables

# Header used to trick finviz into thinking I am human
finviz_headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) \
                  AppleWebKit/537.36 (KHTML, like Gecko) Chrome',
                  'Accept-Language': 'en-gb',
                  'Accept-Encoding': 'deflate',
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9, \
                  image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'Referer': 'http://www.google.com/'}

# url for scrapping
base_url = 'https://finviz.com/screener.ashx'

# parameters
parameters = {'f': 'ind_stocksonly', 'v': 111}

# the 15th table in html
position = 14

category_list = ['Sector', 'Industry', 'Country']


######################################################################
# Functions

def return_single_table_from_finviz(position, base_url, parameters, show_stocks=False):
    """
    Submit requests to finviz and scrap only one stock table
    """
    r = requests.get(url=base_url,
                     params=parameters,
                     headers=finviz_headers)

    dfs = pd.read_html(r.text)
    finviz_headers['Referer'] = r.url

    if show_stocks:
        total = parse_total_stocks(dfs[position - 1])
        return dfs[position], total
    return dfs[position]


def parse_total_stocks(df):
    """
    Parse total stocks from df
    :param df:
    :return: int
    """

    phrase = df.iloc[0, 0]
    return int(phrase.split(' ')[1])


def return_filename():
    """
    Return filename of today
    :return: string
    """

    date_time = datetime.datetime.now().strftime("%Y%m%d")
    filename = './Finviz/' + date_time + '_total' + '.csv'
    return filename


def convert_datatypes_overview(df_input):
    """
    Return the cleaned dataframe
    """

    df = df_input.copy(deep=True)

    df.columns = df.iloc[0]
    df.drop(index=[0], inplace=True)
    df.set_index('Ticker', inplace=True)
    del df['No.']
    del df['Market Cap']
    del df['P/E']
    del df['Price']
    del df['Change']
    del df['Volume']

    return df


def latest_file():
    """
    find latest file from the Finviz directory
    :return: filename
    """

    file_list = glob.glob("Finviz/*.csv")
    combined_str = ''.join(file_list)

    file_date = re.findall(r'\/(.*?)\_', combined_str)
    filename = 'Finviz/' + max(file_date) + '_total.csv'

    print(filename)

    return filename



