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
    print('File Name:', f.split("Structure and table header data/")[-1])
      
    # print the content
    # str=df
    # print(type(str))
    print('Content:')
    # Convert all columns to text Series
    text=open(f,"r",encoding='utf-8')
    text = ' '.join([i for i in text])  
    print(text);
# replacing ',' by space
    text = text.replace(",", " ")  
    comma="),"
    Ftxt=text.replace(")",comma)
    if(Ftxt.startswith('"')==True and Ftxt.endswith('"')==True ):
        Ftxt=Ftxt[1:-1]
    
    print(Ftxt);
#displaying result
    print(Ftxt)
    print("-"*200)