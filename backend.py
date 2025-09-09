import requests as re

API_key = '9e27a426337de1eaff7403a1ba63b4c7'

def get_data(place, forecast_days):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}'
    response = re.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data

# if __name__ == '__main__':


# https://api.openweathermap.org/data/2.5/forecast?q=Tokyo&appid=9e27a426337de1eaff7403a1ba63b4c7