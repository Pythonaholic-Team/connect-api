
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post ,Offer ,Comment
from django.urls import reverse
import requests
def getToken():
  url="http://localhost:8000/api/token/"
  response=requests.post(url,json={"email":"adham@gmail.com","password":"adham123"})
  tokens=response.json()
  return tokens.get("access")

class BlogTest(TestCase):
    




# # #####################

# #    ###########################

    def test_post_comment_offer(self):
        # self.client.login(json={"email":"adham@gmail.com", "password":"adham123"})
        # response = self.client.get(reverse('post'))
        access=getToken()
        response=requests.get("http://localhost:8000/api/v1/connect/post" ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response.status_code, 200)
        post_details=requests.get("http://localhost:8000/api/v1/connect/post/15/post_detail" , headers={"Authorization":"Bearer " +access})
        self.assertEqual(post_details.status_code, 200)
        response2=requests.put("http://localhost:8000/api/v1/connect/post/15/post_detail",json=post_details.json() ,headers={"Authorization":"Bearer " +access})

        self.assertEqual(response2.status_code,200)
        response3=requests.get("http://localhost:8000/api/v1/connect/offer/",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response3.status_code,200)
        response4=requests.put("http://localhost:8000/api/v1/connect/offer/",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response4.status_code,405)
        response5=requests.delete("http://localhost:8000/api/v1/connect/offer/",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response5.status_code,405)
        response6=requests.get("http://localhost:8000/api/v1/connect/comment",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(response6.status_code,200)
        comment_details=requests.get("http://localhost:8000/api/v1/connect/comment/2/comment_detail",json=post_details.json() ,headers={"Authorization":"Bearer " +access})
        self.assertEqual(comment_details.status_code,200)


