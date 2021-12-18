from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import User ,UserManager
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from .serializers import LoginSerializer
import requests
# import pyjwt

def getToken():
  url="http://localhost:8000/api/token/"
  response=requests.post(url,json={"email":"adham@gmail.com","password":"adham123"})
  tokens=response.json()
  return tokens.get("access")

factory = APIRequestFactory()
class BlogTest(TestCase):

    def setUp(self):
      self.user = User.objects.create_user(
    country = "jordan",
    username = "ash",
    email = "adham@gmail.com",
    first_name ="ash",
    last_name = "adham",
    is_verified = True,
    is_active = True,
    is_staff = True,

    date_joined = "12/12/1212",
    
    last_login = "12/12/1212",
    auth_provider = "facebook",
        )
    def setUp(self):
      self.user = User.objects.create_user(
    country = "jordan",
    username = "ash",
    email = "adham@gmail.com",
    first_name ="ash",
    last_name = "adham",
    is_verified = True,
    is_active = True,
    is_staff = True,

    date_joined = "12/12/1212",
    
    last_login = "12/12/1212",
    auth_provider = "facebook",
        )
    
    def test_string_representation(self):
        user = User(username='ash')
        self.assertEqual(str(user), user.username)


# #####################
    def test_all_fields(self):
        
        self.assertEqual(str(self.user), 'ash')
        self.assertEqual(f'{self.user.country}', 'jordan')
        self.assertEqual(self.user.last_name, 'adham')

#    ###########################

    def test_accounts_app(self):
        user={
    "email": "adham@gmail.com",
    "password":"adham123",
    "username": "14dsd34",
    "is_company": "True",
    "phone_number": "False",
    "country": "False"
  
        }
        access=getToken()
        resp=requests.get("http://localhost:8000/register/",headers={"Authorization":"Bearer " +access})
        resp6=requests.post("http://localhost:8000/register/",json={"email":"adham@gmail.com","password":"adham123"},headers={"Authorization":"Bearer " +access})
        resp2=requests.get("http://localhost:8000/register/1",headers={"Authorization":"Bearer " +access})        # response = self.client.get(reverse('register'))
        resp3=requests.post("http://localhost:8000/login/",json=user ,headers={"Authorization":"Bearer " +access})  
       
       
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(resp3.status_code,200)
        self.assertEqual(resp6.status_code,400)


   