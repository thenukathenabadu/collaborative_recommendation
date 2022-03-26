#!/usr/bin/env python
# coding: utf-8

# In[49]:


from load_data_set import Load_data
# from scipy.sparse import csr_matrix
# import numpy as np
# from sklearn.neighbors import NearestNeighbors
from  sklearn.neighbors import KNeighborsClassifier 
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
pd.options.mode.chained_assignment = None
class Knn_m2(Load_data):
    def __init__(self,n_neighbors=3,threshold=10,test_size=0.33):
#         self.urls = None
#         self.metric = metric
        self.recomendations = {}
        self.lb_en = LabelEncoder()
        self.n_neighbors = n_neighbors
        self.test_size = test_size
        self.threshold = threshold
    def set_values(self,urls,dataset,threshold=10):
        self.set_urls(urls)
        self.main_df = self.get_user_preferences_df()
        self.target_df = dataset
        self.threshold = threshold
    def preprocess(self):
        self.filterd_main = self.main_df[self.main_df['userID'].isin(self.target_df['userID'].to_list())]
        self.filterd_main['enc_title'] = self.lb_en.fit_transform(self.filterd_main['bookTitle'])
        self.filterd_main['enc_isbn'] = self.lb_en.fit_transform(self.filterd_main['ISBN'])
        X = self.filterd_main.drop(['bookTitle','enc_title','ISBN','bookAuthor'],axis=1)
        Y = self.filterd_main['enc_title']
        self.train_x,self.test_x,self.train_y,self.test_y = train_test_split(X,Y,test_size=self.test_size)
        scaler = StandardScaler()
        self.X_train = scaler.fit_transform(self.train_x)
        self.X_test = scaler.fit_transform(self.test_x)
    def knn_algo(self):
        knn = KNeighborsClassifier(n_neighbors=self.n_neighbors)
        knn_model = knn.fit(self.X_train, self.train_y)#trains the classification model
        predict_knn = knn_model.predict(self.X_test)#predicts the quality of wine using  classification model
#         print(self.threshold)
        self.pred_list = predict_knn[:self.threshold]
#         print(self.pred_list)
    def print_(self):
        for i in self.filterd_main.index:
            title_en = self.filterd_main.loc[i]['enc_title']
            if title_en in self.pred_list:
                title = self.filterd_main.loc[i]['bookTitle']
                isbn = self.filterd_main.loc[i]['ISBN']
#                 print(isbn)
                self.recomendations[isbn] = title
        temp_sim_df = pd.DataFrame.from_dict(self.recomendations, orient='index')
        temp_sim_df.columns = ['Book-Title']
#         temp_sim_df['userID'] = temp_sim_df.index
        return temp_sim_df


# In[ ]:





# In[50]:


# urls = ['Books.csv','Users.csv','Book-Ratings.csv']

# import test as t
# new_t = t.Test()
# df = new_t.test_case()


# In[51]:


# urls = ['Books.csv','Users.csv','Book-Ratings.csv']
# import test as t
# new_t = t.Test()
# df = new_t.test_case()
# k = Knn_m2()
# k.set_values(urls,df)
# k.preprocess()
# k.knn_algo()
# k.print_()


# In[48]:


# k.print_()


# In[ ]:





# In[ ]:




