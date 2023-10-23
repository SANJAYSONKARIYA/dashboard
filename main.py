# 1st_Session (23-10-2023)
import streamlit as st
import seaborn as sns
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

col1, col2, col3 = st.columns(3)

# Mining Data
df = pd.read_csv('data.csv')
st.title('Data Analysis')
if st.sidebar.button('Load Dataset'):
    st.write(df)

if st.button('Load Description'):
    st.write(df.describe())

if st.button('Load Information'):
    st.write(df.info())
# st.table(df)

df1 = df.drop(['ID','Year','Category','Product','UnitPrice','TotalPrice'],axis='columns')
# st.write(df1)
# st.map(df1)

a1 = pd.DataFrame(df['Year'],df['TotalPrice'])
# st.line_chart(df[['Year'],df['TotalPrice']])

if st.button('Load Bar Chart'):
    df2 = df.head(20)
    fig = plt.figure(figsize=(10,8))
    plt.bar(df2['Product'],df2['Qty'])
    st.pyplot(fig)

col1.metric('Name','a','b')
col2.metric('Marks',82,87)
col3.metric('City','JP','DDN')

    

# a = {
#     'name':['John', 'Anna'],
#     'age':[25, 46],
#     'city':['Jaipur','Patna'],
# }
# st.json(a)
# st.table(a)
# st.write(a)
