from pathlib import Path
import pandas
import numpy 
import pandas as pd


data_dir_raw = Path('../data')
data_sample = pd.read_csv(data_dir_raw/'DISB34.SA.csv')

