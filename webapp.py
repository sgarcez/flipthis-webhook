from flask import Flask
from flask import request

from flipboard import Flipboard

import os



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	# http://stackoverflow.com/questions/15327776/python-django-avoid-saving-passwords-in-source-code
	FB_USERNAME = os.environ.get("FLIPBOARD_USERNAME", '')
	FB_PASSWORD = os.environ.get("FLIPBOARD_PASSWORD", '')

	f = Flipboard(FB_USERNAME, FB_PASSWORD)
	url = request.args['url']
	title = request.args['title']
	success = f.plus(url, title)
	return url + "=" + ('OK' if success else 'FAILED')

if __name__ == '__main__':
    app.run(debug=True)
