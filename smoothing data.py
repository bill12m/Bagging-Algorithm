import subprocess as sp
import pandas as pd
import numpy as np

sp.call('clear', shell = True)

raw_data = pd.read_csv('Data.csv').set_index('Instance')
data_train = raw_data.iloc[0:10,:]
data_val = raw_data.iloc[10:15,:]
del(raw_data)
