# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:42:26 2024

@author: jzapata
"""

#%% Pandas visualization
 
import os
import pandas as pd
 
os.chdir("C:\\Users\\jzapata\\Documents\\python_automation")
 
sales = pd.read_excel("sales_data.xlsx")
 
sales.groupby("Region")[["Sales", "Profit"]].sum().plot()
sales.groupby("Region")[["Sales", "Profit"]].sum().plot(kind="bar")
sales.groupby("Region")[["Sales", "Profit"]].sum().plot(kind="bar",
                                                        title="Regional Sales & Profits")
sales.groupby("Region")[["Sales", "Profit"]].sum().plot(kind="bar",
                                                        title="Regional Sales & Profits",
                                                        subplots=True)
sales.groupby("Region")[["Sales", "Profit"]].sum().plot(kind="bar",
                                                        title="Regional Sales & Profits",
                                                        subplots=True,
                                                        layout=(1,2))
sales.groupby("Region")[["Sales", "Profit"]].sum().plot(kind="bar",
                                                        title="Regional Sales & Profits",
                                                        subplots=True,
                                                        layout=(1,2),
                                                        sharey=True)
sales.groupby("Region")[["Sales", "Profit"]].sum().plot(kind="bar",
                                                        title="Regional Sales & Profits",
                                                        stacked=True)
 
#%% Matplotlib OO Interface - I
 
cwd = os.getcwd()
 
import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(1, 10)
 
fig = plt.figure()
 
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.15,0.7,0.25,0.25])
 
ax1.plot(x, x**2, color = "r")
ax2.plot(x, np.log(x), ls = "--")
 
#%% Matplotlib OO Interface - II
 
import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(1, 10)
 
fig = plt.figure()
fig.suptitle("Major Title")
 
ax1 = fig.add_axes([0,0,0.45,0.9])
ax1.set_title("x squared")
ax1.set_xlabel("x values")
ax1.set_ylabel("y values")
ax2 = fig.add_axes([0.5,0,0.45,0.9])
ax2.set_title("log of x")
ax2.set_xlabel("x values")
ax2.set_yticks([0,1,2])
 
ax1.plot(x, x**2)
ax2.plot(x, np.log(x), color = "r")
 
#%% Matplotlib OO Interface - III
 
import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(1, 10)
 
plt.style.use('ggplot')
 
fig = plt.figure()
fig.suptitle("Major Title")
 
ax1 = fig.add_axes([0,0,0.45,0.9])
ax1.set_title("x raised to a power")
ax1.set_xlabel("x values")
ax1.set_ylabel("y values")
ax2 = fig.add_axes([0.5,0,0.45,0.9])
ax2.set_title("log of x")
ax2.set_xlabel("x values")
ax2.set_yticks([0,1,2])
 
ax1.plot(x, x**2, color = "blue", label = "x squared")
ax1.plot(x, x**3, color = "black", label = "x cubed")
ax2.plot(x, np.log(x), color = "r")
ax1.legend(loc = "best")
 
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows = 2, ncols = 2, sharex=True)
ax1.plot(x, x**2)
ax2.plot(x, x**3)
ax3.plot(x, 4*x)
ax4.plot(x,x**(1/2))
 
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)
ax1.plot(x, x**2)
ax2.plot(x, x**3)
ax3.plot(x, 4*x)
ax4.plot(x,x**(1/2))
 
#%% Combining Pandas Visualization with OO capabilities - I
 
import os
import pandas as pd
import matplotlib.pyplot as plt
 
sales_data = pd.read_excel("sales_data.xlsx")
 
fig = plt.figure()
fig.suptitle("City level Performance", x = 0)
ax1 = fig.add_axes([0,0,1,0.9])
ax2 = fig.add_axes([0.6,0.55,0.25,0.25])
ax1.set_title("Top Cities")
ax2.set_title("Laggard Cities")
sales_data.groupby("City")["Sales"].sum().sort_values(ascending=False).iloc[:15].plot(kind="barh", color = "green", ax = ax1)
sales_data.groupby("City")["Sales"].sum().sort_values(ascending=True).iloc[:5].plot(kind="bar", color = "r", ax = ax2)
 
#%% Combining Pandas Visualization with OO capabilities - II
 
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
 
sales_data = pd.read_excel("sales_data.xlsx")
 
fig = plt.figure()
fig.suptitle("City level Performance", x = 0)
 
def new_ticks(x, pos):
    return "${}K".format(round(x/100))
 
ax1 = fig.add_axes([0,0,1,0.9])
ax1.set_title("Top Cities")
ax1.yaxis.label.set_visible(False)
ax1.set_xlabel("Sales")
ax1.axvline(x=100000, color="black", ls = "--", linewidth = 2)
ax1.xaxis.set_major_formatter(tkr.FuncFormatter(new_ticks))
 
ax2 = fig.add_axes([0.6,0.55,0.25,0.25])
ax2.set_title("Laggard Cities")
ax2.xaxis.label.set_visible(False)
ax2.set_ylabel("Sales")
 
sales_data.groupby("City")["Sales"].sum().sort_values(ascending=False).iloc[:15].plot(kind="barh", color = "green", ax = ax1)
sales_data.groupby("City")["Sales"].sum().sort_values(ascending=True).iloc[:5].plot(kind="bar", color = "r", ax = ax2)
 
#%% Visualization Assignment 1
 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
 
explode = (0.1,0,0)
 
sales_data = pd.read_excel("sales_data.xlsx")
 
fig = plt.figure()
fig.suptitle("Sales Breakdown by Category & Segment")
 
ax1 = fig.add_axes([0,0,0.5,0.8])
ax1.set_title("Category level Sales Breakdown")
ax1.yaxis.label.set_visible(False)
 
ax2 = fig.add_axes([0.5,0,1,0.8]) 
ax2.set_title("Segment level Sales Breakdown")
ax2.yaxis.label.set_visible(False)
ax2.legend(loc = "best")
 
sales_data.groupby("Category")["Sales"].sum().sort_values(ascending=False).iloc[:3].plot(kind="pie", ax = ax1, autopct='%1.2f%%', explode = explode)
sales_data.groupby("Segment")["Sales"].sum().sort_values(ascending=False).iloc[:3].plot(kind="pie", ax = ax2, autopct='%1.2f%%', explode = explode)
 
#%%Visualization Assignment 2

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

sales_data = pd.read_excel("sales_data.xlsx")
sales_data["year"] = sales_data["Order Date"].dt.year
timeseries_data = sales_data.groupby("Order Date")[["year","Sales"]].agg({"year":"first","Sales":"sum"})
timeseries_data.sort_index(inplace=True)

def new_ticks(x,pos):
    return "${}K".format(round(x/1000))

plt.style.use("ggplot")
fig = plt.figure()
fig.suptitle("Cumulative Sales", x = 0.5, y = 1)

ax1 = fig.add_axes([0,0,1,0.9])
ax1.set_title("2017 cumuative sales")
data_2017 = timeseries_data[timeseries_data["year"]==2017]
data_2017["cumsales"] = data_2017["Sales"].cumsum()
ax1.plot(data_2017["cumsales"])
ax1.set_ylabel("Sales")
ax1.yaxis.set_major_formatter(tkr.FuncFormatter(new_ticks))

ax2 = fig.add_axes([0.2,0.55,0.25,0.25])
ax2.set_title("Yearly Sales")
x = timeseries_data.groupby("year").sum().index
height = timeseries_data.groupby("year").sum()["Sales"].to_list()
ax2.bar(x,height)
ax2.set_yticks([0,200000,400000,600000,800000])
ax2.set_xticks(x)
ax2.set_ylabel("Sales")
ax2.yaxis.set_major_formatter(tkr.FuncFormatter(new_ticks))
