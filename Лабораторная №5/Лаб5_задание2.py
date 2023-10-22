#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)


#df = pd.read_csv('dataset.csv')
df = df.head(1000)
df.isnull().sum()

df.hist()
plt.show()

df.boxplot(log=True)
plt.show()
value = 0
df.fillna(value, inplace=True)
lower_bound = 0
upper_bound = 1000
df = df[(df['feature'] >= lower_bound) & (df['feature'] <= upper_bound)]

df['room_count'] = df['room_feature']
room_counts = df['room_count'].value_counts()

pivot_table = pd.pivot_table(df, index='district',columns='room_count', values='count', aggfunc='count')
df.to_csv('surname.csv', index=False)