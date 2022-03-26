#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np
import scipy.stats.stats as sc
import scipy.spatial.distance as scd
from decimal import Decimal
class Similarity:
    def __init__(self, sim = None, target_r =None , closest_r = None):
        self.__sim = sim
        self.__target_r = target_r
        self.__closest_r = closest_r
    def pearson_correlation(self):
        Sxx = sum([i**2 for i in self.__target_r]) - pow(sum(self.__target_r),2)/float(len(self.__target_r))
        Syy = sum([i**2 for i in self.__closest_r]) - pow(sum(self.__closest_r),2)/float(len(self.__closest_r))
        Sxy = sum( i*j for i, j in zip(self.__target_r, self.__closest_r)) - sum(self.__target_r)*sum(self.__closest_r)/float(len(self.__target_r))
        #If the denominator is different than zero, then divide, else, 0 correlation.
        if Sxx != 0 and Syy != 0:
            similarity = Sxy/np.sqrt(Sxx*Syy)
        else:
            similarity = 0
        return similarity
    def pearson_correlation_scipy(self):
        return sc.pearsonr(self.__target_r,self.__closest_r)[0]
    def squared_euclidean_similarity(self):
        similarity = sum(pow(int(a)-int(b),2) for a, b in zip(self.__target_r, self.__closest_r))
        return self.__distance_to_similarity(similarity)
    def euclidean_similarity(self):
        similarity = math.sqrt(sum(pow(int(a)-int(b),2) for a, b in zip(self.__target_r, self.__closest_r)))
        return self.__distance_to_similarity(similarity)
    def minkowski_distance(self, p_value = 3):
        #https://www.youtube.com/watch?v=0j8uMexxzDo
        #https://medium.com/@kunal_gohrani/different-types-of-distance-metrics-used-in-machine-learning-e9928c5e26c7
        # pass the p_root function to calculate
        # all the value of vector parallelly
        # p = 1, Manhattan Distance
        # p = 2, Euclidean Distance
        # p = 3, minkowski_distance
        # p = infinity, Chebychev Distance
        similarity = self.__p_root((sum(pow(abs(int(a)-int(b)), p_value) for a, b in zip(self.__target_r, self.__closest_r))), p_value)
        return self.__distance_to_similarity(float(similarity))
    def cosine_similarity(self):
        numerator = sum(int(a)*int(b) for a,b in zip(self.__target_r, self.__closest_r))
        dinominator = self.__square_rooted(self.__target_r)*self.__square_rooted(self.__closest_r)
        try:
            similarity = numerator/float(dinominator)
        except:
            similarity = "Undifined"
        return round(similarity,3)
    def spearman_correlation_similarity(self):
        return sc.spearmanr(self.__target_r, self.__closest_r)
    def hamming_distance_similarity(self):
        return self.__distance_to_similarity(scd.hamming(self.__target_r, self.__closest_r))
    def __square_rooted(self,k):
        return round(np.sqrt(sum([int(a)*int(a) for a in k])),3)
    def __distance_to_similarity(self,sim_val):
        #The similarity is indirectly proportional to distance. 
        #As the distance increases, similarity decreases and vice vera
        return (1/1+sim_val)
    def __p_root(self, value, root):
        root_value = 1 / float(root)
        return round (Decimal(value) ** Decimal(root_value), 3)
    def __invalid_similarity(self):
        raise Exception("Error : Invalid Similarity or value error")
    def get_similarity(self):
        if(self.__sim == 'squared_euclidean_similarity'):
            return self.squared_euclidean_similarity()
        elif(self.__sim == 'euclidean_similarity'):
            return self.euclidean_similarity()
        elif(self.__sim == 'pearson_correlation'):
            return self.pearson_correlation()
        elif(self.__sim == 'pearson_correlation_scipy'):
            return self.pearson_correlation_scipy()
        elif(self.__sim == 'minkowski_distance'):
            return self.minkowski_distance()
        elif(self.__sim == 'cosine_similarity'):
            return self.cosine_similarity()
        elif(self.__sim == 'spearman_correlation_similarity'):
            return self.cosine_similarity()
        elif(self.__sim == 'hamming_distance_similarity'):
            return self.hamming_distance_similarity()
        else:
            return self.__invalid_similarity()
    def __repr__(self):
        return "\n The "+self.__sim+" is "+str(self.get_similarity())
    def __str__(self):
        return "\n The "+self.__sim+" is "+str(self.get_similarity())

def getSimilarity(sim = None, target_r =None , closest_r = None):
    obj_sim = Similarity(sim = sim,target_r = target_r,closest_r = closest_r)
    return obj_sim.get_similarity()

def awailable_modules():
    method_list = [method for method in dir(Similarity) if method.startswith('__') is False and method != 'get_similarity' and method.startswith('_') is False]
    return method_list

