import requests
import json

class EverveAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.everve.net/v3/"
        self.format = "json"

    def make_request(self, endpoint, params=None):
        if params is None:
            params = {}
        params["api_key"] = self.api_key
        params["format"] = self.format
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        return json.loads(response.text)

    def get_user(self):
        return self.make_request("user")

    def get_socials(self):
        return self.make_request("socials")

    def get_categories(self, id=None):
        endpoint = f"categories/{id}" if id else "categories"
        return self.make_request(endpoint)

    def create_order(self, params):
        return self.make_request("orders", params)

    def get_orders(self, id=None):
        endpoint = f"orders/{id}" if id else "orders"
        return self.make_request(endpoint)

    def update_order(self, id, params):
        params["id"] = id
        return self.make_request(f"orders/{id}", params)

    def delete_order(self, id):
        return self.make_request(f"orders/{id}", {"_method": "DELETE"})

# EXAMPLE:
# api = EverveAPI("your_api_key_here")
# user_info = api.get_user()
# print(user_info)