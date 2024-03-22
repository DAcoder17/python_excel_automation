# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:55:00 2024

@author: jzapata
"""

#%% Python OS Library

import os

os.getcwd()

cwd = os.getcwd()

os.chdir("C:\\Users\\jzapata\\Documents") #This sets up your working directory

os.mkdir("test") #Creates a new folder

os.rmdir("test") #Removes specified folder

os.system("2017_5.xlsx") #Opens a file

os.path.join(cwd, "python_automation")

#%% File Handling using Python

import shutil

os.chdir("C:\\Users\\jzapata\\Documents\\python_automation")

cwd = os.getcwd()

os.mkdir("2014")
os.mkdir("2015")
os.mkdir("2016")
os.mkdir("2017")

os.rename("2014_1.xlsx", os.path.join(cwd, "2014", "2014_1.xlsx")) #Moves a file into a folder
os.replace(os.path.join(cwd,"2014_2.xlsx"), os.path.join(cwd, "2014", "2014_2.xlsx")) #Another way to do it

os.renames("2014", "2015") #Moves one folder into another

shutil.copy("2014_3.xlsx", os.path.join(cwd, "2014", "2014_3.xlsx")) #Copies a file and pastes it into a folder

shutil.copytree("2014", "2014_copy") #Copies a folder and pastes it into another

#%% Glob Library and Handling Filenames

import glob

os.chdir("C:\\Users\\jzapata\\Documents\\python_automation")

cwd = os.getcwd()

filenames = glob.glob("*") # Gets everything from the folder
filenames = glob.glob("2014*") # Only files that start with 2014

glob.glob(cwd+"\\*\\*\\*.xlsx") #Looks for every excel file in every subfolder

#%% Assignment - Organize files

#Move the 48 files to 4 folders where you classify the information by year

#My solution

filenames_2014 = glob.glob("2014*.xlsx")
filenames_2015 = glob.glob("2015*.xlsx")
filenames_2016 = glob.glob("2016*.xlsx")
filenames_2017 = glob.glob("2017*.xlsx")

for i in filenames_2014:
    os.rename(i, os.path.join(cwd, "2014", i))
    
for i in filenames_2015:
    os.rename(i, os.path.join(cwd, "2015", i))
    
for i in filenames_2016:
    os.rename(i, os.path.join(cwd, "2016", i))
    
for i in filenames_2017:
    os.rename(i, os.path.join(cwd, "2017", i))
    
#Instructor's solution

filenames = glob.glob("*.xlsx")

for file in filenames:
    year = file.split(".")[-2][-4:]
    try:
        int(year)
    except:
        continue
    if os.path.isdir(year) == False:
        os.mkdir(year)
    
    os.rename(file,os.path.join(cwd,year,file))

#%% Assignment - Consolidate Numerous Files

#My solution

os.mkdir("Consolidate")

filenames = glob.glob(cwd+"\\*\\*.xlsx")
    
for i in filenames:
    shutil.copy(i, cwd+"\\consolidate")
    
#Instructor's solution

import pandas as pd

filenames = glob.glob(cwd+"\\*\\*.xlsx")

#Initiate the dataframe
consolidated = pd.DataFrame(columns = pd.read_excel(filenames[0]).columns) 
    
for file in filenames:
    temp = pd.read_excel(file)
    consolidated = pd.concat([consolidated, temp], ignore_index = True)
    
consolidated.to_excel("consolidated.xlsx")




