import streamlit as st
st.title(' TDS GA 8')
st.subheader('odd even checking  App')
placeholder_Number = st.empty()
n = placeholder_Number.number_input('Enter Number')
if (n % 2) == 0:
   st.write("your number is even")
else:
   st.write("your number is odd")
