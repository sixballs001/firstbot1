import requests
from datetime import date

api_url = 'http://api.openweathermap.org/data/2.5/weather'

city = ['Бованенково', 'Харасавэй', 'Новый Уренгой', 'Омск', 'Уфа']
params = {
    "lon": 66.09459643381506,
    "lat": 76.65759641417591,
    'appid': '7747a6d446a3bdf00f403d9b4bf3f207',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers["Content_Type"])
today = date.today()
data = res.json()
print(data)
s = data["main"]["temp"]
n1 =" градусов"
n2 =" градус"
n3 =" градуса"
def gradus(s):
    if -60 <= s <=60:
        if s==0:
            return str(s) + n1
        elif abs(s)%100>=10 and abs(s)%100<=20:
            return str(s) + n1
        elif abs(s)%10==1:
            return str(s) + n2
        elif abs(s)%10>=2 and abs(s)%10<=4:
            return str(s) + n3
        else:
            return str(s) + n1

#print(today)
# print(res.json())# return json.loads(res.text)

template_city2 = 'Сегодня {}  текущая температура  {}. Ощущается как {}  в городе {}.Скорость ветра {} м/с'.format(today,gradus(s),data["main"]["feels_like"], city[2], data["wind"]["speed"])

#template_city = 'Сегодня', today,  'в городе', city, gradus(s), 'Скорость ветра',data["wind"]["speed"], 'м/с'
#template_wind = 'Скорость ветра',data["wind"]["speed"], 'м/с'
# print(template_city2)
#print(template_city + template_wind)
#print(template_wind)
# в файле json папка main содержит параметр temp данные по температуре
# print(template_wind.format(data["wind"]["speed"]))
# print(data["main"]["temp"])
# print(data["wind"]["speed"])
# print(data["name"])