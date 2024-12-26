import requests
import json


url = "http://localhost:5000/predict"
# Sample data
data = {
 "CRIM": { "0": 5.82115 },
   "ZN": { "0": 0.0 },
   "INDUS": { "0": 18.1 },
   "CHAS": { "0": 0.0 },
   "NX": { "0": 0.713 },
   "RM": { "0": 6.513 },
   "AGE": { "0": 89.9 },
   "DIS": { "0": 2.8016 },
   "RAD": { "0": 24.0 },
   "TAX": { "0": 666.0 },
   "PTRATIO": { "0": 20.2 },
   "B": { "0": 393.82 },
   "LSTAT": { "0": 10.29 }
}


# Convert to JSON string
input_data = json.dumps(data)


# Set the content type
headers = {"Content-Type": "application/json"}


# Make the request and display the response
# resp = requests.post(url, input_data, headers=headers)
resp = requests.post(url, data=input_data, headers=headers)

print(resp.text)