# Welcome to my VERY brief tutoring for scikit

import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.ion()

# Here, we generate simulated data, and perform PCA and K-means clustering.

# First, generate a simulated data set with 25 observations in each of three classes (i.e. 75 observations total), and 45 variables.

# n observations and p variables
n=25
p=45

#Class 1
X1 = (np.random.uniform(0,1.5,n*p)).reshape(n,p)
Y1 = np.ones((1,n))

#Class 2
X2 = (np.random.uniform(0.2,2.1,n*p)).reshape(n,p)
Y2 = 2*np.ones((1,n))

#Class 3
X3 = (np.random.uniform(1,3.1,n*p)).reshape(n,p)
Y3 = 3*np.ones((1,n))

#Bind data
Xdata = np.concatenate((X1,X2,X3))
Ydata = np.concatenate((Y1,Y2,Y3)).flatten()

#PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(Xdata)

#plt.scatter(principalComponents[:,0],principalComponents[:,1],c=Ydata)




#(b) K-means clustering

model = KMeans(n_clusters=3)
model.fit(Xdata)
print(model.labels_)


# View the results. Set the size of the plot
plt.figure(figsize=(14,7))
 
# Create a colormap
colormap = np.array(['red', 'lime', 'black','blue'])
 
# Plot the Original Classifications
plt.subplot(1, 3, 1)
plt.scatter(principalComponents[:,0],principalComponents[:,1], c=Ydata, s=40)
plt.title('Real Classification')
 
# Plot the Models Classifications
plt.subplot(1, 3, 2)
plt.scatter(principalComponents[:,0],principalComponents[:,1], c=colormap[model.labels_], s=40)
plt.title('K-Mean Classification, K=3')

# Recalculate K-means clustering with K=4
newModel = KMeans(n_clusters=4)
newModel.fit(Xdata)
plt.subplot(1, 3, 3)
plt.scatter(principalComponents[:,0],principalComponents[:,1],
c=colormap[newModel.labels_], s=40)
plt.title('K-Mean Classification, K=4')