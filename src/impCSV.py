# 

# import necessary libraries
import pandas as pd
import os
import glob
  
  
# use glob to get all the csv files 
# in the folder
path = r'/mnt/c/Users/Ashrith/Desktop/ToolV2/src/dev-src/dev-microservices/Order-To-Cash-Microservice/Data/Structure and table header data'
csv_files = glob.glob(os.path.join(path, "*.csv"))
  
  
# loop over the list of csv files
for f in csv_files:
      
    # read the csv file
    df = pd.read_csv(f)
      
    # print the filename
    print('File Name:', f.split("Structure and table header data")[-1])
      
    # print the content
    print('Content:')
    print(df)
    print("-"*200)