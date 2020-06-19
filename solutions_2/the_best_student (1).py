#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
def the_best_student(b):
    b = np.array(b)
    i = 0
    mean = 0
    for i in range(len(b)):
        if b[i].mean() > b.mean():
            print('best')
        else:
            print('not')
    return(i)   

