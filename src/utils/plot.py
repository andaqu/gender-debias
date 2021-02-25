import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# plot function used to visualise biases
def plotBias(mb, fb, extremes, title="Occupation Bias"):
    c = [f"{x[0]} / {x[1]}" for x in extremes]
    _mb = [mb[x[1]] for x in extremes]
    _fb = [fb[x[0]] for x in extremes]
    df = pd.DataFrame({'Words': c, 
                        'Male_Bias': _mb, 
                        'Female_Bias': _fb})


    _, ax = plt.subplots(figsize=(11.7, 8.27))

    bar_plot = sns.barplot(x='Male_Bias', y='Words', data=df, order=c, lw=0, ax=ax)

    bar_plot = sns.barplot(x='Female_Bias', y='Words', data=df, order=c, lw=0, ax=ax)

    bar_plot.set(xlabel="Female/Male Bias", ylabel="Words", title = title)