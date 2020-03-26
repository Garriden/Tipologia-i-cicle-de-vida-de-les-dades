#!/usr/bin/env python
# coding: utf-8

# ## Web scraping

# In[9]:


import bs4 as bs
import urllib
import urllib.request
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io


# In[10]:


HTML = "https://www.trovimap.com/precio-vivienda/barcelona"


# In[11]:


# Amb .read_html() podem obtenir fàcilment la taula que ens mostra la web.

df = pd.read_html(HTML)
df[0].head()


# In[12]:


# Amb BeautifulSoup, podrem obtenir tot el String del codi HTML per si volem obtenir més informació.

df = pd.DataFrame()

historypage = urllib.request.urlopen(HTML)
soup = bs.BeautifulSoup(historypage,'html.parser')
makeitastring = ''.join(map(str, soup))


# Busquem els pobles que pertanyen a ** Barcelona **

tableProv = soup.find('table', {'class':'table table-condensed precio-medio-table'})
strtableProv = ''.join(map(str, tableProv))

tbody = tableProv.find('tbody')
strtbody = ''.join(map(str, tbody))
  #currentIndex=0
for row in tbody.findAll("tr"):
    cells = row.findAll('td')    
    link = cells[0].find('a')
    poble = link.find(text=True)
    print (poble)
    
  #  if (currentIndex >0) # la primera línia es el header 


#makeitastring


# In[ ]:





# In[ ]:




