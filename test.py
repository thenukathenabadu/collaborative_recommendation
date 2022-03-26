#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
import sys
import pandas as pd
from main_program import MainProgram
class Test(MainProgram):
    def test(self):
        time.sleep(1)
        print("\n## Collabarative Recomondation System by Asiri Thenuka Thenabadu : 31048197 ##")
        self.__test = MainProgram()
        # loading = ld.Loading()
        self.__test.loading.start(text_start="Program Starting")
        time.sleep(1)
        self.__test.loading.stop(text_end= "")
        self.__test.loading.start(text_start="Loading Data Sets")
        self.__test.set_merged_dataset_df()
        self.__test.loading.stop(text_end= "Data Set loaded Sucessfully")
        self.__test.loading.start(text_start="Please Insert Value to Begin ")
        time.sleep(1)
        self.__test.loading.stop(text_end= "")
        time.sleep(1)
        print("#Please Enter User Id or ISBN to Proceed")
        print("# or !99 to Exit")
        param1 = input("Value : ")
        if param1 != '!99':
            if self.validate_input(param1) == "user":
                print("user")
                sim_matrix = self.similarity_matrix(self.__test.loading)
                if(sim_matrix != False):
                    thresh = self.get_threshold(self.__test.loading)
                    if(thresh != 'End'):
                        self.__test.set_user_data(param1,None,int(thresh),sim_matrix)
                        output = self.__test.user_based_closest_n()
        #                 print(output)
                        if isinstance(output, pd.DataFrame):
                            print('Closest 10 Users :\n')
                            return output.style.hide_index()
                        else:
                            print('Error Occured !! ')
                    else:
                        return self.end_of_program()
                time.sleep(2)
                self.rer_run(self.__test.loading,"## Program ended ##")
            elif self.validate_input(param1) == "book":
                sim_matrix = self.similarity_matrix(self.__test.loading)
                if(sim_matrix != False):
                    thresh = self.get_threshold(self.__test.loading)
                    if(thresh != 'End'):
    #                     test.set_user_data(param1,int(thresh),sim_matrix)
                        self.__test.set_user_data(None,param1,int(thresh),sim_matrix)
                        output = self.__test.book_based_closest_n()
                        if isinstance(output, pd.DataFrame):
                            return output.style.hide_index()
                        else:
                            print('Error Occured !! ')
                time.sleep(2)
                self.rer_run(self.__test.loading,"## Program ended ##")
            else:
                self.rer_run(self.__test.loading,"Invalid Input Please Start Again ")
        else:
            self.end_of_program()
        
    def get_threshold(self,loading):
        thresh = 0
        i = 0
        while(thresh == 0):
            thresh = input("Threshold : ")
            if(thresh == "!99"):
                thresh = 'End'
                break
            elif((thresh.isdecimal() == False)):
                thresh = 0
            if(i > 0):
                loading.start(text_start="Invalid Threshold Value Please Try Again ")
                time.sleep(1)
                loading.stop(text_end= "")
                time.sleep(1)
        return thresh
        
    def end_of_program(self):
        print("####### End of Program ###########")
        return False

    def similarity_matrix(self,loading):
        import similarities as sm
        time.sleep(1)
        loading.start(text_start="Please Select Similarity matrix ")
        time.sleep(1)
        loading.stop(text_end= "")
        awailable_modals = sm.awailable_modules()
        time.sleep(1)
        for i,val in enumerate(awailable_modals):
            print("\r"+str(i+1)+"."+val+" \n")
        sim_matrix = -99
        while(sim_matrix == -99):
            time.sleep(1)
            print("\nPlease Select a similarity matrics")
            sim_matrix = input("Similarity Matrix Id : ")
            if(sim_matrix.isdecimal() == True):
                if(int(sim_matrix) > 0 and int(sim_matrix) < len(awailable_modals)):
                    print("You selected, "+ awailable_modals[int(sim_matrix)-1])
                    return awailable_modals[int(sim_matrix)-1]
                    break
                else:
                    reload_sim(loading)
                    sim_matrix = -99
            elif(sim_matrix == "!99"):
                return self.end_of_program()
                break
            else:
                reload_sim(loading)
                sim_matrix = -99

    def reload_sim(self,loading):
        loading.start(text_start="Invalid Similarity Please select Correct Similarity ")
        time.sleep(2)
        loading.stop(text_end= "")


    def rer_run(self,loading,welcome_text):
        loading.start(text_start=welcome_text)
        time.sleep(1)
        loading.stop(text_end= "")
        loading.start(text_start="To Exit Please enter !99 ")
        time.sleep(1)
        loading.stop(text_end= "") 
        self.test()
    def validate_input(self,value):
        if(value.isnumeric() and len(value) <= 6 and ((' ' in value) == False)):
        # user to user similarity 
            return "user"
        elif(any(map(str.isdigit, value)) and len(value) < 14 and len(value) > 6 and ((' ' in value) == False)):
        # user to user similarity 
            return "book"
        else:
            return "invalid" 
    def test_case(self,user_id = '276704',isbn=None, similarity_func = 'pearson_correlation', threshold= 10):
        print("## Test Case Input User Id : Collabarative Recomondation System by Asiri Thenuka Thenabadu : 31048197 ##")
#         self.__test = MainProgram()
        self.set_merged_dataset_df()
        self.set_user_data(user_id,isbn,threshold,similarity_func)
        return self.user_based_closest_n()
    def test_case_2(self,user_id = None, isbn = '034544003X', similarity_func = 'pearson_correlation', threshold= 10):
        print("## Test Case Book Id: Collabarative Recomondation System by Asiri Thenuka Thenabadu : 31048197 ##")
#         test = MainProgram()
        self.set_merged_dataset_df()
        self.set_user_data(user_id,isbn,threshold,similarity_func)
        return self.book_based_closest_n()


# In[2]:


# import time
# import sys
# import pandas as pd

# def test():
#     time.sleep(1)
#     print("\n## Collabarative Recomondation System by Asiri Thenuka Thenabadu : 31048197 ##")
#     test = MainProgram()
#     # loading = ld.Loading()
#     test.loading.start(text_start="Program Starting")
#     time.sleep(1)
#     test.loading.stop(text_end= "")
#     test.loading.start(text_start="Loading Data Sets")
#     test.set_merged_dataset_df()
#     test.loading.stop(text_end= "Data Set loaded Sucessfully")
#     test.loading.start(text_start="Please Insert Value to Begin ")
#     time.sleep(1)
#     test.loading.stop(text_end= "")
#     time.sleep(1)
#     print("#Please Enter User Id or ISBN to Proceed")
#     print("# or !99 to Exit")
#     param1 = input("Value : ")
#     if param1 != '!99':
#         if validate_input(param1) == "user":
#             print("user")
#             sim_matrix = similarity_matrix(test.loading)
#             if(sim_matrix != False):
#                 thresh = get_threshold(test.loading)
#                 if(thresh != 'End'):
#                     test.set_user_data(param1,None,int(thresh),sim_matrix)
#                     output = test.user_based_closest_n()
#     #                 print(output)
#                     if isinstance(output, pd.DataFrame):
#                         print('Closest 10 Users :\n')
#                         return output.style.hide_index()
#                     else:
#                         print('Error Occured !! ')
#             time.sleep(2)
#             rer_run(test.loading,"## Program ended ##")
#         elif validate_input(param1) == "book":
#             sim_matrix = similarity_matrix(test.loading)
#             if(sim_matrix != False):
#                 thresh = get_threshold(test.loading)
#                 if(thresh != 'End'):
# #                     test.set_user_data(param1,int(thresh),sim_matrix)
#                     test.set_user_data(None,param1,int(thresh),sim_matrix)
#                     output = test.book_based_closest_n()
#                     if isinstance(output, pd.DataFrame):
#                         return output.style.hide_index()
#                     else:
#                         print('Error Occured !! ')
#             time.sleep(2)
#             rer_run(test.loading,"## Program ended ##")
#         else:
#             rer_run(test.loading,"Invalid Input Please Start Again ")
#     else:
#         end_of_program()
        
        
# def get_threshold(loading):
#     thresh = 0
#     i = 0
#     while(thresh == 0):
#         thresh = input("Threshold : ")
#         if(thresh == "!99"):
#             thresh = 'End'
#             break
#         elif((thresh.isdecimal() == False)):
#             thresh = 0
#         if(i > 0):
#             loading.start(text_start="Invalid Threshold Value Please Try Again ")
#             time.sleep(1)
#             loading.stop(text_end= "")
#             time.sleep(1)
#     return thresh
        
