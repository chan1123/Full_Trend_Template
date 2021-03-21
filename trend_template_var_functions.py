import datetime

def return_filename():
    """
    Return filename of today
    :return: string
    """

    date_time = datetime.datetime.now().strftime("%Y%m%d")
    filename = './assets/Trend_Template/' + date_time + '_Full_TT' + '.csv'
    print(filename)
    return filename

def return_proportion_filename():
    """
    Return filename of today
    :return: string
    """

    date_time = datetime.datetime.now().strftime("%Y%m%d")
    filename = './assets/' + date_time + '_proportion_over_time' + '.csv'
    print(filename)
    return filename
