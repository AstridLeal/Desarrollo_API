import unittest
from app import app, db
from app.models import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        response = self.client.post('/users', json={'username': 'testuser', 'email': 'test@example.com'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()