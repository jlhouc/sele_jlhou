'''
    用于实现系统的登录操作。
    封装登录页所有元素
'''
from selenium import webdriver
from lib.basePage import Basepage
from selenium.webdriver.common.by import By
from time import sleep



class login_page(Basepage):
    #页面URL
    URL= 'http://t.pandabus.cc:8080/wanhua/login'
    #页面关键元素
    username = (By.ID,'userName')#帐号框
    password = (By.ID,'password')#密码框
    verifyCode = (By.ID,'verifyCode')#验证码
    loginbtn = (By.XPATH,'/html/body/div/div/div/div[2]/div/button[1]')#登录按钮

    #页面的登录流程
    def login(self,login_user,login_pwd):
        self.visit(self.URL)
        self.input(self.username,login_user)
        self.input(self.password,login_pwd)
        verification = input('请输入你的验证码：')
        self.input(self.verifyCode,verification)
        sleep(2)
        self.click(self.loginbtn)

