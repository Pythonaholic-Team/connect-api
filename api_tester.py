import fire
import requests

API_HOST = "http://127.0.0.1:8000"
RESOURCE_URI = "connect"
EMAIL = "adham@gmail.com"
PASSWORD = "adham123"


class ApiTester:
    """CLI for testing API"""

    def __init__(self, host=API_HOST):
        self.host = host

    def fetch_tokens(self):
        """Fetches access and refresh JWT tokens from api
        Returns:
            tuple: access,refresh
        """

        token_url = f"{self.host}/api/token/"

        response = requests.post(
            token_url, json={"email": EMAIL, "password": PASSWORD}
        )

        data = response.json()

        tokens = data["access"], data["refresh"]

        return tokens




    # def get_all(self):
    #     """get list of all resources from api
    #     Usage: python api_tester.py get_all
    #     Returns: JSON
    #     """
    #     access_token = self.fetch_tokens()[0]

    #     url = f"{self.host}/api/v1/{RESOURCE_URI}/"

    #     headers = {
    #         "Authorization": f"Bearer {access_token}",
    #     }

    #     response = requests.get(url, headers=headers)

    #     return response.json()

    # def get_one(self, id):
    #     """get 1 resource by id from api
    #     Usage:
    #     python api_tester.py get_one 1
    #     Returns: JSON
    #     """
    #     access_token = self.fetch_tokens()[0]

    #     url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}"

    #     headers = {
    #         "Authorization": f"Bearer {access_token}",
    #     }

    #     response = requests.get(url, headers=headers)

        # return response.json()

    
    # TODO adjust parameter names to match API
    # def create(self, name, description=None, owner=None):
    #     """creates a resource in api
    #     Usage:
    #     python api_tester.py create /
    #         --name=required --description=optional --owner=optional
    #     Returns: JSON
    #     """

    #     access_token = self.fetch_tokens()[0]

    #     url = f"{self.host}/api/v1/{RESOURCE_URI}/"

    #     headers = {
    #         "Authorization": f"Bearer {access_token}",
    #     }

    #     data = {
    #         "name": name,
    #         "description": description,
    #         "owner": owner,
    #     }

    #     response = requests.post(url, json=data, headers=headers)

    #     return response.json()

#  def update(self, id, name=None, description=None, owner=None):
#         """updates a resource in api
#         Usage:
#         python api_tester.py update 1 /
#             --name=optional --description=optional --owner=optional
#         Returns: JSON
#         """
#         access_token = self.fetch_tokens()[0]

#         url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}/"

#         headers = {
#             "Authorization": f"Bearer {access_token}",
#         }

#         original = self.get_cookiestand(id)

#         data = {
#             "name": name or original["name"],
#             "description": description or original["description"],
#             "owner": owner or original["owner"],
#         }

#         response = requests.put(url, json=data, headers=headers)

#         return response.text

    # def delete(self, id):
    #     """deletes a resource in api
    #     Usage:
    #     python api_tester.py delete 1
    #     Returns: Empty string if no error
    #     """

    #     access_token = self.fetch_tokens()[0]

    #     url = f"{self.host}/api/v1/{RESOURCE_URI}/{id}/"

    #     headers = {
    #         "Authorization": f"Bearer {access_token}",
    #     }

    #     response = requests.delete(url, headers=headers)

    #     return response.text
    def register_get_all(self):
        """get list of all resources from api
        Usage: python api_tester.py register_get_all
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/register/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def post_get_all(self):
        """get list of all resources from api
        Usage: python api_tester.py post_get_all
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/post"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()
    def offer_get_all(self):
        """get list of all resources from api
        Usage: python api_tester.py offer_get_all
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/offer"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()
    def comment_get_all(self):
        """get list of all resources from api
        Usage: python api_tester.py comment_get_all
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/comment"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()  
    def register_get_one(self, id):
        """get 1 resource by id from api
        Usage:
        python api_tester.py register_get_one 1
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/register/{id}"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()
    def post_get_one(self, id):
        """get 1 resource by id from api
        Usage:
        python api_tester.py post_get_one 1
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/post/{id}/post_detail"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()
    def comment_get_one(self, id):
        """get 1 resource by id from api
        Usage:
        python api_tester.py comment_get_one 1
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/comment/{id}/comment_detail"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def register_create(self):
        """creates a resource in api
        Usage:
        python api_tester.py register_create 
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/register/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        data = {
        "email": "email@el.com",
        "username": "adadsda",
        "password":"123456",
        "is_company": "False",
        "phone_number": "False",
        "country": "False"
        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()
    def post_create(self):
        """creates a resource in api
        Usage:
        python api_tester.py post_create 
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/post"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        data = {
        "body": "new",
        "created_at": "2021-12-15T09:21:16.786613Z",
        "creator": 5,
        "likes": [
          5
           ]
        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()
    def comment_create(self):
        """creates a resource in api
        Usage:
        python api_tester.py comment_create 
        Returns: JSON
        """
        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/comment"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        data = {
         "comment": "new",
         "created_at": "2021-12-18T13:48:00Z",
         "creator": 1,
         "on_post": [
          1
         ]
        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()

        

   
    def register_update(self, id):
        """updates a resource in api
        Usage:
        python api_tester.py register_update id 
        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/register/{id}"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        original = self.register_get_one(id)

        data = {
        "email": "update@update.com" or original['email'],
        "username": "na" or original['username'],
        "password":"na" or original['password'],
        "is_company": "False" or original['is_company'],
        "phone_number": "False" or original['phone_number'],
        "country": "False"or original['country']
        }

        response = requests.put(url, json=data, headers=headers)

        return response.text
    def post_update(self, id):
        """updates a resource in api
        Usage:
        python api_tester.py post_update id 
        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/post/{id}/post_detail"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        original = self.register_get_one(id)

        data = {
       "body": "new" or original['body'],
        "created_at": "2021-12-15T09:21:16.786613Z" or original['created_at'],
       "creator": 5 or original['creator'],
        "likes": [5] or original['likes'],
    
        }
    def comment_update(self, id):
        """updates a resource in api
        Usage:
        python api_tester.py comment_update id 
        Returns: JSON
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/comment/{id}/comment_detail/"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        original = self.register_get_one(id)

        data = {
      "comment": "new" or original['comment'],
       "created_at": "2021-12-18T13:48:00Z" or original['created_at'],
      "creator": 1 or original['creator'],
        "on_post": [1] or original['on_post'],
    
        }
       

        response = requests.put(url, json=data, headers=headers)

        return response.text


    def register_delete(self, id):
        """deletes a resource in api
        Usage:
        python api_tester.py register_delete id
        Returns: Empty string if no error
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/register/{id}"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.delete(url, headers=headers)

        return response.text
    def post_delete(self, id):
        """deletes a resource in api
        Usage:
        python api_tester.py post_delete id
        Returns: Empty string if no error
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/post/{id}/post_detail"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.delete(url, headers=headers)

        return response.text
    def comment_delete(self, id):
        """deletes a resource in api
        Usage:
        python api_tester.py comment_delete id
        Returns: Empty string if no error
        """

        access_token = self.fetch_tokens()[0]

        url = f"{self.host}/api/v1/connect/comment/{id}/comment_detail"

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        response = requests.delete(url, headers=headers)

        return response.text


if __name__ == "__main__":
    fire.Fire(ApiTester)