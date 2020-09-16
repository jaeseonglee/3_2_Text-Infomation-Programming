#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip3 install python-docx')


# In[2]:


import docx


# In[3]:


def getTextWord(wordFileName): # getTextWord 함수
    doc = docx.Document(wordFileName)
    fullText = []
    for para in doc.paragraphs: # paragraphs 
        fullText.append(para.text)
    return '\n'.join(fullText)


# In[ ]:




