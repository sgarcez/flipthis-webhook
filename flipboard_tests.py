import os
import unittest
import tempfile

from flipboard import Flipboard

class FlipboardTestCase(unittest.TestCase):

    # def setUp(self):
    #     self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    #     flaskr.app.config['TESTING'] = True
    #     self.app = flaskr.app.test_client()
    #     flaskr.init_db()

    # def tearDown(self):
    #     os.close(self.db_fd)
    #     os.unlink(flaskr.app.config['DATABASE'])
	def test_instantiation(self):
		f = Flipboard()

	def test_get_csrf(self):
		html = open('fixtures/login.html', 'r')
		f = Flipboard()
		csrf = f.get_csrf(html)
		self.assertEqual(u'+3Q5PqP2xp8uUOPOFR5N0RvBSxU=|szdAibdBL8xtb7BqYTaX5ZM/mFwi1yKz4guehNTsDyLdm8GelpFLc/4L2S0gXTA5SEGxisNOi4T3AQtQrSEQcA==', csrf,
                         'incorrect csrf token')

if __name__ == '__main__':
	unittest.main()