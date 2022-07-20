import datetime

from django.test import TestCase

from django.utils import timezone

from .models import Companies, Employee

class CompaniesModelTests(TestCase):


    def test_get_company_name(self):
        import datetime

        # Companies.objects.create(name="Testing", company_started=datetime.datetime.now())

        from django.test import Client
        client = Client()

        from django.urls import reverse
        response = client.get(reverse("employeeview", args=["Lavanya"]))

        assert response.status_code == 200
        # assert response.content.decode() == "Testing"


"""
View: get_company_name

Test case: 

company_id i/p
name response

Test cases original db ni access cheyyav. 

Test case lo oka company pettali
    1. Company create cheyyali 
    2. id request URL lo pass.
    3. Response Company name??
"""