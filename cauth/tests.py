from rest_framework import test

from cauth import models


class SigninTest(test.APITestCase):
    def setUp(self):
        self.username = 'test'
        self.password = '12test12'
        self.email = 'test@example.com'
        self.user = models.CustomUser.objects.create_user(
            username=self.username, password=self.password, email=self.email
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = models.CustomUser.objects.get(username=self.username)
        self.assertTrue(user is not None)

    def test_wrong(self):
        user = models.CustomUser.objects.filter(username='wrong_username').first()
        self.assertTrue(user is None)
