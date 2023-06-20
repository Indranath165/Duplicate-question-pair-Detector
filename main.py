import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

col1.title("Duplicate Question Pairs")
col1.subheader("This app uses a machine learning model to predict if two questions are duplicates or not.")

q1 = col2.text_input('Enter question 1')
q2 = col2.text_input('Enter question 2')

if col2.button('Find'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        col2.markdown(f"**Result:** Duplicate")
    else:
        col2.markdown(f"**Result:** Not Duplicate")
