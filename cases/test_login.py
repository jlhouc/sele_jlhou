#coding:utf-8
from lib.basePage import driver
import pytest
from lib.login import login
from time import sleep
from selenium.webdriver.common.keys import Keys


class Test_createDate():

    @classmethod
    def setup_class(cls):
        # cls.driver = webdriver.Edge('D:/py_test/msedgedriver')
        # cls.driver.get("http://t.pandabus.cc:8080/wanhua/login")
        # cls.driver.implicitly_wait(20)
        login()
        driver.find_element_by_xpath('//*[@id="side-menu"]/li[4]/a/span[1]').click()
        driver.find_element_by_xpath('//*[@id="side-menu"]/li[4]/ul/li[4]/a').click()
        print('\n *** 初始化-模块 ***')



    @pytest.mark.parametrize(
        "devicesId,simNumber",
        [("0005","5"),
         ("0006","6")]
        )
    def test_create_device(self,devicesId,simNumber):
        driver.find_element_by_xpath('//*[@id="btn_new"]').click()
        sleep(5)
        assert driver.current_url == 'http://t.pandabus.cc:8080/wanhua/device/update?from=/device/index&funcId=1'
        driver.find_element_by_id('id').send_keys(devicesId)
        driver.find_element_by_xpath('//*[@id="select2-type-container"]').click()
        driver.find_element_by_xpath('//html/body/span/span/span[1]/input').send_keys('扫描设备')
        driver.find_element_by_xpath('//html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
        driver.find_element_by_id('name').send_keys('wanhua')
        driver.find_element_by_id('simNumber').send_keys(simNumber)
        driver.find_element_by_id('btn_save').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[7]/button[2]').click()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div[7]/button[2]').click()
        assert driver.current_url == 'http://t.pandabus.cc:8080/wanhua/device/index'
        print('new success')
    def teardown_class(cls):
        print('\n ***   清除-模块 ***')

if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])