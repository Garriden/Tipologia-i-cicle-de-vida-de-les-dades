#!/usr/bin/env python
# coding: utf-8

# ## Web scraping

# In[1]:


import bs4 as bs
import urllib
import urllib.request
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io


# In[2]:


HTML = "https://www.trovimap.com/precio-vivienda/barcelona"


# In[6]:


# Amb .read_html() podem obtenir fàcilment la taula que ens mostra la web.

df = pd.read_html(HTML)
df[0].head()


# In[7]:


# Amb BeautifulSoup, podrem obtenir tot el String del codi HTML per si volem obtenir més informació.

historypage = urllib.request.urlopen(HTML)
soup = bs.BeautifulSoup(historypage,'html.parser')
makeitastring = ''.join(map(str, soup))

soup
#makeitastring


# In[5]:



#retorna un llistat de ciutats i la seva variació de preu segons el html ja llegit per BeatifulSoup que li hem passat. Aquest html està format segons 
# la provincia. Per exemple: HTML = "https://www.trovimap.com/precio-vivienda/barcelona" retornarà un llistat amb les
# ciutats que es troben en aquesta pàgina que son les ciutats de Barcelona i les seves variacions de preus mensual, els últims 3 mesos
# anual i preu euro/ metre quadrat.

def obtenirCiutatsiVariacio(htmlSoup):
    tableProv = soup.find('table', {'class':'table table-condensed precio-medio-table'})

    tbody = tableProv.find('tbody')

    llistaVarCiutats=[]
    for row in tbody.findAll("tr"):
        cells = row.findAll('td')    
        link = cells[0].find('a')
        ciutat = link.find(text=True)
        #print(ciutat)
        varMensual = cells[1].find(text=True)
        var3mesos = cells[2].find(text=True)
        varAnual = cells[3].find(text=True)
        eumetre = cells[4].find(text=True)
        element=[ciutat,varMensual,var3mesos,varAnual,eumetre]
        llistaVarCiutats.append(element)
        
        
    return llistaVarCiutats


HTML = "https://www.trovimap.com/precio-vivienda/barcelona"

VarCiutat = obtenirCiutatsiVariacio(soup)

print(VarCiutat[0])


# In[ ]:





# In[ ]:





# In[13]:


HTML = "https://www.trovimap.com/precio-vivienda/"


# In[19]:


HTMLEspana = HTML + "espana"

df = pd.read_html(HTMLEspana)
dfProvinciesEspana = df[0]
dfProvinciesEspana = dfProvinciesEspana.rename(columns={"Unnamed: 0": 'Provincies'})

dfProvinciesEspana.head()


# ### Obtenim una taula amb la variació menusal de cada provincia de l'estat.

# ### Si volem obtenir una taula, tenint per files les ciutats més importants de cada provincia tal com hem fet anteriorment amb la de Barcelona:

# In[25]:


dfProvinciesEspana.iloc[0]['Provincies']


# ### Si volem obtenir una taula, tenint per files les ciutats més importants de Catalunta:

# In[37]:


# Agafar la taula per cada una de les quatre provincies de Catalunya.
dfBarcelona = pd.read_html(HTML+"barcelona")
dfTarragona = pd.read_html(HTML+"tarragona")
dfGirona = pd.read_html(HTML+"girona")
dfLleida = pd.read_html(HTML+"lleida")
dfBarcelona = dfBarcelona[0]
dfTarragona = dfTarragona[0]
dfGirona = dfGirona[0]
dfLleida = dfLleida[0]

# Concatenar Taules.
dfCatalunya = pd.concat([dfBarcelona, dfTarragona], ignore_index=True)
dfCatalunya = pd.concat([dfCatalunya, dfGirona], ignore_index=True)
dfCatalunya = pd.concat([dfCatalunya, dfLleida], ignore_index=True)

# Renombrar columnes.
dfCatalunya = dfCatalunya.rename(columns={"Unnamed: 0": 'Provincies', "Variación Mensual": 'Variació mensual',
                                "Variación 3 meses": 'Variació tres messos', "Variación anual": 'Variació anual'})

dfCatalunya.tail()


# In[ ]:




