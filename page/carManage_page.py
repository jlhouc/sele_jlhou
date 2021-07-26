'''
    封装车辆管理页所有元素
'''
from selenium import webdriver
from lib.basePage import Basepage
from selenium.webdriver.common.by import By
from time import sleep

class carManage_page(Basepage):
    #页面关键元素
    left_carM = (By.XPATH,'//*[@id="side-menu"]/li[4]/a/span[1]')
    carM = (By.XPATH,'//*[@id="side-menu"]/li[4]/ul/li[1]/a')
    cartypeM = (By.XPATH,'//*[@id="side-menu"]/li[4]/ul/li[2]/a')
    driverM = (By.XPATH,'//*[@id="side-menu"]/li[4]/ul/li[3]/a')
    deviceM = (By.XPATH,'//*[@id="side-menu"]/li[4]/ul/li[4]/a')

    def deviceManage(self):
        self.click(self.left_carM)
        sleep(1)
        self.click(self.deviceM)