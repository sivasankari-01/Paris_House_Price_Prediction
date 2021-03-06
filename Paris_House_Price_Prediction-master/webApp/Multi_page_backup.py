import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st

HOME_MENU = "Home"
PREDICT_MENU = "Predict"
url = "http://127.0.0.1:8000/prediction"

st.title("House Price Prediction Model")


def show_form():
    with st.form("my_form"):
        size = st.number_input(label="Size", step=1)
        nb_rooms = st.number_input(label="no of rooms", step=1)
        garden = st.radio(
            "Do you want garden?",
            ("Yes", "No"))

        genre = st.radio(
            "Which part of city?",
            ('Est', 'Nord', 'Ouest', 'Sud'))
        submitted = st.form_submit_button("Submit")
        if submitted:
            r = requests.post(url, json={"size": size,
                                         "nb_rooms": nb_rooms,
                                         "garden": garden,
                                         "locations": genre})
            st.write(r.text)


def display_home():
    with st.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("House price in Location Est with Garden", "350000", "-0.5%")
        col2.metric("Active buyers last Month Vs Current Month", "123", "186")
        col3.metric("Profitability after buying house", "2%", "4%")
    st.write('Which kind of house, you would like to buy !')

    df = pd.read_csv("./data/house.csv")
    fig1 = plt.figure()
    plt.scatter(df['size'], df['price'])
    st.pyplot(fig1)
    st.write("THe dataFrame used for House Price Prediction")
    st.write(df)


# Create a side bar
if 'page' not in st.session_state:
    st.session_state['page'] = HOME_MENU
if st.session_state['page'] == HOME_MENU:
    display_home()

if st.session_state['page'] == PREDICT_MENU:
    show_form()


def change_menu(v):
    print(v, v not in st.session_state['page'])
    if v not in st.session_state['page']:
        st.session_state['page'] = v


st.sidebar.button('Home', on_click=change_menu, args=(HOME_MENU,))
st.sidebar.button('Predict', on_click=change_menu, args=(PREDICT_MENU,))
