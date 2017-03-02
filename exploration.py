# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:53:19 2017

@author: Badr
"""

import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats

red = pd.read_csv('winequality-red.csv', header=0, low_memory=False, sep=';')
white = pd.read_csv('winequality-white.csv',header=0,  low_memory=False, sep=';')


def call (functionToCall):
    print('Red')
    functionToCall(red)
    
    print('\n')

    print('White')
    functionToCall(white)
    print('\n')
    

# # ------------- to print basic info ----------------
def basicInfo(wine_set):
    print(len(wine_set))
    print(len(wine_set.columns))
    print(list(wine_set.columns.values))
    print(wine_set.ix[:10,:4])
    print('\n')
    print("--------------describe the data-----------------")
    print('\n')
    print(wine_set.describe())

call(basicInfo)

# ------------ to print frequency distributions of wines' quality ------
def frequencyDists(wine_set):
    print("This is the frequency distribution of the wines' quality.")
    print(wine_set.groupby("quality").size()*100 / len(wine_set))
    print()

call(frequencyDists)

# ------------- to print quartile split of the quality variable -----------------
def quartileSplit(wine_set):
    print("This is the quartile split of the wines' quality. I-st column contains the intervals of wines' quality;")
    print("II-nd - the number of wine samples with the quality in the corresponding interval.")
    wine_set["quality_quart"] = pd.qcut(wine_set["quality"], 3)
    print(wine_set.groupby("quality_quart").size())

call(quartileSplit)

# ---------------- visualization  with countplots and factorplots----------------------------
def countplots(wine_set):
    wine_set["quality"] = pd.Categorical(wine_set["quality"])
    seaborn.countplot(x="quality", data=wine_set)
    plt.xlabel("Quality level of wine (0-10 scale)")
    plt.show()

call(countplots)


def factorplots(wine_set):
    seaborn.factorplot(x="quality", y="alcohol", data=wine_set, kind="strip")
    plt.xlabel("Quality level of wine, 0-10 scale")
    plt.ylabel("Alcohol level in wine, % ABV")
    if wine_set.equals(red):
        plt.title("Alcohol percent in each level of red wine's quality")
    else:
        plt.title("Alcohol percent in each level of white wine's quality")
    plt.show()

call(factorplots)