# def end_of_program():
#     print("####### End of Program ###########")
#     return False
    
# def similarity_matrix(loading):
#     import similarities as sm
#     time.sleep(1)
#     loading.start(text_start="Please Select Similarity matrix ")
#     time.sleep(1)
#     loading.stop(text_end= "")
#     awailable_modals = sm.awailable_modules()
#     time.sleep(1)
#     for i,val in enumerate(awailable_modals):
#         print("\r"+str(i+1)+"."+val+" \n")
#     sim_matrix = -99
#     while(sim_matrix == -99):
#         time.sleep(1)
#         print("\nPlease Select a similarity matrics")
#         sim_matrix = input("Similarity Matrix Id : ")
#         if(sim_matrix.isdecimal() == True):
#             if(int(sim_matrix) > 0 and int(sim_matrix) < len(awailable_modals)):
#                 print("You selected, "+ awailable_modals[int(sim_matrix)-1])
#                 return awailable_modals[int(sim_matrix)-1]
#                 break
#             else:
#                 reload_sim(loading)
#                 sim_matrix = -99
#         elif(sim_matrix == "!99"):
#             return end_of_program()
#             break
#         else:
#             reload_sim(loading)
#             sim_matrix = -99
            
# def reload_sim(loading):
#     loading.start(text_start="Invalid Similarity Please select Correct Similarity ")
#     time.sleep(2)
#     loading.stop(text_end= "")
    
    
# def rer_run(loading,welcome_text):
#     loading.start(text_start=welcome_text)
#     time.sleep(1)
#     loading.stop(text_end= "")
#     loading.start(text_start="To Exit Please enter !99 ")
#     time.sleep(1)
#     loading.stop(text_end= "") 
#     test()
# def validate_input(value):
#     if(value.isnumeric() and len(value) <= 6 and ((' ' in value) == False)):
#     # user to user similarity 
#         return "user"
#     elif(any(map(str.isdigit, value)) and len(value) < 14 and len(value) > 6 and ((' ' in value) == False)):
#     # user to user similarity 
#         return "book"
#     else:
#         return "invalid" 
# def test_case(user_id = '276704',isbn=None, similarity_func = 'pearson_correlation', threshold= 10):
#     print("## Test Case Input User Id : Collabarative Recomondation System by Asiri Thenuka Thenabadu : 31048197 ##")
#     test = MainProgram()
#     test.set_merged_dataset_df()
#     test.set_user_data(user_id,isbn,threshold,similarity_func)
#     return test.user_based_closest_n()
# def test_case_2(user_id = None, isbn = '034544003X', similarity_func = 'pearson_correlation', threshold= 10):
#     print("## Test Case Book Id: Collabarative Recomondation System by Asiri Thenuka Thenabadu : 31048197 ##")
#     test = MainProgram()
#     test.set_merged_dataset_df()
#     test.set_user_data(user_id,isbn,threshold,similarity_func)
#     return test.book_based_closest_n()


# In[1]:


