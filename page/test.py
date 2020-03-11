# _._ coding:utf-8 _._

"""
:author: 花花测试
:time: 2017.05.03
:content: 使用第一种方法切换浏览器
"""

from selenium import webdriver
import time

#   打开课工场网站主页【第一个窗口】
driver = webdriver.Chrome()
driver.get('http://www.kgc.cn/')
driver.maximize_window()

#   点击全部课程，进入课程库【第二个窗口】
driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[3]/a/i').click()
time.sleep(3)

#   使用第一种方法切换浏览器【切换到第二个窗口】
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(3)

#   点击课程库中的某个课程，进入课程详情界面【在第二个窗口页面进行元素点击操作，来判断窗口是否切换成功】
driver.find_element_by_xpath('//*[@id="mainnav"]/li[6]/p/a').click()
time.sleep(3)

#   关闭浏览器
driver.close()
driver.switch_to.window(windows[0])
driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[3]/a/i').click()
print('测试通过')