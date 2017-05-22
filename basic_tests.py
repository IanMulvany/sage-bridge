import os
import basic
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, basic.app.config['DATABASE'] = tempfile.mkstemp()
        basic.app.config['TESTING'] = True
        self.app = basic.app.test_client()
        with basic.app.app_context():
            basic.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(basic.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'hola!' in rv.data

if __name__ == '__main__':
    unittest.main()
