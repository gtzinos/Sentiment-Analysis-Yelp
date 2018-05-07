import seaborn as sns

def seaborn(data):
    g = sns.FacetGrid(data=data, col='stars')
    g.map(plt.hist, 'text length', bins=50)
