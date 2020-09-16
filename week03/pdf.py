#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip3 install PyPDF2')


# In[4]:


from PyPDF2 import PdfFileReader


# In[8]:


def getTextPDF(pdfFileName, password = ''):# getTextPDF 함수 
    pdf_file = open(pdfFileName, 'rb')
    read_pdf = PdfFileReader(pdf_file)
    if password != '':
        read_pdf.decrypt(password)
    text = []
    for i in range(0, read_pdf.getNumPages()):
        text.append(read_pdf.getPage(i).extractText())
    return '\n'.join(text)

