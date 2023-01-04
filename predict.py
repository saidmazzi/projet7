import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pickle


def prediction(ID, df):

    ID = int(ID)
    X = df[df['SK_ID_CURR'] == ID]
    predict = (1 - X['TARGET'][0])*100
    
    return prediction