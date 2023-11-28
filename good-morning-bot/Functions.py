import requests
import random, time
import pandas as pd                        
from pytrends.request import TrendReq
import billboard


# takes current hour as input
# returns appropriate part of day for greeting
def getPartOfDay(h):
    return (
        "Morning"
        if 5 <= h <= 11
        else "Afternoon"
        if 12 <= h <= 17
        else "Evening"
        if 18 <= h <= 22
        else "Night"
    )

# returns one of today's wacky holidays 
# BROKEN as of Jan 2022
# This API no longer exists.
def getHoliday():
    try:
        res = requests.get('https://national-api-day.herokuapp.com/api/today')
        if res.status_code == 200:
            day = (res.json()['holidays'][random.randrange(0,10,1)])
        else :
            day = f"Error retrieving wacky holiday. Status code {res.status_code}"
        return day
    except:
        return("Something went wrong! Try Again!")

# returns a random quote (from API linked)
def getQuote():
	try:
		res = requests.get("https://api.api-ninjas.com/v1/quotes?category=happiness", headers={'X-Api-Key': '1gjR5rGAprLRdLJvZQgvtg==qrwhLBmpYDcFiAWK'})
		if res.status_code == 200:
			return(f'"{res.json()[0]["quote"]}"\n- {res.json()[0]["author"]}')
		else:
			return(f"Error retrieving quote. Status code {res.status_code}")
	except:
		return(f"Something went wrong! Try Again!.")

# returns weather data as a readable string (from API linked)
def getWeather():
    try:
        res = requests.get('http://api.weatherapi.com/v1/current.json?key=2083c355a3ec413ca48202829222603&q=auto:ip&aqi=no')
        if res.status_code == 200:
            data = parseWeather(res)
        else :
            data = f"Error retrieving weather data. Status code {res.status_code}"
        return data
    except:
        return("Something went wrong! Try Again!")

# takes in raw weather data 
# parses and returns as readable string
def parseWeather(res):
    #print(res.text)
    name = res.json()['location']['name']    
    data = "Your weather report for " + name + " is ready!\n"
    time.sleep(1)

    skies = res.json()['current']['condition']['text']    
    data += "The forecast is " + skies + " today, "
    
    wind = res.json()['current']['wind_mph']
    if(wind >= 5.0 and wind < 15.0):
        data += "with a gentle breeze. "
    elif(wind >= 15.0 and wind < 25.0):
        data += "with some wind. "
    elif(wind >= 25.0):
        data += "with strong winds. "
    else:
        data += "with very little wind. "
    
    time.sleep(1)

    temp = int(res.json()['current']['temp_f'])
    data += "The temperature right now is " + str(temp) + u'\N{DEGREE SIGN}' + "F"

    return data


# returns a random cat fact (from API linked)
def getCatFact():
    try:
        res = requests.get('https://catfact.ninja/fact?max_length=140')    
        if res.status_code == 200:
            fact = (res.json()['fact'])
        else :
            fact = f"Error retrieving cat fact. Status code {res.status_code}"
        return fact
    except:
        return("Something went wrong! Try Again!")

# uses Google trends API for python (pytrends)
# returns top 3 Google searches of the day
def getSearchTrends():
    pytrend = TrendReq()
    df = pytrend.trending_searches(pn='united_states')
    df.head()
    return df

# returns top 100 songs (from billboard API)
def getTopSongs():
    return billboard.ChartData('hot-100')

