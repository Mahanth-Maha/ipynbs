import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

d2 = [['Driver_ID', 'Distance_Feature', 'Speeding_Feature'],
      [3423311935, 71.24, 28],
      [3423313212, 52.53, 25],
      [3423313724, 64.54, 27],
      [3423311373, 55.69, 22],
      [3423310999, 54.58, 25],
      [3423313857, 41.91, 10],
      [3423312432, 58.64, 20],
      [3423311434, 52.02, 8],
      [3423311328, 31.25, 34],
      [3423312488, 44.31, 19],
      [3423311254, 49.35, 40],
      [3423312943, 58.07, 45],
      [3423312536, 44.22, 22],
      [3423311542, 55.73, 19],
      [3423312176, 46.63, 43],
      [3423314176, 52.97, 32],
      [3423314202, 46.25, 35],
      [3423311346, 51.55, 27],
      [3423310666, 57.05, 26],
      [3423313527, 58.45, 30],
      [3423312182, 43.42, 23],
      [3423313590, 55.68, 37],
      [3423312268, 55.15, 18]]
df2 = pd.DataFrame(d2[1:], columns=d2[0])
# df2.head()
f1 = df2['Distance_Feature'].values
f2 = df2['Speeding_Feature'].values

X = np.matrix(list(zip(f1, f2)))

plt.plot(1)
plt.subplot(511)
plt.xlim([0, 100])
plt.ylim([0, 50])
plt.title('Dataset')
plt.ylabel('speeding_feature')
plt.xlabel('distance_feature')
plt.scatter(f1, f2)


colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']

# create new plot and data for K- means algorithm
plt.plot(2)
ax = plt.subplot(513)
kmeans_model = KMeans(n_clusters=3).fit(X)

for i, l in enumerate(kmeans_model.labels_):
    plt.plot(f1[i], f2[i], color=colors[l], marker=markers[l])

plt.xlim([0, 100])
plt.ylim([0, 50])
plt.title('K- Means')
plt.ylabel('speeding_feature')
plt.xlabel('distance_feature')

# create new plot and data for gaussian mixture
plt.plot(3)
plt.subplot(515)
gmm = GaussianMixture(n_components=3).fit(X)
labels = gmm.predict(X)

for i, l in enumerate(labels):
    plt.plot(f1[i], f2[i], color=colors[l], marker=markers[l])

plt.xlim([0, 100])
plt.ylim([0, 50])
plt.title('Gaussian Mixture')
plt.ylabel('speeding_feature')
plt.xlabel('distance_feature')


plt.show()
