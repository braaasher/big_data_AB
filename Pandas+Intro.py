
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

import pandas as pd


# In[3]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[4]:

s


# In[5]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# In[6]:

pd.Series(d)


# In[7]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[8]:

pd.Series d


# In[9]:

pd.Series(d, index=['b', 'c', 'a'])


# In[10]:

pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])


# In[11]:

s


# In[12]:

s(0)


# In[13]:

s[0]


# In[14]:

s[:3]


# In[15]:

s[s > s.median()]


# In[16]:

s[[4, 3, 1]]


# In[17]:

np.exp(s)


# In[18]:

s['a']


# In[19]:

s['e'] = 12.0


# In[20]:

s


# In[21]:

if 'f' in s:
    s['f']


# In[22]:

s.get('f', np.nan)


# In[23]:

s[:-1]


# In[24]:

s[1:] + s[:-1]


# In[26]:

s['f'] = 0


# In[27]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[28]:

d


# In[29]:

df = pd.DataFrame(d)


# In[30]:

df


# In[31]:

df.index


# In[32]:

pd.DataFrame(d)


# In[33]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[34]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[35]:

data


# In[36]:

pd.DataFrame(data, index=['first', 'second'])


# In[37]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[38]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[39]:

pd.DataFrame(data2)


# In[40]:

df


# In[41]:

df['one']


# In[42]:

df['three'] = df['one'] * df['two']


# In[43]:

df['flag'] = df['one'] > 2


# In[44]:

df


# In[45]:

del df['two']


# In[46]:

three = df.pop('three')


# In[47]:

df


# In[48]:

three


# In[ ]:



