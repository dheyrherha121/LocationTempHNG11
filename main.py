from fastapi import FastAPI,status
from requests import get
app=FastAPI()

api_key = "43155ad1b40cf402395c590aab20fac1"

@app.get('/api/hello',status_code=status.HTTP_200_OK)
def hello(visitor_name:str):
   #for loction 
    loc= get('https://ipapi.co/json/')
    loc_data=loc.json()
    location=loc_data.get("city")
    client_ip=loc_data.get("ip")

    #for the temp 
    base_url =  "http://api.openweathermap.org/data/2.5/weather/?"
    complete_url=f"{base_url}q={location}&appid={api_key}&units=metric"
    response=get(complete_url).json()
    temp=response['main']['temp']

    return {'client_ip':client_ip,'location':location, 'greeting':f'hello {visitor_name}!,the temperature is {temp} degree Celsius in {location} '}
