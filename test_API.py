import json
import urllib.request as urllib
from pprint import pprint
from credentials import azure_ml_api_key


data = {
    "Inputs": {
        "NRIC, page_id, time_spent": {
            "ColumnNames": ["NRIC", "page_id", "time_spent"],
            "Values": [["S9898467T", "0", "0"], ["S9898467T", "0", "0"],],
        },
    },
    "GlobalParameters": {},
}

body = str.encode(json.dumps(data))

url = "https://ussouthcentral.services.azureml.net/workspaces/49a173e4ed7442fb8716f551a483e358/services/88d9184b914a4a9c800fe44265ae553c/execute?api-version=2.0&details=true"
api_key = azure_ml_api_key  # Replace this with the API key for the web service
headers = {"Content-Type": "application/json", "Authorization": ("Bearer " + api_key)}

req = urllib.Request(url, body, headers)

try:
    response = urllib.urlopen(req)
    result = response.read().decode("utf-8")

    pprint(json.loads(result)["Results"]["Recommendations"]["value"]["Values"])
except urllib.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))
