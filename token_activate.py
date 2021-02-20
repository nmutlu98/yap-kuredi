import requests

def get_token():
    url = "https://api.yapikredi.com.tr/auth/oauth/v2/token"
    payload='client_id=l7xx8a0cf976d6e94486bbf23d22a07c9e66&client_secret=b1ff2218904446b08e3e6db4f7da95a6&grant_type=client_credentials&scope=oob'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()["access_token"]

#request from an api example
url = "https://api.yapikredi.com.tr/api/simulationdata/v1/listTestData"

payload = 'client_id=l7xx8a0cf976d6e94486bbf23d22a07c9e66&client_secret=b1ff2218904446b08e3e6db4f7da95a6&grant_type=client_credentials&scope=oob'
headers = {
    'Authorization': 'Bearer 25507e82-90cd-430f-8f3e-373d0a9bb58e',
    'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.request("GET", url, headers=headers, data=payload)



