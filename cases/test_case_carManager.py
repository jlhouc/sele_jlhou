import pytest
from lib.driverpage import driver
from page.login_page import login_page
from page.carManage_page import carManage_page
from time import sleep

class Test_carManager():

    def setup_class(cls):
        lp = login_page(driver)
        lp.login('wanhua','!QAZ2wsx')
        print('\n *** 初始化-模块 ***')


    def test_create_device(self):
        cm = carManage_page(driver)
        driver.implicitly_wait(20)
        cm.deviceManage()

    def teardown_class(cls):
        print('\n ***   清除-模块 ***')


if __name__ == '__main__':
    pytest.main(['-s', 'test_case_carManager.py'])