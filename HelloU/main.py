import requests
import json


def jason_print(object):
    text = json.dumps(object, sort_keys=True, indent=4)
    print(text)


# Astronauts in space
response = requests.get('http://api.open-notify.org/astros.json')
# jason_print(response.json())
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


def print_response(url, parameters):
    response = requests.get(url, params=parameters)
    jason_print(response.json())
    return response


# Data USA population
parameters = {
    'drilldowns': 'Nation',
    'measures': 'Population'
}
url = 'https://datausa.io/api/data'
response = print_response(url, parameters)
population_year = json.loads(response.content)
for year in population_year['data']:
    print(year['ID Year'], ": ", year['Population'])
