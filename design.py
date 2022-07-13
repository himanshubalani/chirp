from ctypes import alignment
from tkinter import *
from tkinter.tix import TEXT
import requests
import config
from datetime import datetime
 
#Initialize Window
 
root =Tk()
root.geometry("400x600") #size of the window by default
root.resizable(1,1) #to make the window size resizable
#title of our window
root.title("Chirp")
 
 
# Functions to fetch and display weather info
city_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
city_value = StringVar()
 
def showWeather():
    #Enter you api key, copies from the OpenWeatherMap dashboard
    api_key =  config.api_key
 
    # Get city name from user from the input field (later in the code)
    city_name=city_value.get()
 
    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json()
 
 
    
 
#as per API documentation, if the cod is 200, it means that weather data was successfully fetched
 
 
    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
 
#-----------Storing the fetched values of weather of a city
 
        temp = str(int(weather_info['main']['temp'] - kelvin))  #converting default kelvin value to Celcius
        feels_like_temp = str(int(weather_info['main']['feels_like'] - kelvin))
        pressure = str(weather_info['main']['pressure'])
        humidity = str(weather_info['main']['humidity'])
        wind_speed = str(weather_info['wind']['speed'] * 3.6)
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = str(weather_info['clouds']['all'])
        description = str(weather_info['weather'][0]['description'])
 
        sunrise_time = str(time_format_for_location(sunrise + timezone))
        sunset_time = str(time_format_for_location(sunset + timezone))
 
#assigning Values to our weather varaibles, to display as output
         
        
        printtemp = Label(root,justify="left", text = 'Temperature (Celsius): '+temp, font = 'arial 12 bold').pack(pady=10)
        printfeelslike = Label(root,justify="left", text = 'Feels like in (Celsius): '+feels_like_temp, font = 'arial 12 bold').pack(pady=10)
        printpress = Label(root,justify="left", text = 'Pressure: '+ pressure +'hPa', font = 'arial 12 bold').pack(pady=10)
        printhumid = Label(root,justify="left", text = 'Humidity: '+humidity+'%', font = 'arial 12 bold').pack(pady=10)
        printsuntime = Label(root,justify="left", text = 'Sunrise at '+sunrise_time+' and Sunset at '+sunset_time, font = 'arial 12 bold').pack(pady=10)
        printcloud = Label(root,justify="left", text = 'Cloud: '+cloudy+'%', font = 'arial 12 bold').pack(pady=10)
        printinfo = Label(root,justify="left", text = 'Info: '+ description, font = 'arial 12 bold').pack(pady=10)
    else:
        printtemp = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
    tfield.pack(INSERT, printtemp,printfeelslike,printpress,printhumid,printsuntime,printcloud,printinfo)   #to insert or send value in our Text Field to display output
 
 
 
# Frontend part of code - Interface
 
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)

tfield = Label()
 
root.mainloop()