
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
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
        
        self.post = Post.objects.create(
            body='pancake',
            created_at='2021-12-15 00:40:02.119977+00:00',
            creator=self.user,
        )



# #####################
    def test_all_fields(self):
        
        self.assertEqual(str(self.post.body), 'pancake')
        self.assertEqual(f'{self.post.created_at}', '2021-12-15 00:40:02.119977+00:00')
        self.assertEqual(self.post.creator.username, 'ash')

#    ###########################

    # def test_blog_list_view(self):
    #     self.client.login(username='adham@gmail.com', password='adham123')
    #     response = self.client.get(reverse('post'))
    #     self.assertEqual(response.status_code, 200)

    # def test_blog_details_view(self):
    #     response = self.client.get(reverse('post_detail', args='1'))
    #     self.assertEqual(response.status_code, 200)



#         ####### 

        
    # def test_blog_update_view(self):
    #     response = self.client.post(reverse('post_detail',kwargs={'<int:pk>':"4"}), {
    #         'body': 'pancake',
    #     })
    #     self.assertEqual(response.status_code, 401)
    #     self.assertContains(response, 'pancake')

#     ############
    def test_home_status(self):
        user=self.user
        expected = 401
        url = reverse('comment')
        response = self.client.post(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        

#    ################

    # def test_create_view(self):
    #     response = self.client.post(reverse('post'), {
    #         "body":'pancake',
    #         "created_at":'2021-12-15 00:40:02.119977+00:00',
    #         "creator":self.user,
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'pancake')
    #     self.assertContains(response, '2021-12-15 00:40:02.119977+00:00')
    #     self.assertContains(response, 'ash')

    def test_delete_view(self):
        response = self.client.get(reverse('post_detail', args='1'))
        self.assertEqual(response.status_code, 200)
  

