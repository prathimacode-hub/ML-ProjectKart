from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import *
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing

#FOR HISOTGRAMS
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'g', edgecolor = 'g')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 2.0, w_pad = 3.0, h_pad = 1.0)
    plt.show()


nRowsRead = 1000
# Adult mortality.csv may have more rows in reality, but we are only loading/previewing the first 1000 rows
df1 = pd.read_csv('/content/Adult mortality.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'Adult mortality.csv'
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')


# LOAD THE ADULT MORTALITY DATASET
df1.shape

df1.info


df1.describe()

df1 = df1.iloc[1:, :]
df1.head(20)

# CREATE PLOT
plotPerColumnDistribution(df1, 15, 9)

# SIMILARLY VISUALIZATIONS CAN BE CREATED FOR THE REMAINING DATASETS
