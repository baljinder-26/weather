import streamlit as st
import pandas as pd
import datetime
import requests

st.set_page_config("Weather Page",page_icon=':sun_small_cloud:')
st.title("Weather App")
def weather(city):
    API_KEY = "10f1f4d38d1025e47ebc8c84cb6d893f"   #API KEy ABhijay
    
    if city_name:
        api_address = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + API_KEY
        try:
          res = requests.get(api_address)
          a = res.json()
          # st.write(a)
          st.header(f"Hourly Weather of city {a["city"]["name"]}")
          for i in a["list"]:
             st.subheader(i["dt_txt"])
             v=i["dt_txt"]
             day=pd.to_datetime(v).day_name()
             st.write(f":blue[{day}]")
             col1,col2=st.columns([1,1])
             with col1:
                if i["weather"][0]['description']=='light rain':
                      st.image('rain.png', width=100)
                else:
                      st.image('cloud.png', width=100)
             with col2: 
                    st.write(f":blue[Description] {i['weather'][0]['description']}")
                            
                    st.write(f":blue[Temperature]  {i['main']['temp']-273}° C")
                    st.write(f":Wind Speed  {i['wind']['speed']}km/hr")   

             
        except Exception as e:
           st.write("Exception is - ",e)
        

city_name=st.text_input("Enter city name")
weather(city_name)
