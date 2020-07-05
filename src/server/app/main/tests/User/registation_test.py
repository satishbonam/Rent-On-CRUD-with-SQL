from app.main.services.users import user_registration
import unittest

payload = {
    "name": "test"
}


class RegistrationTest(unittest.TestCase):
    def payload_mismatch(self):
        self.assertFalse(user_registration(payload))


if __name__ == '__main__':
    unittest.main()
