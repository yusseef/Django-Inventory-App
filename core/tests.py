from django.test import TestCase
import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
class CoreTest(TestCase):
    #ensure secret key is not common
    def test_secretkey_strength(self):
        SECRET_KEY = settings.SECRET_KEY 
        
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Weak password {e.messages}"
            self.fail(msg)