#!/usr/bin/env python
# coding: utf-8

# In[37]:


import similarities as sm
import pandas as pd
class RecomenderWithBooks():
    def __init__(self):
        self.sim = sm.Similarity()
        self.__simDict={}
    def set_data_frame(self,df):
        self.__data_frame = df
    def set_target_isbn(self,isbn):
        self.__target_isbn = isbn
    def get_target_isbn(self):
        return self.__target_isbn
    def get_target_book_df(self):
        target_book =  self.__data_frame[self.__data_frame['ISBN']== self.__target_isbn]
        self.target_book = target_book
        return target_book
    def target_book_df(self):
        self.__target_book_df = self.get_target_book_df()
    def get_related_users_books(self):
        related_users = self.__data_frame[self.__data_frame['userID'].isin(self.target_book['userID'].tolist())]
        related_users = related_users.loc[related_users['ISBN'] != self.__target_isbn]
        self.__related_users = related_users
    def grouped_by_books(self):
        grouped_books = self.__related_users.groupby('ISBN')
        self.__grouped_books = grouped_books
    def initialize(self,df,isbn,threshhold,algo):
        self.sim = sm.Similarity()
        self.__similarity_ = algo
        self._threshhold = threshhold
        
        self.set_data_frame(df)
        self.set_target_isbn(isbn)
        self.target_book_df()
        self.get_related_users_books()
        self.grouped_by_books()
        return self.closest_n_users()
    def closest_n_users(self):
#         try:
        for name,items in self.__grouped_books:
            targetbook_df=self.target_book[self.target_book['userID'].isin(items['userID'].tolist())]
            tempRatingList = targetbook_df['bookRating'].tolist()
            tempGroupList = items['bookRating'].tolist()

            if(len(tempRatingList) > 2):
                if(sum(tempRatingList) > 0 and sum(tempGroupList) > 0):
#                     print("tempGroupList : ",tempGroupList)
                    similarity = sm.getSimilarity(sim = self.__similarity_, target_r =tempRatingList , closest_r = tempGroupList)
                    if (similarity != 'Undifined'):
                        self.__simDict[name] = similarity
                    else:
                        pass
                else:
                    pass
            else:
                pass
        temp_sim_df = pd.DataFrame.from_dict(self.__simDict, orient='index')
        temp_sim_df.columns = ['similarityIndex']
        temp_sim_df['ISBN'] = temp_sim_df.index
        tm = temp_sim_df.sort_values(by='similarityIndex', ascending=False)[0:self._threshhold]
        return tm
#         except:
#             return "Error"


# In[38]:


import load_data_set as lo
load_dataset = lo.Load_data()
load_dataset.set_urls(['Books.csv','Users.csv','Book-Ratings.csv'])
data_frame = load_dataset.get_user_preferences_df()


# In[39]:


a = RecomenderWithBooks()


# In[40]:


a.initialize(data_frame,'034544003X',10,'pearson_correlation')


# In[ ]:





# In[ ]:




