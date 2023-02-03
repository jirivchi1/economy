import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import time

import streamlit as st
#import seaborn as sns


""" plt.style.use('fivethirtyeight')
pd.set_option('display.max_columns', 500)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"] """

from fredapi import Fred

fred_key = '18f340df3ee3b8b51232b8c2b83b6ff1'

#create fred object
fred = Fred(api_key=fred_key)

#get inflation data from spain
inflation = fred.get_series('CPALTT01ESM657N')

print(inflation.describe)

#plot inflation in streamlit
st.line_chart(inflation)