# import time
# import sys
# import pandas as pd
# from main_program import MainProgram
# class Test(MainProgram):
#     def test(self):
#         time.sleep(1)
#         print("\n## Collabarative Recomondation System by Asiri Thenuka Thenabadu : 31048197 ##")
#         self.__test = MainProgram()
#         # loading = ld.Loading()
#         self.__test.loading.start(text_start="Program Starting")
#         time.sleep(1)
#         self.__test.loading.stop(text_end= "")
#         self.__test.loading.start(text_start="Loading Data Sets")
#         self.__test.set_merged_dataset_df()
#         self.__test.loading.stop(text_end= "Data Set loaded Sucessfully")
#         self.__test.loading.start(text_start="Please Insert Value to Begin ")
#         time.sleep(1)
#         self.__test.loading.stop(text_end= "")
#         time.sleep(1)
#         print("#Please Enter User Id or ISBN to Proceed")
#         print("# or !99 to Exit")
#         param1 = input("Value : ")
#         if param1 != '!99':
#             if self.validate_input(param1) == "user":
#                 print("user")
#                 sim_matrix = self.similarity_matrix(self.__test.loading)
#                 if(sim_matrix != False):
#                     thresh = self.get_threshold(self.__test.loading)
#                     if(thresh != 'End'):
#                         self.__test.set_user_data(param1,None,int(thresh),sim_matrix)
#                         output = self.__test.user_based_closest_n()
#         #                 print(output)
#                         if isinstance(output, pd.DataFrame):
#                             print('Closest 10 Users :\n')
#                             return output.style.hide_index()
#                         else:
#                             print('Error Occured !! ')
#                     else:
#                         return self.end_of_program()
#                 time.sleep(2)
#                 self.rer_run(self.__test.loading,"## Program ended ##")
#             elif self.validate_input(param1) == "book":
#                 sim_matrix = self.similarity_matrix(self.__test.loading)
#                 if(sim_matrix != False):
#                     thresh = self.get_threshold(self.__test.loading)
#                     if(thresh != 'End'):
#     #                     test.set_user_data(param1,int(thresh),sim_matrix)
#                         self.__test.set_user_data(None,param1,int(thresh),sim_matrix)
#                         output = self.__test.book_based_closest_n()
#                         if isinstance(output, pd.DataFrame):
#                             return output.style.hide_index()
#                         else:
#                             print('Error Occured !! ')
#                 time.sleep(2)
#                 self.rer_run(self.__test.loading,"## Program ended ##")
#             else:
#                 self.rer_run(self.__test.loading,"Invalid Input Please Start Again ")
#         else:
#             self.end_of_program()
        
#     def get_threshold(self,loading):
#         thresh = 0
#         i = 0
#         while(thresh == 0):
#             thresh = input("Threshold : ")
#             if(thresh == "!99"):
#                 thresh = 'End'
#                 break
#             elif((thresh.isdecimal() == False)):
#                 thresh = 0
#             if(i > 0):
#                 loading.start(text_start="Invalid Threshold Value Please Try Again ")
#                 time.sleep(1)
#                 loading.stop(text_end= "")
#                 time.sleep(1)
#         return thresh
        
#     def end_of_program(self):
#         print("####### End of Program ###########")
#         return False

#     def similarity_matrix(self,loading):
#         import similarities as sm
#         time.sleep(1)
#         loading.start(text_start="Please Select Similarity matrix ")
#         time.sleep(1)
#         loading.stop(text_end= "")
#         awailable_modals = sm.awailable_modules()
#         time.sleep(1)
#         for i,val in enumerate(awailable_modals):
#             print("\r"+str(i+1)+"."+val+" \n")
#         sim_matrix = -99
#         while(sim_matrix == -99):
#             time.sleep(1)
#             print("\nPlease Select a similarity matrics")
#             sim_matrix = input("Similarity Matrix Id : ")
#             if(sim_matrix.isdecimal() == True):
#                 if(int(sim_matrix) > 0 and int(sim_matrix) < len(awailable_modals)):
#                     print("You selected, "+ awailable_modals[int(sim_matrix)-1])
#                     return awailable_modals[int(sim_matrix)-1]
#                     break
#                 else:
#                     reload_sim(loading)
#                     sim_matrix = -99
#             elif(sim_matrix == "!99"):
#                 return self.end_of_program()
#                 break
#             else:
#                 reload_sim(loading)
#                 sim_matrix = -99

