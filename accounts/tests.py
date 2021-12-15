from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import User
from django.urls import reverse

class BlogTest(TestCase):

    def setUp(self):
      self.user = get_user_model().objects.create_user(
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

    def test_blog_list_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_blog_details_view(self):
        response = self.client.get(reverse('register_return', args="1"))
        self.assertEqual(response.status_code, 200)



#         ####### 

        
    def test_blog_update_view(self):
        response = self.client.get(reverse('register_return', args=('1')), {
            "email": "adham@gmail.com",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'adham@gmail.com')

#     ############
 
    def test_home_status(self):
        expected = 200
        url = reverse('register')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        

    
#    ################

    def test_create_view(self):
        response = self.client.get(reverse('register'), {
            "id": 1,
            "email": "adham@gmail.com",
            "username": "adham",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 1)
        # self.assertContains(response, 'adham@gmail.com')
        self.assertContains(response, 'adham')

    def test_delete_view(self):
        response = self.client.get(reverse('register_return', args='1'))
        self.assertEqual(response.status_code, 200)
    
    
    