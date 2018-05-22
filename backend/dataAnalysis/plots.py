import seaborn as sns
import matplotlib.pyplot as plt

def seaborn(data):
    data['text length'] = data['text'].apply(len)
    print(data['text length'])

    # g = sns.FacetGrid(data=data, col='stars')
    # g.map(plt.hist, 'text length', bins=50)

    # sns.boxplot(x='stars', y='text length', data=data)
    # stars = data.groupby('stars').mean()
    # stars.corr()
    # sns.heatmap(data=stars.corr(), annot=True)

