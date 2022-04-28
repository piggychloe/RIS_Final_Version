"""
Created on 4/25/22

@author: qinyuzhu
"""
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
"""
this file is used to get the barplot
input: NLTK data, BERT data, NTLK+BERT outcome
output: three barplot with % of positive sentiment on it
"""
Nplot = pd.read_csv("temp_skl_ALLFOUR_comp.csv")
sns.set(style="whitegrid")
# sns.set_theme()
here = sns.barplot(data=Nplot, x="model", y="comp_sentiment")
here.set_xticklabels(here.get_xticklabels(),rotation = 30)
plt.show()
if __name__ == '__main__':
    pass
