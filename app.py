import streamlit as st
st.title("Learning is fun :sunglasses:")
st.header("Hello World")
st.subheader("I am learning streamlit🔪")
st.button("Tap me please!!")
tap_button=st.button("Tap me to get an emoji")
if tap_button==True:
    st.subheader(":sunglasses:")