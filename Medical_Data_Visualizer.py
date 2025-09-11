import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Import the data

df = pd.read_csv('C:/Users/darkm/OneDrive/Desktop/PROJECTS/medical_examination.csv')

#Add an overweight column

df['overweight'] = np.where(df['weight'] / ((df['height'] * 0.01) ** 2 ) > 25,1,0)
df.head()
df

#Normalize data by making 0 always good and 1 always bad.
#If value == cholesterol || gluc == 1, set value == 0. If value > 1, then value == 1.

df['cholesterol'] = np.where(df['cholesterol'] == 1,0,1)
df['gluc'] = np.where(df['gluc'] == 1,0,1)
df

#Draw the Categorical Plot in the draw_cat_plot function
#Creation of a DataFrame for the cat plot using pd.melt
df_cat = sorted(['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
df_cat = pd.melt(df, id_vars = 'cardio', value_vars=df_cat)

#Drawing a plot graph using sns.catplot
sns.catplot(x='variable', col='cardio', hue='value', kind='count',data=df_cat).set_axis_labels('variables', 'total')

#Draw the Heat Map
#Cleaning the data from the information to provide visual insights.
df_heat  = df.loc[(df['ap_lo'] <= df['ap_hi']) &
(df['height'] >= df['height'].quantile(0.025)) & 
(df['height'] <= df['height'].quantile(0.975)) &
(df['weight'] >= df['weight'].quantile(0.025)) &
(df['weight'] <= df['weight'].quantile(0.975))]

#Calculating the correlation
corr = df_heat.corr()

#Generating a mask for the upper triangle 
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True

#Using seaborn to subplot the heatmap.
fig , ax = plt.subplots(figsize = (8,6))
ax=sns.heatmap(corr, vmin=0, vmax=0.25, annot=True, fmt='.1f', linewidths=0, square=True, mask=mask, cbar_kws={'shrink':.70})
