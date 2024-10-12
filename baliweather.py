import streamlit as st
import pandas as pd
import datetime
import requests
import base64

st.set_page_config("Weather Page",page_icon=':sun_small_cloud:')
st.title("Weather App")

# data-testid="stApp"
with open('rain.png','rb')as f:
    data=f.read()
imgs=base64.b64encode(data).decode()
css=f"""
    <style>
    [data-testid="stAppViewContainer"]{{
    background-image:url('data:image/png;base64,{imgs}');
    background-size:cover

    }}

    </style>
"""
# video=f"""
#   <style>
#   .vid{{

#       position: fixed;
# 		  right: 0;
# 		  bottom: 0;
#       min-width: 100%; 
# 		  min-height: 100%;
    
#   }}
#   </style>
  
#  <video autoplay loop muted class="vid"  >
#   <source src="" type="video/mp4">
#   </video>

# """

# st.markdown(video,unsafe_allow_html=True)

def weather(city):
    API_KEY = "10f1f4d38d1025e47ebc8c84cb6d893f"   #API KEy ABhijay
#     ch=v.split(" ")[1].split(":")[0]
#     st.write(ch)
#   if ch
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
             ch=int(v.split(" ")[1].split(":")[0])
             st.write(ch)
            #  if ch>=6 and ch<=18:
            #      day.append(ch)
            #  else:
            #      night.append(ch)
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
# st.write(day)
# st.write(night)
