#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
number = np.random.randint(1,101)    # picked a number
print ("a number between 1 and 100 been picked")

def game_core(number):
 """Function to guess the number"""
 count = 0
 left_border = 1
 right_border = 100
 predict = 0 # variable for guessing the number
 while number!= predict:
        count +=1
        predict = (left_border + right_border)//2
        if number > predict: 
            left_border = (left_border + right_border)//2 + 1
        elif number < predict: 
            right_border = (left_border + right_border)//2 - 1
 return count


# In[21]:


def score_game(game_core):
    '''launching the game 1000 times to learn how quick the number is guessed'''
    count_ls = []
    np.random.seed(1)  # fixing RANDOM SEED to make the experiment reproducibe!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Your algorithm on average guesses the number for {score} iterations")
    return(score)


# In[22]:


score_game(game_core)


# In[ ]:




