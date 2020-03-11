#-*-coding:utf-8 -*-

import requests,re
from bs4 import BeautifulSoup

class pageApi:

    def get_pageData(self,num):
        proxy = '127.0.0.1:10809'
        proxies = {
            'http':'http://'+proxy,
            'https':'https://'+proxy
        }

        msg = """lastCity=101280600; __c=1583668618; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1582983683,1583027130,1583068146,1583668618; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1583668618; __l=l=https%253A%252F%252Fwww.zhipin.com%252Fshenzhen%252F&r=&friend_source=0&friend_source=0; __a=89382694.1583034028.1583068146.1583668618.14.3.2.14; __zp_stoken__=37d42ghx1R5ZzdXy9ENcsMnad14ZSN1jQwE26p2pgGiLkSdjWmJr1F5t0brFCFWT1NJqKALsR94NnsVVmUjS34Swg%2Bns8TH840FSzyCxgjbzSPQ6nFLKXQ5estbnlxPOLflR"""
        jobURL = []
        cookie = {}
        for i in msg.split(";"):
            cookie[i.split("=")[0]] = i.split("=")[1]

        url = 'https://www.zhipin.com/c101280600/'
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "cookie":msg
        }

        for index in range(num):
            data = {
                "query": "软件测试工程师",
                "page": index+1,
                "ka": "page-{0}".format(index+1)
            }
            result = requests.get(url=url, headers=header, params=data)
            print(result.text)
            soup = BeautifulSoup(result.text, 'lxml')
            for tag in soup.findAll('a', href=True):

                if tag['href'].find('job_detail') == 1:

                    if tag['href'].find('query') == -1:
                        # print(tag['href'])
                        urlpra = "https://www.zhipin.com/" + tag['href']
                        jodInfo = requests.get(url=urlpra, headers=header)
                        # print(jodInfo.text)
                        jobURL.append(urlpra)

                        reResult = BeautifulSoup(jodInfo.text, 'lxml')
                        self.save_data(reResult.select('.text')[0].get_text())

        print(jobURL)



    def save_data(self,num):
        with open("../data/jodInfo.txt","a",encoding='utf-8') as file:

            file.writelines(num)
        file.close()


if __name__ == "__main__":
    temp = pageApi()
    temp.get_pageData(1)