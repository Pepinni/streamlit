import streamlit as st
import pandas as pd
import numpy as np



n = st.slider('No of members', 1, 1000, 500)
v = st.slider('No of views', 0, n, 1)
f = st.slider('No of flags', 0, v, 0)
s = st.slider('Sentiment score', -1.0, 1.0, 0.0,0.1)
# n = st.slider('No of members', 1.0, 1000.0, 100.0)
# v = st.slider('No of views', 0.0, n, 1.0)
# f = st.slider('No of flags', 0.0, v, 0.0)
# s = st.slider('Sentiment score', -1.0, 1.0, 0.0,0.1)



#displaying the selected value
def risk(F, S, V):
    return 4*np.exp((F/V) - S)/np.square(1 + np.exp((F/V) - S))
# def risk(F, S, V):
#     return 4*np.exp(4*(F/V) - S)/np.square(1 + np.exp(4*(F/V) - S))

st.write("The risk score is ", 1-risk(f,s,v))












# #adding a range slider

# values = st.slider('Please select a range of values',0.0, 100.0, (40.0, 80.0))



# #displaying the selected values

# st.write('Values selected: ', values)