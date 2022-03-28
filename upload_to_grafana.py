import requests
import json
import time
from requests.auth import HTTPBasicAuth

filename='coverage.json'

with open(filename) as json_file:
    data = json_file.read()

data = str(data)
ts = time.time_ns()
ts = str(ts)

url = 'https://loki.dev-ue1.icanbwell.com/loki/api/v1/push'
headers = {
    'Content-type': 'application/json'
}
payload = {
  "streams": [
    {
      "stream": {
        "coverage": "results"
      },
      "values": [
          [ ts, data ],
      ]
    }
  ]
}

payload = json.dumps(payload)
response = requests.post(url, data=payload, headers=headers, auth=HTTPBasicAuth('logmon', 'dx6NDRzVgnjLDNyDWmUakjr65r3av4at'))
print(response)
