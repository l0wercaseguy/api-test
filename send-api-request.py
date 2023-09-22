import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
    Result of this API request:
    
        response status code: 201
        response reason: Created

        response text:
        {
            "outcome": "success",
            "lead": {
                "id": "650de324f53035d7b74436cc"
            },
            "price": 0
        }
"""

url = f'https://app.leadconduit.com/flows/64f88c209fdcbc91ead79a18/sources/64f88bb312e29022f8da4df2/submit'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'first_name': 'Daryle',
    'last_name': 'Bowles',
    'email': 'darylebowles@gmail.com',
    'repo_url': 'https://github.com/l0wercaseguy/api-test'
}

response = requests.post(url, headers=headers, data=data, verify=False)

print(f"\nresponse status code: {response.status_code}")
print(f"\nresponse reason: {response.reason}\n")
print(f"response text:\n{json.dumps(json.loads(response.text), indent=4)}")

