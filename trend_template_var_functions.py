import datetime
import pandas as pd

def return_filename():
    """
    Return filename of today
    :return: string
    """

    date_time = datetime.datetime.now().strftime("%Y%m%d")
    filename = './assets/Trend_Template/' + date_time + '_Full_TT' + '.csv'
    print(filename)
    return filename

def return_and_save_proportion(proportion):
    """
    Return filename of today
    :return: string
    """
    filename = './assets/' + 'Proportion_overtime' + '.csv'
    print(filename)
    original = pd.read_csv(filename, index_col=0)

    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    if original.index[-1] != today_date:
        df = proportion.T
        df.index = [datetime.datetime.today().date()]
        df.columns.name = 'Date'
        combined = pd.concat([original, df], axis=0)
        combined.to_csv(filename)

        return combined
    return original





