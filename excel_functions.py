# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:04:24 2024

@author: jzapata
"""

#%% Vlookup - 1

import os
import glob
import pandas as pd
import numpy as np

os.chdir("C:\\Users\\jzapata\\Documents\\python_automation")

sales = pd.read_excel("sales_data.xlsx")

zip_income = pd.read_csv("zipcode_income.csv", encoding = "latin-1")

temp = sales.merge(zip_income.loc[:,["Zip_Code", "Mean"]].rename(columns = {"Zip_Code": "Postal Code", "Mean": "Mean Income"})
                   , how="left", on="Postal Code")

temp.drop_duplicates(subset=["Row ID"], inplace = True)

temp.isna().sum()

#%% Vlookup - II

def vlookup(left_df, right_df, left_key, right_key, right_val):
    left = pd.read_excel(left_df)
    left.reset_index(inplace = True)
    right = pd.read_csv(right_df, encoding = "latin-1")
    right = right.loc[:, [right_key, right_val]].rename(columns = {right_key: left_key})
    temp = left.merge(right, how = "left", on = left_key)
    temp.drop_duplicates(subset=["index"], keep = "first", inplace = True)
    return temp.set_index("index")

vlookup("sales_data.xlsx", "zipcode_income.csv", "Postal Code", "Zip_Code", "Mean")

#%% Pivot Table - II

os.chdir("C:\\Users\\jzapata\\Documents\\python_automation")

cwd = os.getcwd()

sales = pd.read_excel('sales_data.xlsx')

filenames = glob.glob(cwd + "\\*\\*.xlsx")

#consolidated = pd.DataFrame(columns = pd.read_excel(filenames[0]).columns)
#for file in filenames:
#    temp = pd.read_excel(file)
#    consolidated = pd.concat([consolidated, temp], ignore_index = True)
    
columns = ["Region"]
rows = ["Segment", "Category", "Sub-Category"]
values = ["Profit"]

relevant_df = sales.loc[:,columns + rows + values]

pivot_df = relevant_df.groupby(rows+columns).sum().unstack()

pivot_df.to_excel("pivot.xlsx")

#%% Pivot Table - III

sales = pd.read_excel('sales_data.xlsx')

pd.pivot_table(sales,
    values = "Profit",
    index = ["Segment", "Category", "Sub-Category"],
    columns = ["Region", "State"],
    aggfunc = np.sum)
    
#%% IF Function - II

sales = pd.read_excel('sales_data.xlsx')

conditions = [
    sales["Category"] == "Furniture",
    sales["Category"] == "Office Supplies",
    sales["Category"] == "Technology"
]

choices = [
    0.8 * sales["Profit"],
    0.7 * sales["Profit"],
    0.8 * sales["Profit"]
]

sales["Profit Net Tax"] = np.select(conditions, choices, default=0)

#%% String Manipulation in Python

sales = pd.read_excel('sales_data.xlsx')

sales["Order ID"].str[3:7] #mid function
sales["Order ID"].str[:2] #left function
sales["Order ID"].str[:-2] #right function

sales["Order ID"].str.split("-").str[1]

sales["Order ID"].str.strip() #trim function

sales["State"] + "_" + sales["City"] #Concatenate

sales["State"].str.upper() #Capitalize
sales["State"].str.lower()

sales["City"].str.find("Fort") #Find a string

#%% Assignment SUMIF and COUNTIF

sales = pd.read_excel('sales_data.xlsx')

sales[sales["Quantity"] > 5].shape[0] #COUNTIF

sales[(sales["State"] == "Kentucky") & (sales["Quantity"] > 5)].shape[0] #COUNTIFS

sales[sales["City"].str[:4] == "Fort"]["Profit"].sum() #SUMIF

sales[(sales["City"].str[:4] == "Fort") & (sales["Quantity"] > 5)]["Profit"].sum() #SUMIFS



