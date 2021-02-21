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



#def createData():
#    url = "https://api.yapikredi.com.tr/api/simulationdata/v1/createTestData"
#    response = requests.request("GET", url, headers=headers, data=payload)
#    print(response.text)

#def resetData():
#    url = "https://api.yapikredi.com.tr/api/simulationdata/v1/resetTestData"
#    response = requests.request("GET", url, headers=headers, data=payload)
#    print(response.text)
def listData():
    url = "https://api.yapikredi.com.tr/api/simulationdata/v1/listTestData"
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

def getCustomerList():
    # reads from txt file
    file = open("customerList.txt", "r")
    contents = file.read()
    customerList = ast.literal_eval(contents)
    file.close()
    return customerList["response"]["return"]["customerList"]

def getDatabaseCustomerList():
    customers = []
    id = 9
    for customer in getCustomerList():
        customer_dict = {"customer_id" : str(id),
                         "account_number" : customer["accounts"][0]["accountNumber"],
                         "customer_number" : customer["customerNumber"]}
        customers.append(customer_dict)
        id+=1
        customer_dict  = {}
    return customers

print(getDatabaseCustomerList())

def getAccountTransaction(accNo):
    url = "https://api.yapikredi.com.tr/api/currentAccounts/account/v1/accountTransactionList"
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }
    payload="{\r\n  \"accountNo\": \""+ accNo +"\",\r\n  \"ccy\": \"TL\",\r\n  \"continuousSearch\": \"true\",\r\n  \"descSort\": \"true\",\r\n  \"startDate\": \"2013-10-01\",\r\n  \"endDate\": \"2021-02-21\",\r\n  \"noOfPage\": \"1\",\r\n  \"noOfRecs\": \"5\",\r\n  \"postNo\": \"0\"\r\n}"

    response = requests.request("POST", url, headers=headers,data = payload)
    return response.text

#print(getAccountTransaction())

def getCustomerbyNumber():
    url =  "https://api.yapikredi.com.tr/api/customers/v1/customerInformationByCustomerNumber"


    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }
    payload = "{\"customerNumber\" : \"10704092\"}"

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
#print(getCustomerbyNumber())

def getAccbyNumber(cusNumber):
    for customer in getDatabaseCustomerList():
        if(customer["customer_number"] == cusNumber):
            return customer["account_number"]


def remmitanceFromCustomerNumber(fromCus,toAcc,amount):
    fromAcc = getAccbyNumber(fromCus)
    payload = "{\"clientNo\": \""+ fromCus+ "\", \"amount\": \""+ amount  +"\",\"customExplanation\": \"Hesaba havale\",\"toAccountValue\": \""+toAcc +"\",\"fromAccountValue\": \""+fromAcc+"\"}"
    url = "https://api.yapikredi.com.tr/api/remittance/v1/remittanceToCurrentAccount"
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text



print(remmitanceFromCustomerNumber("10704090","10704732","1"))
print(getAccountTransaction("10704732"))

#accno2 = 10704737

