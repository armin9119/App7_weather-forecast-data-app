import requests as re

API_key = '9e27a426337de1eaff7403a1ba63b4c7'

def get_data(place, forecast_days, kind):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}'
    response = re.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]

    return filtered_data

if __name__ == '__main__':
    print(get_data('Tokyo', 3, 'Temperature'))

# https://api.openweathermap.org/data/2.5/forecast?q=Tokyo&appid=9e27a426337de1eaff7403a1ba63b4c7