from tkinter import *
from tkinter import ttk
import requests
from Countrydetails import countries

data = countries.all_countries()
data.countries() 


global cities
cities = ["Anantapur","Chittoor","East Godavari","Ahmedabad","Amreli","Bharuch","Kheda (Nadiad)","Vadodara","Valsad","Surendranagar","Surat","Rajkot","Patan","Navsari","Narmada","Morbi","Mehsana","Junagadh","Jamnagar","Gir Somnath","Dahod","Dang","Devbhoomi Dwarka","Gandhinagar","Botad","Bhavn","Bilaspur","Chamba","Hamirpur","Kangra","Kinnaur","Kullu","Lahaul and Spiti","Mandi","Shimla","Sirmaur","Solan","Una","Bokaro","Chatra","Deoghar","Dhanbad","Dumka","Garhwa","Giridih","Godda","Gumla","Hazaribagh","Jamtara","Khunti","Koderma","Latehar","Lohardaga","Pakur","Palamu","Ramgarh","Ranchi","Sahibganj","Seraikela Kharsawan","Simdega","West Singhbhum","Bagalkot","Bangalore Rural","Bangalore Urban","Belgaum","Bellary","Bidar","Vijayapura","Chamarajanagar","Chikmagalur","Chitradurga","Dakshina Kannada","Davanagere","Dharwad","Gadag","Gulbarga","Hassan","Haveri","Kodagu","Kolar","Koppal","Mandya","Mysore","Raichur","Ramanagara","Shimoga","Tumkur","Udupi","Uttara Kannada","Yadgir","Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode","Malappuram","Palakkad","Pathanamthitta","Thiruvananthapuram","Thrissur","Wayanad","Agar Malwa","Alirajpur","Anuppur","Ashoknagar","Balaghat","Barwani","Betul","Bhind","Bhopal","Burhanpur","Chhatarpur","Chhindwara","Damoh","Datia","Dewas","Dhar","Dindori","Guna","Gwalior","Harda","Hoshangabad","Indore","Jabalpur","Jhabua","Katni","Khandwa","Khargone","Mandla","Mandsaur","Morena","Narsinghpur","Neemuch","Panna","Raisen","Rajgarh","Ratlam","Rewa","Sagar","Satna","Sehore","Seoni","Kota","Sikar","Sirohi","Sri Ganganagar","Tonk","Udaipur","Ajmer","Alwar","Banswara","Baran","Barmer","Bharatpur","Bhilwara","Bikaner","Bundi","Chittorgarh","Churu","Dausa","Dholpur","Dungarpur","Hanumangarh","Jaipur","Jaisalmer","Jalore","Jhalawar","Jhunjhunu","Jodhpur","Karauli","Nagaur","Pali","Pratapgarh","Rajsamand","Sawai Madhopur","Sikar","Sirohi","Sri Ganganagar","Tonk","Udaipur","East Sikkim","North Sikkim","South Sikkim","West Sikkim","Ariyalur","Chengalpattu","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kallakurichi","Kanchipuram","Kanyakumari","Karur","Krishnagiri","Madurai","Mayiladuthurai","Nagapattinam","Namakkal","Nilgiris","Perambalur","Pudukkottai","Ramanathapuram","Ranipet","Salem","Sivaganga","Tenkasi","Thanjavur","Theni","Thoothukudi","Tiruchirappalli","Tirunelveli","Tirupattur","Tiruppur","Tiruvallur","Tiruvannamalai","Vellore","Viluppuram","Virudhunagar","Dhalai","Gomati","Khowai","North Tripura","Sepahijala","South Tripura","Unakoti","West Tripura","Agra","Aligarh","Ambedkar Nagar","Amethi","Amroha","Auraiya","Ayodhya","Azamgarh","Baghpat","Bahraich","Ballia","Balrampur","Banda","Barabanki","Bareilly","Basti","Bhadohi","Bijnor","Budaun","Bulandshahr","Chandauli","Chitrakoot","Deoria","Etah","Etawah","Farrukhab"]

def get_weather():
    city = com.get()
    api_key = '253682c0bd759acfb4255d4aa08c3dd7'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9/5 + 32
        humidity = data['main']['humidity']
        weather_condition = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        country_code = data['sys']['country']
        city_with_country = f"{city}, {country_code}"
        
        # Update the result label with weather information
        result_label.config(text=f"City: {city_with_country}\nTemperature: {temperature_celsius:.2f} °C / {temperature_fahrenheit:.2f} °F\nHumidity: {humidity}%\nWeather Condition: {weather_condition}\nWind Speed: {wind_speed} m/s\nPressure: {pressure} hPa")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error: {e}")
    except KeyError as e:
        result_label.config(text="Error: Data format incorrect, please try again.")

def on_key_release(event):
    value = event.widget.get()
    if value:
        matches = [city for city in cities if value.lower() in city.lower()]
        listbox_update(matches)
    else:
        listbox_update([])

def listbox_update(matches):
    listbox.delete(0, END)
    for match in matches:
        listbox.insert(END, match)

def on_select(event):
    selected_city = listbox.get(ACTIVE)
    com.set(selected_city)
    listbox_update([])

# GUI setup
win = Tk()
win.title("Weather App")
win.config(bg="#f5f5f5")
win.geometry("600x400")

name_label = Label(win, text="Weather App", font=("Helvetica", 30, "bold"), fg="#333", bg="#f5f5f5")
name_label.place(x=200, y=20)

com = ttk.Combobox(win, values=cities, font=("Helvetica", 12))
com.place(x=200, y=80, width=200)
com.bind('<KeyRelease>', on_key_release)

listbox = Listbox(win, font=("Helvetica", 12))
listbox.place(x=200, y=105, width=200, height=100)
listbox.bind('<<ListboxSelect>>', on_select)

done_button = Button(win, text="Get Weather", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=get_weather)
done_button.place(x=250, y=200)

result_label = Label(win, text="", font=("Helvetica", 12), wraplength=500, justify="left", bg="#f5f5f5")
result_label.place(x=50, y=260)

win.mainloop()
