"""
Created on 3/14/22

@author: qinyuzhu
"""

import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from csv import reader
from csv import writer
import matplotlib.ticker as ticker

Nplot = pd.read_csv("temp_skl_ALLFOUR_comp.csv")
sns.set(style="whitegrid")
# sns.set_theme()
here = sns.relplot(data=Nplot, x="YM", y="comp_sentiment", hue="model", kind="line")
here.set_xticklabels(rotation = 30)
# plt.xaxis.set_major_locator(ticker.LinearLocator(10))
# for ind, label in enumerate(plt.xticklabels()):
#     if ind % 10 == 0:  # every 10th label is kept
#         label.set_visible(True)
#     else:
#         label.set_visible(False)
plt.show()





if __name__ == '__main__':
    pass
