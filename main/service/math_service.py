import heapq
from statistics import median
from unicodedata import decimal
import numpy as np

def calculate_min(list_of_numbers : list,quantifier:int)->list:
    n_minimum_numbers= heapq.nsmallest(quantifier,list_of_numbers)
    return n_minimum_numbers

def calculate_max(list_of_numbers : list,quantifier:int)->list:
    n_maximum_numbers= heapq.nlargest(quantifier,list_of_numbers)
    return n_maximum_numbers

def calculate_average(list_of_numbers : list)->decimal:
    length=len(list_of_numbers)
    if(length==0):
        raise ValueError("List should have atleast one number")

    average=sum(list_of_numbers)/length
    return average

def calculate_median(list_of_numbers : list)->int:
    length=len(list_of_numbers)
    if(length==0):
        raise ValueError("List should have atleast one number")

    median_value=median(list_of_numbers)
    return median_value

def calculate_percentile(list_of_numbers : list,quantifier:float) ->decimal:
    length=len(list_of_numbers)
    if(length==0):
        raise ValueError("List should have atleast one number")
        
    percentage=np.percentile(list_of_numbers,quantifier)
    return percentage