#     def reload_sim(self,loading):
#         loading.start(text_start="Invalid Similarity Please select Correct Similarity ")
#         time.sleep(2)
#         loading.stop(text_end= "")


#     def rer_run(self,loading,welcome_text):
#         loading.start(text_start=welcome_text)
#         time.sleep(1)
#         loading.stop(text_end= "")
#         loading.start(text_start="To Exit Please enter !99 ")
#         time.sleep(1)
#         loading.stop(text_end= "") 
#         self.test()
#     def validate_input(self,value):
#         if(value.isnumeric() and len(value) <= 6 and ((' ' in value) == False)):
#         # user to user similarity 
#             return "user"
#         elif(any(map(str.isdigit, value)) and len(value) < 14 and len(value) > 6 and ((' ' in value) == False)):
#         # user to user similarity 
#             return "book"
#         else:
#             return "invalid" 
#     def test_case(self,user_id = '276704',isbn=None, similarity_func = 'pearson_correlation', threshold= 10):
#         print("## Test Case Input User Id : Collabarative Recomondation System by Asiri Thenuka Thenabadu : 31048197 ##")
# #         self.__test = MainProgram()
#         self.set_merged_dataset_df()
#         self.set_user_data(user_id,isbn,threshold,similarity_func)
#         return self.user_based_closest_n()
#     def test_case_2(self,user_id = None, isbn = '034544003X', similarity_func = 'pearson_correlation', threshold= 10):
#         print("## Test Case Book Id: Collabarative Recomondation System by Asiri Thenuka Thenabadu : 31048197 ##")
# #         test = MainProgram()
#         self.set_merged_dataset_df()
#         self.set_user_data(user_id,isbn,threshold,similarity_func)
#         return self.book_based_closest_n()


# In[2]:


# a= Test()


# In[5]:


# a.test()


# In[6]:


# a.set_merged_dataset_df()


# In[ ]:


# loading = ld.Loading()
# similarity_matrix(loading)


# In[7]:


# test_case()


# In[8]:


# test_case_2().style.hide_index()


# In[10]:


# test()


# In[28]:


# newoutput


# In[27]:


# a = test_case()


# In[26]:


# a.style.hide_index()


# In[ ]:


# load_dataset = lo.Load_data()
# load_dataset.set_urls(['Books.csv','Users.csv','Book-Ratings.csv'])
# data_frame = load_dataset.get_user_preferences_df()


# In[ ]:


# data_frame


# In[ ]:


# import load_data_set as lo
# load_dataset = lo.Load_data()
# load_dataset.set_urls(['Books.csv','Users.csv','Book-Ratings.csv'])
# data_frame = load_dataset.get_user_preferences_df()


# In[ ]:


# rc = rc_users.RecomenderWithUsers()
# rc.initialize(df=data_frame,user_id = "236959", algo = 'pearson_correlation_scipy', threshhold= 10)


# In[ ]:





# In[23]:


# import loading as ld
# import similarities as sm
# import time
# import sys
# loading = ld.Loading()
# awailable_modals = sm.awailable_modules()
# print(len(awailable_modals))
# sim_matrix = -99
# while (int(sim_matrix) <= 0 or int(sim_matrix) > len(awailable_modals) or isinstance(sim_matrix, int) == False):
#         sim_matrix = int(input("Similarity Matrix Id : "))
#         if(isinstance(sim_matrix, int)):
#             print("==========",int(sim_matrix) > len(awailable_modals))
#             if(int(sim_matrix) < 0 and int(sim_matrix) > len(awailable_modals)):
#                 loading.start(text_start="Invalid Similarity Please select Correct Similarity ")
#                 time.sleep(2)
#                 loading.stop(text_end= "")
#             else:
#                 loading.start(text_start="Invalid Similarity Please select Correct Similarity ")
#                 time.sleep(2)
#                 loading.stop(text_end= "")
#                 similarity_matrix(loading)
#         else:
#             pass


# In[24]:


# awailable_modals = sm.awailable_modules()
# print(len(awailable_modals))


# In[25]:


# isinstance("123", int)

