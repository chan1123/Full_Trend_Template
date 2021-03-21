import pandas as pd
import os
from overview_trial import df_overview
from IBD import df_ibd
from scraping import df_tt
from trend_template_var_functions import return_filename

def return_TT():

# Check if the program has been run today
    filename = return_filename()
    if os.path.isfile(filename):
        return pd.read_csv(filename)

    df_rs = df_ibd[df_ibd['RS Rating'] > 70]
    # Join RS and TT to form REAL trend template list
    trend_template_list = list(set(df_rs.index.tolist()) & set(df_tt.index.tolist()))

    df_overview_groupby_sector = pd.DataFrame(df_overview.groupby('Sector').count()['Company'])
    filtered = df_overview[df_overview.index.isin(trend_template_list)]
    filtered_groupby_sector = pd.DataFrame(filtered.groupby('Sector').count()['Company'])
    df_proportion = (filtered_groupby_sector/df_overview_groupby_sector*100).sort_values(by='Company', ascending=False)

    df_conclusion = pd.concat([df_ibd, df_tt, filtered], join='inner', axis=1, )

    df_conclusion.to_csv(filename)
    print(df_conclusion)
    return df_conclusion

return_TT()