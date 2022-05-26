#!/usr/bin/env python
# coding: utf-8

# In[43]:





# In[8]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib

contatos_df = pd.read_excel('Enviar.xlsx')

navegador = webdriver.Chrome('chromedriver.exe')
navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements(by = By.ID, value = 'side')) < 1:
    time.sleep(1)

for i, mensagem in enumerate(contatos_df['Mensagem']):
    try:
        pessoa = contatos_df.loc[i, 'Pessoa']
        numero = contatos_df.loc[i, 'Número']
        texto = urllib.parse.quote(f'Oi {pessoa}! {mensagem}')
        link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
        navegador.get(link)
        while len(navegador.find_elements(by = By.ID, value = 'side')) < 1:
            time.sleep(1)
        navegador.implicitly_wait(10)
        navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(10)
        print(f'Mensagem para {pessoa} enviada!')
    except:
        print(f'Ocorreu um erro! Mensagem para {pessoa} não enviada!')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




