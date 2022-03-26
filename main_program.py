#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import loading as ld
from load_data_set import Load_data
from recomend_on_users import RecomenderWithUsers
from recomend_on_books import RecomenderWithBooks
import similarities as sm
# import similarities as sm
import pandas as pd
class MainProgram(RecomenderWithBooks,RecomenderWithUsers,Load_data):
    def __init__(self):
        self.urls = ['Books.csv','Users.csv','Book-Ratings.csv']
        self.loading = ld.Loading()
#         self.load_dataset = lo.Load_data()
        self.set_urls(self.urls)
        self.user_base = RecomenderWithUsers()
        self.book_base = RecomenderWithBooks()
    def set_user_data(self,user_id,isbn,threshhold,algo):
        self.user_id = user_id
        self.threshhold = threshhold
        self.algo = algo
        self.isbn = isbn
    def set_merged_dataset_df(self):
        self.data_frame = self.get_user_preferences_df()
    def user_based_closest_n(self):
        print("User Base Closest Users")
        return self.user_base.initialize(self.data_frame,self.user_id,self.threshhold,self.algo)
    def book_based_closest_n(self):
        print("Book Base Closest Books")
        return self.book_base.initialize(self.data_frame,self.isbn,self.threshhold,self.algo)

