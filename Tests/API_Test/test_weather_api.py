# import requests
# from Tests.configtest import get_api_data
#
#
# def test_get_current_weather(get_api_data):
#     base_url = get_api_data["BASE_URL"]
#     api_key = get_api_data["api_key"]
#     location = get_api_data["location"]
#     url = f"{base_url}/v1/current.json?q={location}&key={api_key}"
#     response = requests.get(url)
#     current = response.json()
#     print(current["location"]["name"])
#     print(response.json())
#     assert current["location"]["name"] == location
#     assert response.status_code == 200
#
#
# def test_get_forcast(get_api_data):
#     base_url = get_api_data["BASE_URL"]
#     api_key = get_api_data["api_key"]
#     location = get_api_data["location"]
#     days = get_api_data["days"]
#     url = f"{base_url}/v1/forecast.json?q={location}&days={days}&key={api_key}"
#     response = requests.get(url)
#     forecast = response.json()
#     assert forecast["location"]["name"] == location
#     assert response.status_code == 200
