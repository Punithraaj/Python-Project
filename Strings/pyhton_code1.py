import requests
import time
from datetime import datetime
def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()

def main():
    f = open('output.txt', 'w')
    while True:
        location = input('Enter location: ')
        if location == 'EXIT' or location == 'Exit' or location == 'exit':
            f.write('')
            f.close()
            return
        api_key = '2b92ac90c161a8b52a86175509113de9'
        weather = get_weather(api_key, location)
        try:
            prediction = weather['list']
            f.write('location: ' + location + '\n \n')
            for day in prediction:
                s = '%-40s%.2f' % (str(datetime.fromtimestamp(day['dt'])), day['main']['temp'])
                f.write(s+'\n')
                print(s)
        except:
            print("Location not Found")
            print("Please provide the Correct Location to get the Weather Prediction")

main()