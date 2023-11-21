import seaborn as sns
pulse_data = sns.load_dataset('exercise')

sns.catplot(x = 'diet', y = 'kind', data = pulse_data)

sns.heatmap(vmin = '1 min', vmax = '30 min', data = pulse_data)

#Based on the graph, elementary schoolers could be told that exercise 
#as well as dieting makes your heart rate go up. 




