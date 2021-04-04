from IBD_functions import latest_file
from IBD_functions import read_ibd, convert_datatypes_ibd

df_ibd = convert_datatypes_ibd(read_ibd(latest_file()))



