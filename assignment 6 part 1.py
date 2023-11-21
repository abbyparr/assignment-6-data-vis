import seaborn as sns
iris_data = sns.load_dataset('iris')

sns.relplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data = iris_data)
sns.relplot(x = 'petal_length', y = 'petal_width', hue = 'species', data = iris_data)

sns.scatterplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data = iris_data)
sns.scatterplot(x = 'petal_length', y = 'petal_width', hue = 'species', data = iris_data)

sns.lineplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data = iris_data)
sns.lineplot(x = 'petal_length', y = 'petal_width', hue = 'species', data = iris_data)


sns.displot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data = iris_data)
sns.displot(x = 'petal_length', y = 'petal_width', hue = 'species', data = iris_data)

sns.histplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data = iris_data)
sns.histplot(x = 'petal_length', y = 'petal_width', hue = 'species', data = iris_data)

sns.catplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data = iris_data)
sns.catplot(x = 'petal_length', y = 'petal_width', hue = 'species', data = iris_data)

sns.stripplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data = iris_data)
sns.stripplot(x = 'petal_length', y = 'petal_width', hue = 'species', data = iris_data)

sns.boxplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data = iris_data)
sns.boxplot(x = 'petal_length', y = 'petal_width', hue = 'species', data = iris_data)

#The most related species based on the graphs are virginica and versicolor. 
#Both species have similar sepal lengths and widths, as well as petal lengths and widths. 