import streamlit as st
import pandas as pd
import plotly.express as px 
import os

st.sidebar.title("Penta Investments")
page = st.sidebar.radio("Select a company", ["Dr. Max", "Fortuna", "Penta Hospitals"])

def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"File {file_path} does not exist.")
        return None
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            st.error(f"File {file_path} is empty.")
            return None
        return df
    except pd.errors.EmptyDataError:
        st.error(f"No columns to parse from {file_path}.")
        return None

if page == "Dr. Max":
    st.title("Dr. Max Performance")
    df = load_data("dr_max_data.csv")
    if df is not None:
        fig = px.line(df, x='day', y='sales', title='Dr. Max Sales Over Time')
        st.plotly_chart(fig)

elif page == "Fortuna":
    st.title("Fortuna Revenue")
    df = load_data("fortuna_data.csv")
    if df is not None:
        fig = px.bar(df, x='month', y='revenue', title='Fortuna Monthly Revenue')
        st.plotly_chart(fig)

elif page == "Penta Hospitals":
    st.title("Penta Hospitals Patient Distribution")
    df = load_data("penta_hospitals_data.csv")
    if df is not None:
        fig = px.pie(df, names='department', values='patients', title='Patients per Department')
        st.plotly_chart(fig)