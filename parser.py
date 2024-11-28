# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:22:33 2024

@author: n.nteits
"""

##Import Data
import pandas as pd
dfc = pd.read_csv( r'C:\Users\Γιώργος Μπόζιακας\Projects\Data_management\First\Data\Characters.csv',sep=';')
dfe = pd.read_csv( r'C:\Users\Γιώργος Μπόζιακας\Projects\Data_management\First\Data\episodes.csv',sep=';')
dfk = pd.read_csv( r'C:\Users\Γιώργος Μπόζιακας\Projects\Data_management\First\Data\keyValues.csv',sep=';')
dfl = pd.read_csv( r'C:\Users\Γιώργος Μπόζιακας\Projects\Data_management\First\Data\locations.csv',sep=';')

##Replace quote with doublequote to parse
dfc.replace("'", "''",regex=True,inplace=True)
dfe.replace("'", "''",regex=True,inplace=True)
dfk.replace("'", "''",regex=True,inplace=True)
dfl.replace("'", "''",regex=True,inplace=True)
##Name Dataframes
dfc.name='Characters'
dfe.name='Episodes'
dfk.name='Keyvalues'
dfl.name='Locations'




def create_insert(dfc,queries,x):
    ##Create a string with column names
    columns = ", ".join(['iid']+list(dfc.columns)) 
    
        
    for index, row in dfc.iterrows():
            # Create a string with row values
            values = ", ".join(f"'{value}'" for value in row)
            # Create an INSERT statement for each row
            sql = f"INSERT INTO ({dfc.name}) ({columns}) VALUES ({x},{values});\n"
            ##Append to query list
            queries.append(sql)
            ## add to counter
            x+=1
        
    return queries,x

##Initialize a list of queries
queries=[]
##Initialize id
x=1
##Pass dataframes to populate query list
queries,x=create_insert(dfc,queries,x)
queries,x=create_insert(dfe,queries,x)
queries,x=create_insert(dfk,queries,x)
queries,x=create_insert(dfl,queries,x)



##Write list to sql file with linechange as sep
with open("dynamic-queries-with-extra.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(queries))

print("SQL queries generated and saved to dynamic-queries-with-extra.sql.")

