import joblib

import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('uber.csv')
model = joblib.load("model.pkl")

st.set_page_config("Best Website Ever!", layout='wide')

def predict(distance, year):
    pred = model.predict([[distance, year]])
    plots(round(pred[0], 2))

def home_page():
    # Display text

    st.title("Epsilon Deployment!")
    st.header("This is a header")
    st.subheader("This is a subheader")

    st.markdown("**This is written using markdown**")
    st.markdown("This is normal markdown")

    st.caption("This is a caption")
    st.code("import requests\nrequests.post(<URL>, json={<DATA>})")


    st.markdown("<a href=\"https://www.google.com\">Click me!</a>", unsafe_allow_html=True)

    # Display media
    st.image("https://d3544la1u8djza.cloudfront.net/APHI/Blog/2021/07-06/small+white+fluffy+dog+smiling+at+the+camera+in+close-up-min.jpg", width=200)

    # st.audio()
    # st.video()

    # Dataframes

    df = pd.DataFrame({"Area":[100, 150, 200], "Finishing":["Not finished", "Semi-finished", "Finished"], "Price":[1000, 1400, 2200]})

    st.dataframe(df)

def inputs():
    # Inputs
    st.title("Predict")
    
    distance = st.number_input("Distance")
    year = st.number_input("Year")
    
    st.button("Predict", on_click=predict, args=(distance, year))
    
    #     st.date_input("Built Year")

    #     st.checkbox("Furnished")
    #     st.checkbox("Amenities")

    #     st.radio("Finishing", ['Finishing 1', 'Finishing 2', 'Finishing 3'])
    #     st.select_slider("Another Finishing", ['Finishing 1', 'Finishing 2', 'Finishing 3'])
    #     st.selectbox("Yet Another Finishing", ['Finishing 1', 'Finishing 2', 'Finishing 3'])

    #     st.slider("Price", 1000,10000)

def plots(result=0):
    # Plotting
    st.title("Result")
    
    st.markdown(f"Estimated Fare: **{result}**")
    
    fig = plt.figure()
    sns.histplot(df, x='fare_amount')
    
    st.pyplot(fig)

    st.button("Make Another Prediction", on_click=inputs)
    
    #     st.header("Matplotlib (Seaborn)")
    #     df = sns.load_dataset("penguins")

    #     fig = plt.figure(figsize=(4,4))
    #     sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species')

    #     st.pyplot(fig)

    #     st.header("Plotly")

    #     st.caption("Using Plotly")
    #     fig = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='species')
    #     st.plotly_chart(fig)

    #     st.caption("Using Streamlit")
    #     st.scatter_chart(df, x='bill_length_mm', y='bill_depth_mm', color='species')


page = st.sidebar.selectbox("Select page", ["Home", "Predict", "Plots"])

if page == 'Home':
    home_page()
elif page == 'Predict':
    inputs()
else:
    plots()


















