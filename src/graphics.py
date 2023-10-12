import sys

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/BIRTHS_MOON_PHASE.csv")
df['DT_DATE'] = pd.to_datetime(df['DT_DATE'])

sns.countplot(data=df,
              x='moon_phase',
              order=df['moon_phase'].value_counts().index)
plt.title('Nombre de naissances par phase de la lune')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Phase de la lune')
plt.ylabel('Nombre de naissances')
plt.tight_layout()
plt.show()

# sns.lineplot(data=df, x='DT_DATE', y='MS_NUM_BIRTHS')
# plt.title('Naissances en fonction du temps avec phases de la lune')
# plt.xticks(rotation=45)
# plt.show()


sns.barplot(data=df, x='moon_phase', y='MS_NUM_BIRTHS')
plt.title('Moyenne de naissances par phase de la lune')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Phase de la lune')
plt.ylabel('Moyenne du nombre de naissances')
plt.tight_layout()
plt.show()

sns.boxplot(data=df, x='moon_phase', y='MS_NUM_BIRTHS')
plt.title('Box-plot des naissances par phase de la lune')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#p_value = 0.9919
#threshold = 0.05
#sns.barplot(x=['p-value', 'Seuil'], y=[p_value, threshold],
#            palette=['red', 'green'])
#plt.title('Comparaison de la valeur p au seuil')
#plt.tight_layout()
#plt.show()
