#!/usr/bin/env python
# coding: utf-8

# In[74]:


import telebot
import pandas as pd
from telebot import types
import datetime 
import matplotlib.pyplot as plt
import json


# In[106]:


df = pd.read_excel("Data/SCORES.xlsx",index_col="Member Code")
#df = df.sort_values(by='Activity')
length = len(df)
#my_ranking_list = [i for i in range(1,length+1)]
#my_ranking_list.reverse()
#df['rank']= my_ranking_list

df_min = pd.read_excel("Data/FDataVR.xlsx",index_col="Student Number")
#df_min = df_min.sort_values(by='Total')
#length2 = len(df_min)
#my_ranking_list2 = [i for i in range(1,length2+1)]
#my_ranking_list2.reverse()
#df_min['rank_min']= my_ranking_list2


# In[12]:


def CodeisValid(number):
    if number in df.index:
        return True
    return False


# In[13]:


def PassisValid(member_code,password):
    real_password = str(df.loc[member_code].Password)
    if password == real_password:
        return True
    return False


# In[14]:


def GetName(member_code):
    return df_min.loc[member_code]['Latin Name']


# In[ ]:


def GetScore(member_code):
    return str(df.loc[member_code].Activity)


# In[ ]:


def GetTime(member_code):
    return str(round(df_min.loc[member_code].Total/60,2))


# In[15]:


def GetExperience(member_code):
    #date_read = df_min.loc[member_code]['Join Date'][1:-1]
    #past_date = datetime.date(int(date_read[0:4]), int(date_read[5:7]), int(date_read[8:]))
    
    past_date = df_min.loc[member_code]['Join Date']

    current_date = datetime.date.today()

    # Calculate the difference in days
    difference_in_days = (current_date - past_date).days
    years = difference_in_days // 365
    months = (difference_in_days % 365) // 30
    days = (difference_in_days % 365) % 30
    
    return ("You have been in the speaking group for: \n" + f"{years} year, {months} month, and {days} day")


# In[17]:


def GetFeedback(member_code):
    fb = df.loc[member_code]['Feedback']

    if fb==0:
        return 0
    else:
        return ("Teacher's Feedback: \n"+  fb)


# In[73]:


def history(member_code):
    dff = pd.DataFrame(df_min.loc[member_code][-10:])
    dff.reset_index(inplace=True)
    dff.columns=['week','minute']
    max_y_value = max(dff ['minute'])+10
    
    ax = dff.plot.bar(x='week',y='minute', width=0.7)
    ax.set_ylim(0, max_y_value)
    
    for p in ax.patches:
        ax.annotate(
            str(p.get_height()), 
            (p.get_x() + p.get_width()/2, 
             p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')
    plt.savefig('image_'+str(member_code)+'.jpg',bbox_inches='tight',dpi=200)
    return 1


# In[110]:


def get_score_rank(member_code):
    rank = df.loc[member_code]['rank']
    return ("Your score has ranked " + str(rank) + " among " + str(length) + " members." )


# In[111]:


def get_min_rank(member_code):
    rank = df_min.loc[member_code]['rank']
    return ("Your speaking time has ranked " + str(rank) + " among " + str(length) + " members." )


# In[ ]:


def GetVideo(member_code):
    fb = df.loc[member_code]['Feedback']
    
    try:
        video_file = open(str(member_code)+'.mp4', 'rb')
        return video_file
    except:
        return 0


# In[4]:


def GetVideo(member_code):   
    try:
        video_file = open( r"FB/" + str(member_code)+".mp4", 'rb')
        return video_file
    except:
        return 0


# In[7]:


def GetVoice(member_code):  
    try:
        voice_file = open('FB/'+str(member_code)+'.mp3', 'rb')
        return voice_file
    except:
        return 0


# In[ ]:




