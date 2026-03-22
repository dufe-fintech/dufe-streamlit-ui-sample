import streamlit as st
import pandas as pd 

st.title("Sample UI")

st.write("Hello Visitor, Welcome!")

name = st.text_input("Write your name")
st.write("Your name is : ",name)

age = st.slider("Select ur age",1,100,25)
st.write("your age is :  ",age)

Tool = ["Python","Excel","PPT","SQL","Power BI"]

Fav_tool = st.selectbox("select ur fav tool",Tool)
st.write("Your fav tool : ",Fav_tool)

File = st.file_uploader("Upload ur file",type="csv")

if File is not None:
    df = pd.read_csv(File)
    st.write("File preview")
    st.dataframe(df.head())
