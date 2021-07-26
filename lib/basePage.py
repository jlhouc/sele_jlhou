'''
    定义POM基类，作为整个POM结构下的工具类，用于其他PO对象进行调用
    封装一些常用的页面操作方法到这个类
'''
from selenium import webdriver
from time import sleep
driver = 1
# driver.find_element_by_id()

class Basepage:
    #定义一个构造函数
    def __init__(self,driver):
        self.driver = driver
    #元素的定位
    def locator(self,loc):
        return self.driver.find_element(*loc)

    #元素的输入
    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)

    #元素的点击
    def click(self,loc):
        self.locator(loc).click()

    #访问指定URL
    def visit(self,url):
        self.driver.get(url)

    #关闭浏览器
    def quit(self):
        sleep(3)
        self.driver.quit()

