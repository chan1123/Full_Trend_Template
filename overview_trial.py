import os
import time
import random

import pandas as pd

from overview_var_functions import base_url, parameters, position
from overview_var_functions import return_filename, convert_datatypes_overview, latest_file
from overview_var_functions import return_single_table_from_finviz

def scrap_overview():

# Check if the program has been run today
    filename = return_filename()
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col='Ticker')

# Check amount of stocks and determine the pages required to click through finviz
    trial = return_single_table_from_finviz(position, base_url, parameters, True)
    total = trial[1]
    results = trial[0]
    print(total)

    # total = 60
#   uncomment total for testing purposes

# Loop through finviz scrapping the entire list
    for _ in list(range(21, total, 20)):
        parameters['r'] = _
        new_frame = return_single_table_from_finviz(position, base_url, parameters)
        results = results.append(new_frame)

        time.sleep(random.randint(4, 7))
        print(_, 'is done')
    filtered = convert_datatypes_overview(results)
    filtered.to_csv(filename)
    return filtered


#df_overview = scrap_overview()

df_overview = pd.read_csv(latest_file(), index_col='Ticker')





