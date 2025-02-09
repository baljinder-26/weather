import streamlit as st
import pandas as pd
import datetime
import requests
import base64

st.set_page_config("Weather Page",page_icon=':sun_small_cloud:')


# data-testid="stApp"
# <<<<<<< Updated upstream
with open('rain.png','rb')as f:
    data=f.read()
imgs=base64.b64encode(data).decode()
# =======
# with open('rain.png','rb')as f:
#     data=f.read()
# imgs=base64.b64encode(data).decode()
# >>>>>>> Stashed changes
# css=f"""
#     <style>
#     [data-testid="stAppViewContainer"]{{
#     background-image:url('data:image/png;base64,{imgs}');
#     background-size:cover
# <<<<<<< Updated upstream

#     }}

#     </style>
# """
video=f"""
   <style>
   .vid{{

       position: fixed;
		  right: 0;
 		  bottom: 0;
       min-width: 100%; 
 		  min-height: 100%;
    
   }}
   </style>
  
  <video autoplay loop muted class="vid"  >
   <source src="https://cdn.discordapp.com/attachments/1294905019388395563/1294907714929033308/4038059-hd_1280_720_30fps.mp4?ex=6780bc49&is=677f6ac9&hm=e96c0d2e6e461087d020bd630b4e0e6b833d9739b127daf3c9ff19407782456c&" type="video/mp4">
   </video>

   """

st.markdown(video,unsafe_allow_html=True)
# =======

#     }}
 
#     </style>
# """
video=f"""
  <style>
  .vid{{
      position: fixed;
		  right: 0;
		  bottom: 0;
      min-width: 100%; 
		  min-height: 100%;
    
  }}
  </style>
  
 <video autoplay loop muted class="vid"  >
 <source src="https://cdn.discordapp.com/attachments/1294905019388395563/1294907714929033308/4038059-hd_1280_720_30fps.mp4?ex=6780bc49&is=677f6ac9&hm=e96c0d2e6e461087d020bd630b4e0e6b833d9739b127daf3c9ff19407782456c&">

  </video>

"""

# st.markdown(css,unsafe_allow_html=True)

st.markdown(video,unsafe_allow_html=True)
st.title("Weather App")
# >>>>>>> Stashed changes

def weather(city):
    API_KEY = "10f1f4d38d1025e47ebc8c84cb6d893f"   #API KEy ABhijay
#     ch=v.split(" ")[1].split(":")[0]
#     st.write(ch)
#   if ch
    if city_name:
        api_address = "https://api.openweathermap.org/data/2.5/forecast?q="+city+"&appid="+API_KEY
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
