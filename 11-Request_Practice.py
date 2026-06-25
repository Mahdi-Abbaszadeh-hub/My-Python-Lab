# Practice one
import requests  # Library for making HTTP requests to fetch data
import json  # Library to parse and manipulate JSON data
import pyttsx3  # Library for Text-to-Speech (TTS) conversion

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Fetch astronomical data from the 7Timer API for specific coordinates
# Parameters include longitude, latitude, and output format (JSON)
r = requests.get(
    "https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0"
)

# Extract the HTTP status code (e.g., 200 for success)
status = r.status_code

# Get the raw response content as a string
detail_request = r.text

# Deserialize the JSON string into a Python dictionary
data = json.loads(r.text)

# Access the specific 'init' key from the API response dictionary
# This typically represents the initialization time of the data
init_time = data["init"]

# Output the extracted value to the console
print(init_time)

# Convert the text data to speech and play the audio output
engine.say(init_time)
engine.runAndWait()  # Block execution until the speech synthesis is finished

# --------------------------------------
