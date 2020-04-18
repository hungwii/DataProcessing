# adopt PCA to reduce drug embedding vector dimension
import numpy as np
from sklearn.decomposition import PCA

# load data
data = np.loadtxt('all_drug111.t', dtype=np.float, delimiter='\t')

# change data into array
data_array = np.array(data)

# print data array shape
(row, col) = data_array.shape
print('row=', row, 'col=', col)

# adopt PCA to fit our data
pca = PCA(n_components=600).fit(data_array)

# gain dimension reduced data array
reduce_data_array = pca.fit_transform(data_array)

# save dimension reduced data
np.savetxt('all_drug_600.txt', reduce_data_array, delimiter='\t', fmt='%.6f')


# print('reduce_data_array.shape=',reduce_data_array.shape)
