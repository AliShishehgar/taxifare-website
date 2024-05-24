import streamlit as st
import datetime
from datetime import datetime, date, time
import requests

# page configuration
st.set_page_config(page_title="Taxi Fare Predictor", page_icon="🚖", layout="centered")

#title and subtitle
st.title("Taxi Fare Predictor 🚖")
st.markdown("### Predict the fare of your taxi ride in New York City")

#my code:
with st.form('Insert the following parameters'):
    pickup_dt = st.date_input("Select a date")
    pickup_tm= st.time_input("Select a time")
    datetime_value = datetime.combine(pickup_dt,pickup_tm)
    #datetime_value = st.text_input("date and time",'2013-07-06 17:18:00')
    pickup_lon= st.text_input("pickup longitude", '-73.950655')
    pickup_lat= st.text_input("pickup latitude", '40.783282')
    dropoff_lon= st.text_input("dropoff longitude", '-73.984365')
    dropoff_lat= st.text_input("dropoff latitude", '40.769802')
    num_passengers = st.selectbox("Number of passengers", list(range(1, 11)))

    submitted = st.form_submit_button("Submit")
    if submitted:
        query = {
            'pickup_datetime':datetime_value,
            'pickup_longitude':float(pickup_lon),
            'pickup_latitude': float(pickup_lat),
            'dropoff_longitude':float(dropoff_lon),
            'dropoff_latitude': float(dropoff_lat),
            'passenger_count': int(num_passengers)
        }

query= {"pickup_datetime":datetime_value, "pickup_longitude":float(pickup_lon), "pickup_latitude":float(pickup_lat),
        "dropoff_longitude":float(dropoff_lon)  , "dropoff_latitude":float(dropoff_lat), "passenger_count":int(num_passengers)
       }

url = 'https://taxifare.lewagon.ai/predict'
response= requests.get(url=url, params=query).json()
fare= response["fare"]
st.write(fare)

# Add footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(232, 234, 235, 0.8);
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #333;
    }
    </style>
    <div class="footer">
        Created with ❤️ by Ali
    </div>
    """, unsafe_allow_html=True)
