#!/usr/bin/env python
# coding: utf-8

# In[87]:


import similarities as sm
import pandas as pd
class RecomenderWithUsers():
    def __init__(self):
        self.sim = sm.Similarity()
        self.__simDict={}
    def initialize(self,df,user_id,threshhold,algo):
        self._threshhold = threshhold
        self.similarity_algo = algo
        self.set_data_frame(df)
        self.set_target_user(user_id)
        self.target_users_df()
        self.related_users_df()
        self.order_user_by_rating()
        return self.closest_n_users()
#         return self.closest_n_similarity_df
    def set_data_frame(self,df):
        self.__data_frame = df
    def set_target_user(self,user_id):
        self.target_user_id = user_id
    def get_target_user(self):
        return self.target_user_id
    def get_target_user_df(self):
#         print("============",self.__data_frame.head(10))
#         print("self.target_user_id :",self.target_user_id)
        return self.__data_frame.loc[self.__data_frame['userID'] == int(self.target_user_id)][['bookRating','ISBN']]
    def target_users_df(self):
        self.__target_user_df = self.get_target_user_df()
#         print("target_user_df : ",  self.__target_user_df)
    def get_related_users(self):
        temp_df = self.__data_frame[self.__data_frame['ISBN'].isin(self.__target_user_df['ISBN'].tolist())]
        return temp_df.loc[temp_df['userID'] != int(self.target_user_id)]
    def related_users_df(self):
        self.related_users = self.get_related_users()
#         print("self.related_users",self.related_users)
    def order_user_by_rating(self):
        temp_group_by_df = self.related_users.groupby(['userID'])
        # order by the most common rating count
        self.related_users_orderd = sorted(temp_group_by_df,  key=lambda x: len(x[1]), reverse=True)
#         print(" == ",self.related_users_orderd)
    def closest_n_users(self):
        try:
            for name,group in self.related_users_orderd:
    #             print("self.related_users_orderd == ",name)
                group = group.sort_values(by='ISBN')
                targetsBooks = self.__target_user_df.sort_values(by='ISBN')
                temp_df = targetsBooks[targetsBooks['ISBN'].isin(group['ISBN'].tolist())]
                tempRatingList = temp_df['bookRating'].tolist()
                tempGroupList = group['bookRating'].tolist()
    #             print("tempGroupList : ",tempGroupList)
                if(len(tempRatingList) > 2):
                    if(sum(tempRatingList) > 0 and sum(tempGroupList) > 0):
    #                     print("tempGroupList : ",tempGroupList)
                        similarity = sm.getSimilarity(sim = self.similarity_algo, target_r =tempRatingList , closest_r = tempGroupList)
                        if (similarity != 'Undifined'):
                            self.__simDict[name] = similarity
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            temp_sim_df = pd.DataFrame.from_dict(self.__simDict, orient='index')
    #         print(temp_sim_df)
            temp_sim_df.columns = ['similarityIndex']
            temp_sim_df['userID'] = temp_sim_df.index
    #             temp_sim_df.index = range(len(temp_sim_df))
            tm = temp_sim_df.sort_values(by='similarityIndex', ascending=False)[0:self._threshhold]
    #             print("== \n",tm)
            return tm
        except:
            return "Error"
            
        
    


# In[88]:


# import load_data_set as lo
# load_dataset = lo.Load_data()
# load_dataset.set_urls(['Books.csv','Users.csv','Book-Ratings.csv'])
# data_frame = load_dataset.get_user_preferences_df()


# In[89]:


# rc = RecomenderWithUsers()
# rc.initialize(df=data_frame,user_id = "236959", algo = 'pearson_correlation_scipy', threshhold= 10)


# In[90]:


# rc = RecomenderWithUsers()
# rc.initialize(df=data_frame,user_id = "236959", algo = 'pearson_correlation', threshhold= 10)


# In[91]:


# data_frame.loc[data_frame['userID'] == 236959][['bookRating','ISBN']]


# In[ ]:





# In[ ]:




