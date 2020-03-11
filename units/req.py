import requests
from urllib.parse import urlencode

class req:

    def req_post(self,url,data):
        headers = {
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie":None,
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }

        result = requests.post(url,data=data,headers=headers)
        print(result.url)
        print(result.headers)

        return result