from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import geopy.distance


class LocationComparison:
    def __init__(self, driver):
        self.driver = driver

    def get_expected_location(self):
        # Retrieve expected location from the webpage
        expected_location_element = self.driver.find_element_by_id("expectedLocation")
        expected_location_text = expected_location_element.text
        # Extract latitude and longitude from the text
        expected_latitude, expected_longitude = map(float, expected_location_text.split(": ")[1].split(", "))
        return expected_latitude, expected_longitude

    def get_user_location(self):
        # Retrieve the user's current location using JavaScript
        user_latitude = self.driver.execute_script(
            "return navigator.geolocation.getCurrentPosition(function(position) {return position.coords.latitude});")
        user_longitude = self.driver.execute_script(
            "return navigator.geolocation.getCurrentPosition(function(position) {return position.coords.longitude});")
        return user_latitude, user_longitude

    def calculate_distance(self, user_latitude, user_longitude, expected_latitude, expected_longitude):
        # Calculate the distance between two points using geopy.distance
        user_location = (user_latitude, user_longitude)
        expected_location = (expected_latitude, expected_longitude)
        distance = geopy.distance.geodesic(user_location, expected_location).kilometers
        return distance

    def compare_location(self):
        # Get the expected location from the webpage
        expected_latitude, expected_longitude = self.get_expected_location()

        # Get the user's current location
        user_latitude, user_longitude = self.get_user_location()

        # Calculate the distance between the user's location and the expected location
        distance = self.calculate_distance(user_latitude, user_longitude, expected_latitude, expected_longitude)

        # Determine if the distance is within a threshold (e.g., 1 kilometer)
        threshold = 1  # You can adjust this threshold as needed
        if distance <= threshold:
            print("You are in the expected location.")
        else:
            print("You are not in the expected location.")


# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the webpage
url = "file:///path/to/your/page.html"  # Replace with the URL of your target webpage
driver.get(url)

# Create an instance of the LocationComparison class
location_comparison = LocationComparison(driver)

# Call the compare_location method to compare the user's location with the expected location
location_comparison.compare_location()

# Close the WebDriver
driver.quit()
