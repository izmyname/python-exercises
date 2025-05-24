import requests

class Post:
    def __init__(self):
        self.blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.get_blogs = self.blogs()
        
    def blogs(self):
        response = requests.get(url=self.blogs_url)
        return response.json
    
    def title(self, num):
        return self.get_blogs()[num -1]["title"]
    
    def subtitle(self, num):
        return self.get_blogs()[num -1]["subtitle"]
    
    def body(self, num):
        return self.get_blogs()[num -1]["body"]