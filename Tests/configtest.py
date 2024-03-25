import pytest
import json
from selenium import webdriver
import os
import configparser

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, '..', 'Config', 'config.ini')
config_path1 = os.path.join(current_dir, '..', 'Data', 'data.json')
config_path2 = os.path.join(current_dir, '..', 'Data', 'asserationData.json')


@pytest.fixture(params=["chrome"], scope="function")
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        config = read_config()
        if not config or 'BASE_URL' not in config:
            raise ValueError("BASE_URL not found in the config file.")
        base_url = config['BASE_URL']
        print(f"Base URL: {base_url}")
        driver.maximize_window()
        driver.get(base_url)
        yield driver
        driver.quit()


# @pytest.fixture
# def get_api_data():
#     config = read_config()
#     print(config)
#     return {
#         "BASE_URL": config[1].get("API", "BASE_URL"),
#         "api_key": config[1].get("API", "api_key"),
#         "location": config[1].get("API", "location"),
#         "days": config[1].get("API", "days")
#     }


def read_config(ui_path=config_path):
    config = {}
    with open(ui_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key.strip()] = value.strip()
    return config


@pytest.fixture
def login_data():
    # Load data from the JSON file
    with open(config_path1, "r") as file:
        data = json.load(file)
    return data


@pytest.fixture
def assertion_data():
    # Load  assertion data from the JSON file
    with open(config_path2, "r") as file:
        assertionData = json.load(file)
    return assertionData
