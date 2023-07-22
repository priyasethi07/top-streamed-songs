# -*- coding: utf-8 -*-
"""music_fetch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nrDqCoIV5NqcULs0XxllU0WFLc38Clno
"""

import pandas as pd
import matplotlib.pyplot as plt
from firebase_admin import credentials, firestore, initialize_app
import time

from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("/content/data-analysis-6df39-firebase-adminsdk-gzv79-45763a684f.json")
initialize_app(cred,{'databaseURL':'https://data-analysis-6df39.firebaseio.com/'})

db = firestore.client()

db = firestore.client()

doc_ref = db.collection('training')
docs = db.collection(u'training').stream()
training =[]
for doc in docs:
  training.append(doc.to_dict())
print(training)

df = pd.DataFrame(training)
df.head()

df.dtypes

import seaborn as sns
plt.figure(figsize=(6, 4))
sns.countplot(df.energy.round(1))
plt.title("Energy Distribution")
plt.show()

sns.distplot(df["duration"],bins=50,kde=False,vertical=True)
plt.show()

sns.distplot(df["tempo"],bins=50,kde=False,vertical=False)
plt.show()

sns.countplot(df['energy'].round(1),hue=df['duration'].round(1), dodge=False)
plt.show()

sns.barplot(y=df["speechiness"], x=df['duration'].round(1))
plt.show()

sns.boxplot(y=df["liveness"], x=df['duration'].round(1), color='g')
plt.show()

sns.barplot(x=df["instrumentalness"].round(1),y=df['energy'])
plt.show()

types=df["key"].value_counts()
types.reset_index()

types=df["energy"].round(1).value_counts()
plt.pie(types.values, labels=types.index, labeldistance=1.2, shadow=True, startangle=60)
plt.title('Music',fontsize=15)
plt.plot()

plt.figure(figsize=(9,6))
fig=sns.countplot(df['liveness'].round(1), palette=['Orange'])
plt.xlabel("Liveness")
plt.ylabel("Count")
plt.title("Count Plot", fontsize=15)
plt.plot()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=2)
plt.show()

x=df['danceability']
y=df['energy']
plt.scatter(x,y)

