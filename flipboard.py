from urlparse import urlparse
from bs4 import BeautifulSoup

import requests
import time
import urllib


class Flipboard:
	_ADD_URI = "https://share.flipboard.com/flipit/load?v=1.0&url={0}&title={1}&device=wbookmarklet&t={2}"
	_LOGIN_URI = "https://share.flipboard.com/u/login"
	_POST_URI = "https://share.flipboard.com/flipit/flipsave"

	_USER_AGENT = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 ' + \
				'(KHTML, like Gecko) Chrome/13.0.782.99 Safari/535.1'

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def get_input_value(self, html, key):
		soup = BeautifulSoup(html)
		tags = soup.find_all('input', attrs={'name' : key})
		csrf = tags[0]['value']
		return csrf

	def get_csrf(self, html):
		return self.get_input_value(html, '_csrf')

	def plus(self, url, title):
		headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': self._USER_AGENT, 'Accept-Encoding': 'gzip, deflate'}

		# get login form
		s = requests.Session()
		response = s.get(self._LOGIN_URI, headers=headers, verify=False)

		csrf = self.get_csrf(response.text)

		# login
		payload = {'_csrf': csrf, 'username': self.username, 'password': self.password}
		response = s.post(self._LOGIN_URI, data=payload, headers=headers, verify=False)

		# get the post form
		uri = self._ADD_URI.format(url, title.encode('utf-8','ignore'), int(time.time()))
		response = s.get(uri, headers=headers, verify=False)

		payload = {}
		payload['_fmt'] = 'JSON'
		payload['_csrf'] = self.get_input_value(response.text, '_csrf')
		payload['target'] = self.get_input_value(response.text, 'target')
		payload['imageIndex'] = '0'
		payload['signedImages'] = self.get_input_value(response.text, 'signedImages')
		payload['previewImage'] = ''
		payload['url'] = url
		payload['flipurl'] = self.get_input_value(response.text, 'flipurl')
		payload['device'] = 'wbookmarklet'
		payload['message'] = ''
		payload['services'] = ''


		# add the document
		headers = {'Content-Type' : 'application/x-www-form-urlencoded', 'Accept-Encoding' : 'gzip,deflate,sdch', 'X-Requested-With' : 'XMLHttpRequest', 'User-Agent': self._USER_AGENT}
		response = s.post(self._POST_URI, data=payload, headers=headers, verify=False)
		status = response.json()
		return status['success']