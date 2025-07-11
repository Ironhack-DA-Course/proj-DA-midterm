#
import pandas as pd
import numpy as np

def normalize(df_col):
    min_col = min(df_col)
    max_col = max(df_col)
    mmx_diff = max_col - min_col
    return [(x-min_col)/mmx_diff for x in df_col]