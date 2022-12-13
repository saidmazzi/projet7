import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

st.write("""
## Dashboard
Probabilité de faillite du client
""")

#d = {'col1': [1,2,5,3,9,10], 'col2': [3,4,6,7,2,9]}
#df = pd.DataFrame(data=d)

#st.line_chart(df)

#number = st.slider("Pick a number", 0, 100)

date = st.date_input("Pick a date")

#genre = st.radio(
#    "What's your favorite movie genre",
#    ('Comedy', 'Drama', 'Documentary'))

#if genre == 'Comedy':
#    st.write('You selected comedy.')
#elif genre == 'Drama':
#    st.write('You selected drama.')
#elif genre == 'Documentary':
#    st.write('You selected documentary.')
#else:
#    st.write("good choose.")


    