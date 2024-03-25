import pytest
import requests
from Tests.configtest import api_data_fixture, auth_token, created_booking_id,api_config_from_ini,logger_setup
import logging
import allure
@pytest.mark.usefixtures("created_booking_id","auth_token","api_config_from_ini","api_data_fixture","logger_setup")
class TestAPITest:
    @pytest.mark.run(order=7)
    @allure.feature('Getting all booking data')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_all_bookings(self, api_data_fixture, auth_token, api_config_from_ini):
        allure.attach('Starting test_get_all_bookings', attachment_type=allure.attachment_type.TEXT); logging.info("Starting test_get_all_bookings")
        api_config = api_config_from_ini
        allure.attach('Fetching bookings from API', attachment_type=allure.attachment_type.TEXT);logging.debug("Fetching bookings from API")
        response = requests.get(api_config['api_url'] + api_config['booking_base_end_point'], headers={'Cookie': 'token=' + auth_token})
        assert response.status_code == 200, f"Failed to get all bookings. Status code: {response.status_code}"
        data = response.json()
        assert any("bookingid" in item for item in data), "No bookings found"
        allure.attach('Bookings fetched successfully', attachment_type=allure.attachment_type.TEXT);logging.debug("Bookings fetched successfully")
        allure.attach('Ending test_get_all_bookings', attachment_type=allure.attachment_type.TEXT);logging.info("Ending test_get_all_bookings")

    # Test case to create a new booking
    @pytest.mark.run(order=8)
    @allure.feature('Creating booking data')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_booking(self, api_data_fixture, auth_token, api_config_from_ini):
        allure.attach('Starting test_create_booking', attachment_type=allure.attachment_type.TEXT); logging.info("Starting test_create_booking")
        assert auth_token is not None, "Authentication token not obtained"
        api_config = api_config_from_ini
        allure.attach('ending request to create a booking', attachment_type=allure.attachment_type.TEXT);logging.debug("Sending request to create a booking")
        response = requests.post(api_config['api_url'] + api_config['booking_base_end_point'],json=api_data_fixture.get("booking_data", {}),headers={'Cookie': 'token=' + auth_token})
        assert response.status_code == 200, f"Failed to create booking. Status code: {response.status_code}"
        booking_id = response.json().get("bookingid", '')
        allure.attach('Retrieving created booking for validation', attachment_type=allure.attachment_type.TEXT);logging.debug("Retrieving created booking for validation")
        response = requests.get(api_config['api_url'] +'/' + api_config['booking_detail_end_point'].format(bookingid=booking_id))
        assert response.status_code == 200, f"Failed to retrieve created booking. Status code: {response.status_code}"
        assert response.json() == api_data_fixture.get("booking_data", {}), "Created booking data does not match"
        allure.attach('Ending test_create_booking', attachment_type=allure.attachment_type.TEXT);logging.info("Ending test_create_booking")

 # Test case to update a booking
    @pytest.mark.run(order=9)
    @allure.feature('Updating booking data')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_booking(self, api_data_fixture, auth_token, created_booking_id,api_config_from_ini):
        allure.attach('Starting test_update_booking', attachment_type=allure.attachment_type.TEXT);logging.info("Starting test_update_booking")
        assert api_data_fixture is not None, "API data fixture is None"
        assert auth_token is not None, "Authentication token not obtained"
        assert created_booking_id is not None, "Created booking ID is None"
        api_config = api_config_from_ini
        updated_data = api_data_fixture.get("updated_booking_data", {})
        allure.attach('Preparing data for updating booking', attachment_type=allure.attachment_type.TEXT);logging.debug("Preparing data for updating booking")
        response = requests.put(api_config['api_url'] +'/' + api_config['booking_detail_end_point'].format(bookingid=created_booking_id), json=updated_data, headers={'Cookie': 'token=' + auth_token})
        allure.attach('Sending request to update booking', attachment_type=allure.attachment_type.TEXT);logging.debug("Sending request to update booking")
        assert response.status_code == 200, f"Failed to update booking. Status code: {response.status_code}"
        assert response.json().get("firstname") == updated_data.get("firstname"), "First name not updated"
        assert response.json().get("lastname") == updated_data.get("lastname"), "Last name not updated"
        allure.attach('Booking updated successfully', attachment_type=allure.attachment_type.TEXT);logging.info("Booking updated successfully")
        allure.attach('Ending test_update_booking', attachment_type=allure.attachment_type.TEXT); logging.info("Ending test_update_booking")



 # Test case to patch a booking
    @pytest.mark.run(order=10)
    @allure.feature('Patching booking details')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_patch_booking(self, api_data_fixture, auth_token, created_booking_id, api_config_from_ini):
        allure.attach('Starting test_patch_booking', attachment_type=allure.attachment_type.TEXT);logging.info("Starting test_patch_booking")
        assert api_data_fixture is not None, "API data fixture is None"
        assert auth_token is not None, "Authentication token not obtained"
        assert created_booking_id is not None, "Created booking ID is None"
        patch_data = api_data_fixture.get("patch_data", {})
        api_config = api_config_from_ini
        allure.attach('Sending request to patch booking', attachment_type=allure.attachment_type.TEXT);logging.debug("Sending request to patch booking")
        response = requests.post(api_config['api_url']  + api_config['booking_base_end_point'], json=api_data_fixture.get("booking_data", {}), headers={'Cookie': 'token=' + auth_token})
        assert response.status_code == 200, f"Failed to patch booking. Status code: {response.status_code}"
        allure.attach('Booking patched successfully', attachment_type=allure.attachment_type.TEXT);logging.info("Booking patched successfully")

    # Test case to delete a booking
    @pytest.mark.run(order=11)
    @allure.feature('Deleting booking data')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_booking(self, api_data_fixture, auth_token, created_booking_id,api_config_from_ini):
        allure.attach('Starting test_delete_booking', attachment_type=allure.attachment_type.TEXT)
        logging.info("Starting test_delete_booking")
        assert api_data_fixture is not None, "API data fixture is None"
        assert auth_token is not None, "Authentication token not obtained"
        assert created_booking_id is not None, "Created booking ID is None"
        api_config = api_config_from_ini
        allure.attach('Sending request to delete booking', attachment_type=allure.attachment_type.TEXT);logging.debug("Sending request to delete booking")
        response = requests.delete(api_config.get('api_url', '')  +'/' + api_config['booking_detail_end_point'].format(bookingid=created_booking_id), headers={'Cookie': 'token=' + auth_token, 'Content-Type': 'application/json'})
        assert response.status_code == 201, f"Failed to delete booking. Status code: {response.status_code}"
        logging.info("Booking deleted successfully")
        allure.attach('Sending request to delete booking', attachment_type=allure.attachment_type.TEXT)
