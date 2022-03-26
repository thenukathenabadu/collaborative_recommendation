#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

class Load_data:
    def __init__(self,url=None):
        self.__url = url
        self.__book_df = None
        self.__users_df = None
        self.__rating_df = None
        self.__merged_df = None
    def set_urls(self,url):
        self.__url = url
    def books_data(self):
#         books = pd.read_csv(self.__url[0], sep=';',error_bad_lines=False, warn_bad_lines=False,converters={'yearOfPublication': self.convert_dtype})
        books = pd.read_csv(self.__url[0], sep=';',usecols=[0,1,2])
#         books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
        books.columns = ['ISBN', 'bookTitle', 'bookAuthor']
        self.__book_df = books
    def user_data(self):
        users = pd.read_csv(self.__url[1], sep=';', error_bad_lines=False)
        users.columns = ['userID', 'Location', 'Age']
        self.__users_df =  users
    def rating_data(self):
        ratings = pd.read_csv(self.__url[2], sep=';', error_bad_lines=False)
        ratings.columns = ['userID', 'ISBN', 'bookRating']
        self.__rating_df = ratings
    def merge_dataset(self):
        self.get_books_data()
        self.get_rating_data()
        combined_df = pd.merge(self.__rating_df,self.__book_df[['ISBN','bookTitle', 'bookAuthor']],on='ISBN')
        # merged_inner = pd.merge(left=ratings, right=books, left_on='ISBN', right_on='ISBN')
        self.__merged_df = combined_df
    def get_books_data(self):
        return self.books_data()
    def get_user_data(self):
        return self.user_data()
    def get_rating_data(self):
        return self.rating_data()
    def get_user_preferences_df(self):
        self.merge_dataset()
        return self.__merged_df
    def convert_dtype(self,x):
        if not x:
            return ''
        try:
            return str(x)   
        except:        
            return ''


# In[90]:


# load_data_books = Load_data('Books.csv')
# load_data_users = Load_data('Users.csv')
# load_data_books = Load_data('Book-Ratings.csv')


# In[91]:


# urls = ['Books.csv','Users.csv','Book-Ratings.csv']
# load_data_books = Load_data(urls)


# In[92]:


# merged_dataset = load_data_books.merge_dataset()


# In[85]:


# urls = ['Books.csv','Users.csv','Book-Ratings.csv']
# dataset = Load_data(urls)
# dataset.merge_dataset()


# In[83]:


# import pandas as pd
# books = pd.read_csv('Books.csv', sep=';',usecols=[0,1,2])


# In[ ]:





# In[ ]:




