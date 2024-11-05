#!/usr/bin/env python
# coding: utf-8

# # STREAMLIT PARTE 2

# ### Aula 1:
# - Apresentação do dataset
# - Apresentação da ferramenta final
# 
# ### Aula 2:
# - Parte 1:
#     - 1 coluna como filtro
#     - st.set_page_config()
#     - st.image()
#     - st.slider()
#     - st.pyplot()
# - Parte 2:
#     - 2 colunas como filtro
#     - st.multiselect()
# - Parte 3:
#     - st.form()
#     - st.form_submit_button()
#     - sns.set_theme()
# 
# ### Aula 3:
# - 9 colunas como filtro
# 
# 
# ### Aula 4:
# - pip install --upgrade streamlit
# - pip install --upgrade matplotlib
# - st.cache()
# 
# 
# ### Aula 5:
# - st.file_uploader()
# 
# 
# ### Aula 6:
# - st.download_button()
# 
# 
# ### Aula 7:
# - st.columns()
# - st.radio()
# 

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[28]:


bank_raw = pd.read_csv('./data/input/bank-additional-full.csv', sep=';')
# se executado pelo jupyter alterar o formato da exportação do arquivo para:
# bank = pd.read_csv('./data/input/bank-additional-full.csv', sep=';')

bank = bank_raw.copy()


# In[30]:


bank_raw.head(2)


# In[32]:


# IDADES
max_age = int(bank.age.max())
min_age = int(bank.age.min())
print(min_age,max_age)


# In[5]:


bank_raw.shape


# In[34]:


idades = [min_age,26]


# In[36]:


bank = bank[(bank['age'] >= idades[0]) & (bank['age'] <= idades[1])]


# In[38]:


bank.head()


# In[40]:


bank.shape


# In[42]:


bank_raw_target_perc = bank_raw.y.value_counts(normalize = True).to_frame()*100
bank_raw_target_perc = bank_raw_target_perc.sort_index()
bank_raw_target_perc


# In[48]:


bank_target_perc = bank.y.value_counts(normalize = True).to_frame()*100
bank_target_perc = bank_target_perc.sort_index()
bank_target_perc


# In[46]:


# # PLOTS
fig, ax = plt.subplots(1, 2, figsize = (5,3))


sns.barplot(x = bank_raw_target_perc.index,
            y = 'y',
            data = bank_raw_target_perc,
            ax = ax[0])
ax[0].bar_label(ax[0].containers[0])
ax[0].set_title('Dados brutos',
                fontweight ="bold")


sns.barplot(x = bank_target_perc.index,
            y = 'y',
            data = bank_target_perc,
            ax = ax[1])
ax[1].bar_label(ax[1].containers[0])
ax[1].set_title('Dados filtrados',
                fontweight ="bold")


# **Aula 2 - Parte II: Aplicação Inicial - Parte 2**

# In[13]:


idades = [17,98]


# In[14]:


bank.head(2)


# In[50]:


bank.job.unique().tolist()


# In[70]:


jobs_list = bank.job.unique().tolist()
jobs_list.append('all')
print('PROFISSÕES DISPONIVEIS:', jobs_list)


# In[72]:


jobs_selected = ['all']
jobs_selected


# In[74]:


bank = bank_raw.copy()
bank.shape


# In[76]:


jobs_selected = jobs_list
jobs_selected = ['housemaid','services']


# In[78]:


bank = bank_raw.copy()
bank.shape


# In[84]:


# bank = bank[(bank['age'] >= idades[0]) & (bank['age'] <= idades[1])]

bank = bank[bank['job'].isin(jobs_selected)].reset_index(drop=True)


# In[86]:


bank.shape


# **Aula 2 - Parte III: Aplicação Inicial**

# In[88]:


bank = bank_raw.copy()
bank.shape


# In[24]:


if 'all' in jobs_selected:
    pass
else:
    bank = bank[bank['job'].isin(jobs_selected)].reset_index(drop=True)


# In[25]:


bank.shape


# **Aula 3: 9 Colunas como filtro**

# In[26]:


bank[['age','job','marital','default','housing','loan','contact','month','day_of_week','y']]


# In[27]:


bank.day_of_week.unique().tolist()


# **Aula 4: st.cache()**

# In[28]:


bank_maior = pd.concat([bank]*20,ignore_index=True)
bank_maior


# In[29]:


bank_maior.shape


# In[ ]:


bank_maior.to_csv('./data/input/bank-additional-full-40.csv',index=False, sep=';')


# **Aula 5: st.file_uploader()**

# In[31]:


## diretamente nos códigos do streamlit


# **Aula 7: st.download_button()**

# In[32]:


bank = pd.read_csv("bank-additional-full.csv", delimiter=';')
# se executado pelo jupyter alterar o formato da exportação do arquivo para:
# bank = pd.read_csv('./data/input/bank-additional-full.csv', sep=';')

bank.head(10)


# In[66]:


a = bank.to_csv()


# In[34]:


type(a)


# In[68]:


b = a.encode('utf-8')


# In[36]:


type(b)


# In[37]:


from io                     import BytesIO


# In[38]:


pip install XlsxWriter


# In[39]:


output = BytesIO()
writer = pd.ExcelWriter(output, engine='xlsxwriter')


# In[40]:


bank.to_excel(writer, index=False, sheet_name='Sheet1')


# In[41]:


writer


# In[42]:


writer.save()


# In[43]:


processed_data = output.getvalue()


# In[44]:


processed_data[:100]


# In[47]:


a=bank.y.value_counts(normalize=True).to_frame()
a


# In[49]:


a.plot.pie(y = 'y',ax=ax[1])


# In[50]:


fig, ax = plt.subplots(1, 1, figsize = (5,3))
a.plot(kind='pie', autopct='%.2f', y='y', ax = ax)
plt.show()


# In[51]:


a.plot(kind='bar')


# **Aula 7: st.collumns() e st.radio()**

# In[52]:


## diretamente nos códigos do streamlit

