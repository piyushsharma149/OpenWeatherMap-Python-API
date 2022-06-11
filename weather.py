import tkinter as tk
import requests
import time

def getWeather(canvas):
    city_name = textfield.get()
    api2 = "http://api.openweathermap.org/geo/1.0/direct?q=" + city_name +  "&limit=5&appid=79b1195ccd08569c3a2ddc5edeb5fa21"
    json_data1 = requests.get(api2).json
    lat = json_data1['lat']
    lon = json_data1['lon']
   


    api = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=79b1195ccd08569c3a2ddc5edeb5fa21"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data [ 'main']['temp'] - 273.15)
    min_temp = int(json_data [ 'main']['temp'] - 273.15)
    max_temp = int(json_data [ 'main']['temp'] - 273.15)
    pressure = json_data ['main']['pressure']
    wind = json_data ['wind']['speed']
    sunrise = time.strfttime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunrise = time.strfttime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))


    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" +"Min Temp: " + str(min_temp) + "\n" +str(pressure) +"\n"+ "Humidity: "+ str(humidity) + "\n" + "Wind speed :"
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
f = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = f)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = f)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()