import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pickle
import requests
import time
from urllib.request import urlopen
import json
#from projet7.main.py import *


#Load Dataframe
path_df = "train.csv"
path_kernel = "submission_kernel02.csv"

@st.cache # mise en cache
def loading_data(path):
    dataframe = pd.read_csv(path)
    return dataframe

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

# total data
dataframe1 = loading_data(path_df)
dataframe2 = loading_data(path_kernel)

# data sample (10%)
data_samp = dataframe1.sample(35625, random_state=42)
# ID
id_list = dataframe2['SK_ID_CURR'].tolist()

#data_api = dataframe2.copy(deep=True)

#affichage formulaire ID Client
st.title('Customer Loan Dashboard')
st.subheader("General positioning")

#st.text("Exemples d'identifiants de clients risqués : 100031, 100047, 131711 ou 144155")
#st.text("Exemples d'identifiants de clients peu risqués : 100018, 312966, 362295 ou 448296")
id_input = st.text_input('Veuillez saisir l\'identifiant du client (6 chiffres) :', max_chars=6, key = "<uniquevalueofid>")

chaine = "l\'id saisi est " + str(id_input)
#st.write(chaine)
    
if id_input in id_list: 
    
    st.write("c'est un identifiant connu")
    st.write(pro = dataframe2.loc[dataframe2['SK_ID_CURR']==id_input])
    st.write(proba = (1 - pro['TARGET'][0])*100)
    st.write(proba)
else:
    st.write("Mais il n'est pas dans la liste")

space(2)    
    
# graphes features
    
features_list= ["DAYS_EMPLOYED_PERC","INCOME_CREDIT_PERC","INCOME_PER_PERSON","ANNUITY_INCOME_PERC","PAYMENT_RATE"]

selected_feature=st.selectbox(label="Choose features to visualize", options= features_list)

submitted=st.button("submit")

if submitted:
    filtered_feature = dataframe1[features_list]==selected_feature
    #line_fig=px.scatter(filtered_feature,
                        #   x=filtered_feature)#,
                           #y="Count",
                           #color= "type",
                      #     title= f"features :{filtered_feature} "
                      # )
    hist_values = np.histogram(
    filtered_feature, bins=24, range=(0,1))[0]
    st.bar_chart(hist_values)
    
    #st.plotly_chart(line_fig)







         
          