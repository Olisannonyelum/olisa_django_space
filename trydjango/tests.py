# from django.test import testcases
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password

import os
#OR we may use 
from django.conf import settings

class TryDjangoConfigTest(TestCase):
    def test_secrit_key_strength(self):
        # self.assertaTrue(1==2)
        SECRET_KEY = os.environ.get('SECRET_KEY1')
        # or by using this this provide more flexivility as in like
        # settings.DEBUG
        # settings.ALLOWED_HOST
        # this can bring out all variable in the setting.py file or with this we can access all the variable in the setting.py 
        SECRET_KEY2 = settings.SECRET_KEY
        try:
            # self.assertNotEqual(SECRET_KEY, "abc")
            is_strong = validate_password(SECRET_KEY)
            # print(type(is_strong),'...................>')
        except Exception as e:
            self.fail('bad password')
#django provid a future that help to validate password
# this validation is located in from django.contrib.auth.password_validation import