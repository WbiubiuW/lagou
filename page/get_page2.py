# encoding: utf-8

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from collections import namedtuple
from selenium.webdriver.common.action_chains import ActionChains
from units.getElements import waitObject
import units.dataClean as dc
import time,csv
import re
import json
import pandas as pd



class getPage():

    def __init__(self):
        self.url = "https://www.zhipin.com/"
        # 避免被识别出为模拟浏览器
        options = ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=None)


    def get_pare(self):

        self.driver.get(self.url)

        msg = """lastCity=101280600; __c=1583668618; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1582983683,1583027130,1583068146,1583668618; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1583668618; __l=l=https%253A%252F%252Fwww.zhipin.com%252Fshenzhen%252F&r=&friend_source=0&friend_source=0; __a=89382694.1583034028.1583068146.1583668618.14.3.2.14; __zp_stoken__=37d42ghx1R5ZzdXy9ENcsMnad14ZSN1jQwE26p2pgGiLkSdjWmJr1F5t0brFCFWT1NJqKALsR94NnsVVmUjS34Swg%2Bns8TH840FSzyCxgjbzSPQ6nFLKXQ5estbnlxPOLflR"""
        cookie = {
            "expires": ".zhipin.com",
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False,

        }
        for i in msg.split(";"):

            cookie['name'] = i.split("=")[0]
            cookie['value'] = i.split("=")[1]
            # self.driver.add_cookie(cookie_dict=cookie)
            print(cookie)
            # cookie.clear()

        self.driver.add_cookie(cookie)


        self.driver.get("https://www.zhipin.com/c101280600")

        getElementObj = waitObject(self.driver)
        #切换城市
        getElementObj.getElement('xpath', '//*[@id="header"]/div/div[2]/p/span[2]').click()
        # mouse = getElementObj.getElement('xpath', '//*[@id="header"]/div/div[2]/div/ul/li[28]')
        # ActionChains(self.driver).move_to_element(mouse).perform()#鼠标右击
        getElementObj.getElement('xpath', '/html/body/div[2]/div[2]/div[2]/div[2]/div[4]/ul/li[4]/a').click()

        #搜索
        getElementObj.getElement('name', 'query').clear()
        getElementObj.getElement('name', 'query').send_keys("软件测试工程师")
        getElementObj.getElement('xpath', '//*[@id="wrap"]/div[3]/div/div/div[1]/form/button').click()


    def get_page(self,page):

        temp = []

        for g in range(page):

            #分页设置
            start = g + 3
            getPageData = '//*[@id="main"]/div/div[3]/ul/li/div'
            pagePath = '//*[@id="main"]/div/div[3]/div[3]/a[{0}]'.format(start)
            if g > 0:
                getPageData = '//*[@id="main"]/div/div[2]/ul/li/div'
                pagePath = '//*[@id="main"]/div/div[2]/div[2]/a[{0}]'.format(start)
            if start >5:
                pagePath = '//*[@id="main"]/div/div[2]/div[2]/a[{0}]'.format(6)

            getElementObj = waitObject(self.driver)
            all = getElementObj.getElements('xpath', getPageData)

            for i in all:
                pageDate = i.text.replace("\n", " ").strip('\n').split(' ')

                # 数据清洗，提取计算平均工资
                dc.saleAvg(pageDate)
                # 数据清洗，把没有区的数据默认为深圳市
                dc.addAddress(pageDate)
                # 扩展列表
                pageDate.append(None)
                # 提取工作年限
                dc.jodExperience(pageDate)
                pageDate.append(None)
                # 提取学历
                dc.Education(pageDate)

                temp.append(pageDate)

            # 下拉到页面底部
            js = "var q=document.documentElement.scrollTop=10000"
            self.driver.execute_script(js)
            time.sleep(5)
            getElementObj.getElement('xpath', pagePath).click()

        return temp

    def get_dataClean(self):
        pass

    def get_pageData(self):
        cookie = {}
        for i in self.driver.get_cookies():
            cookie[i['name']] = i['value']
        print(json.dumps((self.driver.get_cookies())))
        print(cookie)



    #保存数据
    def save_data(self,num):
        with open("../data/page_data.csv","w") as file:

            w =csv.writer(file)
            title =['职位','薪资','城市','地区','垃圾数据','公司','公司规模','招聘者','工作年限','学历']

            w.writerow(title)
            w.writerows(num)
        file.close()

    def get_jodInfo(self):
        infoXpath = '//*[@id="main"]/div/div[3]/ul/li[1]/div/div[1]/h3/a/div[2]/div[2]/div[2]'
        getElementObj = waitObject(self.driver)
        temp = getElementObj.getElement('xpath',infoXpath)
        print('.........')
        print(temp.text)

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    temp = getPage()
    temp.get_pare()
    # temp.get_jodInfo()
    num = temp.get_page(10)

    temp.save_data(num)
    # temp.get_pageData()
    temp.close()

