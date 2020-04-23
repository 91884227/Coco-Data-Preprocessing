#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[3]:


import pandas as pd
import numpy as np
import re
from itertools import compress
from tqdm import tqdm
import sys


# In[16]:


def string_replace(str_):
    all_replace_word = ["\n","\u3000"]
    for i in all_replace_word:
        str_ = str_.replace(i, " ")
    return(str_)


# In[53]:


def str_adjust(str_):
    buf = str_
    try:
        m = re.match(r'(^\s+)((.*)(\S))(\s+$)', str_)
        buf = m.group(2)
#         if(len(buf) < 5):
#             print("to short: %s\n" % str_)
    except:
        pass
        print("error happend: %s\n" % str_)
        #print("error happend")
    return(buf)


# In[55]:


if __name__ == '__main__':
    FIALNAME =  sys.argv[1]
    #FILENAME = "coco_title_category_1_to_3_MAX_5.csv"
    MIN_LENGTH = 10

    print("read %s in " % FIALNAME)
    df = pd.read_csv(FIALNAME, encoding="utf-8")
    title = df.title.to_numpy()

    print("replace %s to \" \" for all title" % ["\n","\u3000"])
    title_A = [string_replace(i) for i in tqdm(title)] 

    print("remove blank in front of title and remove blank at the end of title")
    title_B = [str_adjust(i) for i in tqdm(title_A)]

    print("delete title that len(title) < %d" % MIN_LENGTH)
    title_length = [len(i) for i in title_B]
    bool_want = np.array(title_length) > 10
    title_C = list(compress(title_B, bool_want))

    # save
    name = "%s_adjust.npy" % FIALNAME[:-4]

    try:
        np.save(name, title_C)
        print("preprocessing successfully")
        print("save as %s" % name)
    except:
        print("preprocessing failed")

