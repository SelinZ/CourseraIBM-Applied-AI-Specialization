"""Once you have the URL for the API, you can use it in your Python code with the requests library to make HTTP requests and retrieve data from the API.
For example, to retrieve data from the FishWatch API, you can use the following code:"""

# Import the requests and json modules for making HTTP requests and handling JSON data, respectively.
import requests
import json
# Specify the URL of the API endpoint for retrieving information about fish species.
url = "https://www.fishwatch.gov/api/species"
# Make an HTTP GET request to the specified URL and store the response in the data variable.
data = requests.get(url)
# Parse the JSON data received from the API response using json.loads() and store it in the results variable.
results = json.loads(data.text)