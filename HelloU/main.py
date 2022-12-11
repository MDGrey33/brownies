import requests
import json

# Cat facts API
response = requests.get("https://catfact.ninja/fact")
if response.status_code == 200:
    cat_facts = json.loads(response.content)
    print(cat_facts['fact'])
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

print('\n')

# Bitcoin price API
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
if response.status_code == 200:
    bitcoin_price = json.loads(response.content)
    print(f'bitcoin price on ' + (bitcoin_price['time']['updated']) + ' is ' + str(bitcoin_price['bpi']['EUR']['rate_float']) + ' EUR')
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

print('\n')

# Astronauts in space
response = requests.get('http://api.open-notify.org/astros.json')
if response.status_code == 200:
    astronauts_in_space = json.loads(response.content)
    print('The astronauts in space at this point are:')
    for astronaut in astronauts_in_space['people']:
        print(astronaut['name'] + ' traveled in ' + astronaut['craft'])
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

print('\n')

# Agify the name
name = input('write a name and we will tell you their approximate age')

url_age = 'https://api.agify.io?name=' + name
response = requests.get(url_age)
if response.status_code == 200:
    agify = json.loads(response.content)
    print(agify['age'])
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

url_gender = 'https://api.genderize.io?name=' + name
response = requests.get(url_gender)
if response.status_code == 200:
    genderize = json.loads(response.content)
    print(genderize['gender'])
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

url_nationality = 'https://api.nationalize.io?name=' + name
response = requests.get(url_nationality)
if response.status_code == 200:
    nationalizeize = json.loads(response.content)
    for country in nationalizeize['country']:
        print('Country: ' + country['country_id'] + ' Probability: ' + str(country['probability']))
else:
    print('Something went wrong')
    print(response.status_code)
    print(response)

print('\n')

