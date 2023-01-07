#!/usr/bin/env python
# coding: utf-8

# In[3]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
from scipy.stats import skewtest
from sklearn import metrics

warnings.filterwarnings("ignore")

def romanToInt(i):   
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    j = 0
    num = 0
    while j < len(i):
        if j+1<len(i) and i[j:j+2] in roman:
            num+=roman[i[j:j+2]]
            j+=2
        else:

            num+=roman[i[j]]
            j+=1
    return num

def skew_df(df):
    skewness, p_value = skewtest(df)
    dskew=pd.DataFrame(np.round(np.vstack((skewness.T,p_value.T)),2),columns=df.columns,
                    index=['skewness', 'p_value'])
    return(dskew)

def plot_roc_curve(fpr,tpr):
    plt.plot(fpr,tpr)
    plt.plot([0,1],[0,1],'r')
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC - TPR vs FPR')
    
def printCustomMetrics(y_test, y_pred):
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred).round(2))
    print("Precision:", metrics.precision_score(y_test, y_pred).round(2))
    print("Recall:", metrics.recall_score(y_test, y_pred).round(2))
    print("f1:", metrics.f1_score(y_test, y_pred).round(2))
