#importing pandas as pd
import pandas as pd;
import csv, json, sys;

# Read and store content
# of an excel file
read_file = pd.read_excel ("gis_iit_matrix.xlsx")

# Write the dataframe object
# into csv file
read_file.to_csv ("in.csv",index = None, header=True, quoting=csv.QUOTE_NONNUMERIC)
	
# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv("in.csv"))

# show the dataframe
df

