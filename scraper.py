import requests
from bs4 import BeautifulSoup

temperatures=[]
def convertFtoC(fahrenheit):
    fahrenheit = fahrenheit.split('\\xa')
    fahrenheit = fahrenheit[0].split('\'')
    if fahrenheit[1] == 'N/A':
        return 'N/A'
    fahrenheit = int(fahrenheit[1])
    # print(fahrenheit)
    celsius = (fahrenheit-32)*5/9
    return str(round(celsius,2))+' °C'

def sendTemperatures():
    temperatures = []
    source = requests.get('https://www.timeanddate.com/weather/?low=4').text
    soup = BeautifulSoup(source, 'lxml')
    output = soup.find_all('table', class_='zebra fw tb-theme')
    tr = output[0].find_all('tr')[1:]
    for x in tr:
        td=x.find_all('td')
        if td[0].a != None:
            capital = td[0].text
            time = td[1].text
            fahrenheit = td[3].text
            celsius=convertFtoC(repr(fahrenheit))
            temperature = {
                'capital': capital,
                'time': time,
                'fahrenheit':fahrenheit,
                'celsius': celsius
            }
            temperatures.append(temperature)
            # print(capital,time,temperature,celsius,end="--")

        if td[4].a != None:
            capital = td[4].a.text
            time = td[5].text
            fahrenheit = td[7].text
            celsius = convertFtoC(repr(fahrenheit))
            temperature = {
                'capital': capital,
                'time': time,
                'fahrenheit': fahrenheit,
                'celsius': celsius
            }
            temperatures.append(temperature)
            # print(capital,time,temperature,celsius,end="--")

        # if td[8].a != None:
        #     capital = td[8].a.text
        #     time = td[9].text
        #     fahrenheit = td[11].text
        #     celsius = convertFtoC(repr(fahrenheit))
        #     temperature = {
        #         'capital': capital,
        #         'time': time,
        #         'fahrenheit': fahrenheit,
        #         'celsius': celsius
        #     }
        #     temperatures.append(temperature)
        #     # print(capital, time, temperature, celsius,end="--")

    temperatures.sort(key=lambda x:x['capital'])
    return temperatures

if __name__=='__main__':
    for temperature in sendTemperatures():
        print(temperature['capital'],temperature['time'],temperature['fahrenheit'],temperature['celsius'])