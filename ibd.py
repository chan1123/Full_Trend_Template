import pandas as pd
from IBD_functions import read_ibd, convert_datatypes_ibd
from IBD_functions import latest_file

df_ibd = convert_datatypes_ibd(read_ibd(latest_file()))



