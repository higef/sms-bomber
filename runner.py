import random
import re
import textwrap
import requests
import time
from stem import Signal
from stem.control import Controller
import socks, socket


def call_me(num):
	controller.signal(Signal.NEWNYM)
	time.sleep(controller.get_newnym_wait())
	current_ip = requests.get(url='http://icanhazip.com/')
	print(f"Sending to {num} from IP: {current_ip.text}")

	session.head('http://ossinfo.ru/otpravit-sms-na-mts.html')
	response = session.post(
		url='http://ossinfo.ru/functions/custom.php',
		data={
			"method": "sendSms",
			"params[message]": "Vashy voiny ubivaiut mirnoe naselenie v Ukraine",
			"params[number]": f"+{num}",
			"params[transliterate]": "false"
		},
		headers={
			"Referer": 'http://ossinfo.ru/otpravit-sms-na-mts.html',
			"X-Requested-With": "XMLHttpRequest"
		}
	)
	print(response.text)


with Controller.from_port(port=9051) as controller:
	controller.authenticate(password='')
	socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
	socket.socket = socks.socksocket
	session = requests.Session()

	while True:
		with open('phones_pikabu.txt', 'r') as file:
			lines = file.readlines() 
			random_line = random.choice(lines) if lines else None
			num = re.sub('\D', '', random_line)
			if len(num) == 11:
				call_me(num)
			elif len(num) % 11 == 0:
				for n in textwrap.wrap(num, 11):
					call_me(num)

