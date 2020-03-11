#-*-coding:utf-8 -*-

import requests,re
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import namedtuple
from selenium.webdriver.common.action_chains import ActionChains
from units.getElements import waitObject
import units.dataClean as dc
import time,csv
import re
import pandas as pd

class pageApi:


    def __init__(self):
        self.url = "https://www.zhipin.com/"
        self.driver = webdriver.Chrome()


    def get_pare(self):
        self.driver.get(self.url)
        getElementObj = waitObject(self.driver)

        cookie = {}
        for i in self.driver.get_cookies():
            cookie[i['name']] = i['value']

        self.driver.get("https://www.zhipin.com/job_detail/?query=&city=101280600&industry=&position=")

        print(self.driver.page_source)

        time.sleep(5)

    def get_pageData(self,page):
        for g in range(page):

            #分页设置
            start = g + 3
            getPageData = '//*[@id="main"]/div/div[3]/ul/li[1]/div/div[1]'
            pagePath = '//*[@id="main"]/div/div[3]/div[3]/a[{0}]'.format(start)
            if g > 0:
                getPageData = '//*[@id="main"]/div/div[2]/ul/li/div/div[1]'
                pagePath = '//*[@id="main"]/div/div[2]/div[2]/a[{0}]'.format(start)
            if start >5:
                pagePath = '//*[@id="main"]/div/div[2]/div[2]/a[{0}]'.format(6)

            getElementObj = waitObject(self.driver)

            getjodList = getElementObj.getElements('xpath',getPageData)
            print(len(getjodList))

            for k in getjodList:
                k.click()
                windows = self.driver.window_handles
                self.driver.switch_to.window(windows[-1])

                reResult = BeautifulSoup(self.driver.page_source, 'lxml')

                self.save_data(reResult.select('.text')[0].get_text())

                self.driver.close()
                self.driver.switch_to.window(windows[0])
                time.sleep(5)

            # 下拉到页面底部
            js = "var q=document.documentElement.scrollTop=10000"
            self.driver.execute_script(js)
            time.sleep(5)
            getElementObj.getElement('xpath', pagePath).click()


    def save_data(self,num):
        with open("../data/jodInfo.txt","a",encoding='utf-8') as file:

            file.writelines(num)
        file.close()

if __name__ == "__main__":
    temp = pageApi()
    temp.get_pare()

    # temp.get_pageData(10)