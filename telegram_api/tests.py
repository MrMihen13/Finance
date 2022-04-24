from rest_framework.test import APIClient, APITestCase

from core import models


class TestTelegramCostView(APITestCase):
    def setUp(self) -> None:
        self.cost_id = 0
        self.cost_name = 'Test Cost Name'
        self.cost_uid = 123455678
        self.cost_amount = '1234'

    def tearDown(self) -> None:
        cost = models.Cost.objects.filter(name=self.cost_name).first()
        if cost is not None:
            cost.delete()

    def testPost(self):
        response = self.client.post(
            '/api/v1/telegram/cost/', {'telegram_uid': self.cost_uid, 'name': self.cost_name, 'amount': self.cost_amount}, format='json'
        )
        self.assertTrue(response.status_code == 201)

    def testPut(self):
        ...

    def testPatch(self):
        ...

    def testDelete(self):
        ...


class TestTelegramCategoryView(APITestCase):
    ...
