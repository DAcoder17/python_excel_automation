# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:11:18 2024

@author: User
"""

#%% Series

import numpy as np
import pandas as pd

np_array = np.array([2,6,1,3])

pd_series = pd.Series(np_array) #Series are arrays with indexes

pd_series = pd.Series(np_array, index = ["a", "b", "c", "d"])

pd_series2 = pd.Series({"a":2, "b":6, "c":1, "d":3})

pd_series["b"]
pd_series[["b", "d"]]

pd_series2[2:]

#%% Dataframes

df = pd.DataFrame(np.array([[1,2,3],
                            [4,5,6],
                            [7,8,9]]), 
                  columns= ["alpha","beta","kappa"])

df.columns = ["a", "b", "c"]

df_dict = pd.DataFrame({"a":[1,2,3],
                         "b":[4,5,6],
                         "c":[7,8,9]})

type(df["a"])

df_dict[["a", "c"]]

df_dict.index = ["m", "n", "o"]

df_dict.loc["m"]

df_dict.iloc[1]

df_dict.loc["n":,"b":]

df_dict.loc[["n","o"],["a","c"]]

#%% Importing/Exporting Data

data = pd.read_excel("data.xlsx", sheet_name="Orders", header=3, index_col="Row ID")

data.head(10)
data.tail()
data.dtypes
data.describe()
data.columns
data.drop("Product Name", axis=1)
data.drop(["Product Name", "Ship Date"], axis=1)

data["Per Unit Sale"] = data["Sales"]/data["Quantity"]

data.to_excel("data_2.xlsx")

#%% Handling Python/Dataframe Data Types

data = pd.read_excel("data.xlsx", sheet_name="Orders", header=3, index_col="Row ID")

data.columns

data["Postal Code"] = data["Postal Code"].astype(str)

data["Order Date"] = pd.to_datetime(data["Order Date"], errors = "raise", format = "%Y-%m-%d")

data["month"] = data["Order Date"].dt.month
data["year"] = data["Order Date"].dt.year
data["Processing Time"] = data["Ship Date"] - data["Order Date"]

data["string date"] = data["Order Date"].dt.strftime("%b-%Y")

#%% Handling NaN Values

data = pd.read_excel("data_2.xlsx", index_col="Row ID")

data.isna().sum()

data[data.isna().sum(axis=1)>0]

data.dropna(axis=1)
data.fillna()

#%% Combining Dataframes

menu = pd.DataFrame({"item":["pizza","pasta","salad","burritto","taco","burger"],
                    "price":[14.99,12.99,7.99,10.99,6.99,5.99],
                    "popularity":["high","medium","low","high","medium","high"]})

nutrition = pd.DataFrame({"item":["pizza","pastry","burritto","salad","pasta"],
                         "avg_calorie":[3200,800,940,240,740],
                         "protein":["12%","4%","16%","6%","10%"]})

pd.concat([menu, nutrition], axis=1)

menu.merge(nutrition) #Important to have a common column to perform the merge or specificy left and right keys
menu.merge(nutrition, how = "outer")
menu.merge(nutrition, how = "left")
menu.merge(nutrition, how = "right")

menu.set_index("item", inplace=True)
menu.reset_index(inplace=True)
menu.set_index("item").join(nutrition.set_index("item"))

#%% Data Aggregation/Summarization using Groupby
 
data = pd.read_excel("data.xlsx", sheet_name="Orders", header=3, index_col="Row ID")
data.columns
#data["Postal Code"] = data["Postal Code"].astype(str) #Postal Code should be integer
numeric_columns = data.select_dtypes(include=["number"]) #Group by sum only allows numeric columns
numeric_columns["Region"] = data["Region"] #Adding the column which we want the aggregation to be performed
numeric_columns["Category"] = data["Category"]
numeric_columns.groupby("Region").sum() #Pivot table with 1 index
numeric_columns.groupby(["Region", "Category"]).sum() #Pivot table with 2 indexes
numeric_columns.groupby(["Region", "Category"]).sum().unstack()
 
gp = data.groupby("Region")
gp.groups
gp.get_group("South") # Like applying an excel filter

#%% Numpy Assignment
 
#1. Total cost of transportation
#2. Highest cost day
 
# My solution
 
sales = pd.read_excel("commute.xlsx", sheet_name="Sales")
price = pd.read_excel("commute.xlsx", sheet_name="Price", header=None)
 
sales_np = np.array(sales)
price_np = np.array(price) 
 
sales_np[:,1] = np.where(sales_np[:,1] == "Yes", 1, 0)
sales_np[:,4] = np.where(sales_np[:,4] == "Yes", 1, 0)
total_per_day = sales_np[:,1] * 8 + sales_np[:,2] * 3 + sales_np[:,3] * 0.5 + sales_np[:,4] * 12
 
sales_np = np.column_stack((sales_np, total_per_day))
 
total_cost = np.sum(sales_np[:,5])
 
day = sales_np[:,5].argmax()
 
highest_cost_day = sales_np[day,0].strftime("%Y-%m-%d")
 
# Instructor's solution

#reading excel data from sheet 
commute = pd.read_excel("commute.xlsx", sheet_name = "Sales", index_col="Date")

commute.replace(["Yes","No"],[1,0],inplace=True) #replace Yes and No with 1 and 0

x = np.array(commute) #trasnform daily commute data into 2d array

y = np.array([8,3,0.5,12]) #store pricing information in a 1d array

daily_expenses = x.dot(y) #calculating dot product

daily_expenses.sum() #calculating sum of the product

daily_expenses.argmax() #identifying index with maximum value

commute.index[daily_expenses.argmax()].strftime("%Y-%m-%d") #using max index to identify the relavant date

#%% Pandas Assignment

#Split dataset by the combination year/month

sales = pd.read_excel("sales_data.xlsx", index_col="Row ID")
sales["Postal Code"] = sales["Postal Code"].astype(str)
numeric_sales = sales.select_dtypes(include=["number"])
numeric_sales["Order Date"] = sales["Order Date"]
numeric_sales["Year"] = numeric_sales["Order Date"].dt.year
numeric_sales["Month"] = numeric_sales["Order Date"].dt.month
numeric_sales.drop("Order Date", axis =1, inplace = True)
gb = numeric_sales.groupby(["Year", "Month"])

ls = []
for df in gb.groups:
    ls.append(gb.get_group(df))
    
for df in ls:
    file_name = df["Year"].astype(str).iloc[0] + "_" + df["Month"].astype(str).iloc[0]
    df.to_excel("{}.xlsx".format(file_name), index=False)