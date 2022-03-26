#!/usr/bin/env python
# coding: utf-8

# In[3]:


from load_data_set import Load_data
from scipy.sparse import csr_matrix
import numpy as np
from sklearn.neighbors import NearestNeighbors
class Knn(Load_data):
    def __init__(self,metric,n_neighbors):
        self.urls = None
        self.metric = metric
        self.n_neighbors = n_neighbors
    def set_values(self,urls,dataset):
        self.set_urls(urls)
        self.main_df = self.get_user_preferences_df()
        self.target_df = dataset
    def preprocess(self):
        filterd_main = self.main_df[self.main_df['userID'].isin(self.target_df['userID'].to_list())]
        reco_sample_u = filterd_main.drop_duplicates(['userID', 'bookTitle'])
        self.user_rating_pivot = reco_sample_u.pivot(index = 'bookTitle', columns = 'userID', values = 'bookRating').fillna(0)
        self.user_rating_matrix = csr_matrix(self.user_rating_pivot.values)
    def knn_algo(self):
        model_knn = NearestNeighbors(metric = self.metric, algorithm = 'brute',leaf_size=30,metric_params=None, n_jobs=1, n_neighbors=self.n_neighbors, p=2, radius=1.0)
        model_knn.fit(self.user_rating_matrix)
        self.query_index = np.random.choice(self.user_rating_pivot.shape[0])
        self.distances, self.indices = model_knn.kneighbors(self.user_rating_pivot.iloc[self.query_index, :].values.reshape(1, -1), n_neighbors = self.n_neighbors)
    def print_(self):
        for i in range(0, len(self.distances.flatten())):
            print('{0}: {1}, with distance of {2}:'.format(i+1, self.user_rating_pivot.index[self.indices.flatten()[i]], self.distances.flatten()[i]))
#             if i == 0:
#                 print('Recommendations for {0}:\n'.format(self.user_rating_pivot.index[self.query_index]))
#             else:
#                 print('{0}: {1}, with distance of {2}:'.format(i, self.user_rating_pivot.index[self.indices.flatten()[i]], self.distances.flatten()[i]))
        


# In[ ]:


# arr = ['Books.csv','Users.csv','Book-Ratings.csv']

