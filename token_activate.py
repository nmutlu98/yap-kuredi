import ast

import requests



def getToken():
    url = "https://api.yapikredi.com.tr/auth/oauth/v2/token"
    payload = 'client_id=l7xx8a0cf976d6e94486bbf23d22a07c9e66&client_secret=b1ff2218904446b08e3e6db4f7da95a6&grant_type=client_credentials&scope=oob'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()["access_token"]
auth  = "Bearer " + getToken()

payload='client_id=l7xx8a0cf976d6e94486bbf23d22a07c9e66&client_secret=b1ff2218904446b08e3e6db4f7da95a6&grant_type=client_credentials&scope=oob'
headers = {
    'Authorization': auth,
    'Content-Type': 'application/x-www-form-urlencoded'
}

# request from an api example
# url = "https://api.yapikredi.com.tr/api/simulationdata/v1/listTestData"

def getApi(url,token):
    payload = 'client_id=l7xx8a0cf976d6e94486bbf23d22a07c9e66&client_secret=b1ff2218904446b08e3e6db4f7da95a6&grant_type=client_credentials&scope=oob'
    auth = "Bearer " + token
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def createData():
    url = "https://api.yapikredi.com.tr/api/simulationdata/v1/createTestData"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
"""
def resetData():
    url = "https://api.yapikredi.com.tr/api/simulationdata/v1/resetTestData"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
"""

def listData():
    url = "https://api.yapikredi.com.tr/api/simulationdata/v1/listTestData"
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text



def getCustomerList():
    file = open("customerList.txt", "r")
    #ast is imported
    contents = file.read()
    customerList = ast.literal_eval(contents)
    file.close()
    #return listData()

    return customerList["response"]["return"]["customerList"]



def getAccountTransaction():
    url = "https://api.yapikredi.com.tr/api/currentAccounts/account/v1/accountTransactionList"

    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }
    payload = {
    "accountNo": "10704092",
    "ccy": "TL",
    "continuousSearch": "true",
    "descSort": "true",
    "startDate": "2017-10-01",
    "endDate": "2017-11-01",
    "noOfPage": "1",
    "noOfRecs": "5",
    "postNo": "0"}

    response = requests.request("POST", url, headers=headers,data = payload)
    return response.text

print(getAccountTransaction())








