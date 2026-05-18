from django.test import TestCase


class PortfolioSmokeTests(TestCase):
    def test_landing_page(self):
        response = self.client.get("/landing/")
        self.assertEqual(response.status_code, 200)
