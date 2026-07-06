import requests


class PostApi ():
    URL_BASE="https://jsonplaceholder.typicode.com"

    def get_one_post(self, post_id):
        ret= requests.get(
            f"{self.URL_BASE}/posts/{post_id}"
            )
        return ret
    
    def get_posts(self):
        return requests.get(
            f"{self.URL_BASE}/users"
        )
    
a= PostApi()
a.get_one_post(10)
# b=a.get_posts()
# print(b.headers)
        
    