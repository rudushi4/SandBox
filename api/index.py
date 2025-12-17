from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class BillingDetails(BaseModel):
    city: str
    country: str
    line1: str
    line2: str | None = None
    postal_code: str
    state: str
    firstName: str
    lastName: str
    email: str
    phoneNumber: str

class SessionInfo(BaseModel):
    crumb: str
    ss_cvr: str
    ss_cvt: str
    ga: str
    fbp: str
    cart: str
    has_cart: str
    ga_dexes2kd6e: str
    stripe_mid: str
    stripe_sid: str
    csrf_token: str

class PaymentInfo(BaseModel):
    card_number: str
    exp_month: str
    exp_year: str
    cvv: str
    amount: str
    billing_details: BillingDetails
    session_info: SessionInfo

@app.post("/api/process_payment")
def process_payment(payment_info: PaymentInfo):
    cc = payment_info.card_number
    mm = payment_info.exp_month
    yy = payment_info.exp_year
    cvv = payment_info.cvv
    amount = payment_info.amount
    billing_details = payment_info.billing_details
    session_info = payment_info.session_info

    stripe_key = os.environ.get("STRIPE_KEY")
    stripe_account = os.environ.get("STRIPE_ACCOUNT")
    hcaptcha_token = os.environ.get("HCAPTCHA_TOKEN")

    if not all([stripe_key, stripe_account, hcaptcha_token]):
        return {"error": "Missing required environment variables"}

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

    data = {
        'billing_details[address][city]': billing_details.city,
        'billing_details[address][country]': billing_details.country,
        'billing_details[address][line1]': billing_details.line1,
        'billing_details[address][line2]': billing_details.line2 or "",
        'billing_details[address][postal_code]': billing_details.postal_code,
        'billing_details[address][state]': billing_details.state,
        'billing_details[name]': f"{billing_details.firstName} {billing_details.lastName}",
        'billing_details[email]': billing_details.email,
        'type': 'card',
        'card[number]': cc,
        'card[cvc]': cvv,
        'card[exp_year]': yy,
        'card[exp_month]': mm,
        'allow_redisplay': 'unspecified',
        'payment_user_agent': 'stripe.js/4901af2b6b; stripe-js-v3/4901af2b6b; payment-element; deferred-intent',
        'referrer': 'https://www.choseizen.org',
        'time_on_page': '66308',
        'client_attribution_metadata[client_session_id]': 'd8769de2-7599-45af-b6e2-a8c55e90ba0f',
        'client_attribution_metadata[merchant_integration_source]': 'elements',
        'client_attribution_metadata[merchant_integration_subtype]': 'payment-element',
        'client_attribution_metadata[merchant_integration_version]': '2021',
        'client_attribution_metadata[payment_intent_creation_flow]': 'deferred',
        'client_attribution_metadata[payment_method_selection_flow]': 'merchant_specified',
        'guid': '93494dcf-adcd-4631-a465-c81054a6e5e1ccf186',
        'muid': '2a502e2b-5e33-4dc4-bf34-347d3459a4ac3b370b',
        'sid': '4b14cf60-714e-4224-afa1-bfa7e4354ea49f8342',
        'key': stripe_key,
        '_stripe_account': stripe_account,
        'radar_options[hcaptcha_token]': hcaptcha_token,
    }

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    if response.status_code != 200:
        return {"error": "Failed to create payment method", "details": response.json()}

    payment_method_id = response.json().get('id')

    if not payment_method_id:
        return {"error": "Payment method ID not found in response", "details": response.json()}

    cookies = {
        'crumb': session_info.crumb,
        'ss_cvr': session_info.ss_cvr,
        'ss_cvt': session_info.ss_cvt,
        '_ga': session_info.ga,
        '_fbp': session_info.fbp,
        'CART': session_info.cart,
        'hasCart': session_info.has_cart,
        '_ga_DEXES2KD6E': session_info.ga_dexes2kd6e,
        '__stripe_mid': session_info.stripe_mid,
        '__stripe_sid': session_info.stripe_sid,
    }

    headers = {
        'authority': 'www.choseizen.org',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.choseizen.org',
        'referer': f'https://www.choseizen.org/checkout?cartToken={session_info.cart}',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
        'x-csrf-token': session_info.csrf_token,
    }

    json_data = {
        'email': billing_details.email,
        'subscribeToList': False,
        'shippingAddress': {
            'id': '',
            'firstName': billing_details.firstName,
            'lastName': billing_details.lastName,
            'line1': billing_details.line1,
            'line2': billing_details.line2 or '',
            'city': billing_details.city,
            'region': billing_details.state,
            'postalCode': billing_details.postal_code,
            'country': billing_details.country,
            'phoneNumber': billing_details.phoneNumber,
        },
        'createNewUser': False,
        'newUserPassword': None,
        'saveShippingAddress': False,
        'makeDefaultShippingAddress': False,
        'customFormData': None,
        'shippingAddressId': None,
        'proposedAmountDue': {
            'decimalValue': amount,
            'currencyCode': 'USD',
        },
        'cartToken': session_info.cart,
        'paymentToken': {
            'stripePaymentTokenType': 'PAYMENT_METHOD_ID',
            'token': payment_method_id,
            'type': 'STRIPE',
        },
        'billToShippingAddress': True,
        'billingAddress': {
            'id': '',
            'firstName': billing_details.firstName,
            'lastName': billing_details.lastName,
            'line1': billing_details.line1,
            'line2': billing_details.line2 or '',
            'city': billing_details.city,
            'region': billing_details.state,
            'postalCode': billing_details.postal_code,
            'country': billing_details.country,
            'phoneNumber': billing_details.phoneNumber,
        },
        'savePaymentInfo': False,
        'makeDefaultPayment': False,
        'paymentCardId': None,
        'universalPaymentElementEnabled': True,
    }

    response = requests.post('https://www.choseizen.org/api/2/commerce/orders', cookies=cookies, headers=headers, json=json_data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to process payment", "details": response.json()}
