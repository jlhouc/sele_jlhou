from time import sleep
from lib.basePage import driver

def login():
    driver.get('http://t.pandabus.cc:8080/wanhua/login')
    driver.implicitly_wait(20)
    # driver.maximize_window()
    driver.find_element_by_id('userName').send_keys('wanhua')
    driver.find_element_by_id('password').send_keys('!QAZ2wsx')
    verification = input('请输入你的验证码：')
    driver.find_element_by_id('verifyCode').send_keys(verification)
    driver.find_element_by_css_selector('body > div > div > div > div:nth-child(2) > div > button.btn.btn-primary.block.full-width.m-b').click()
    sleep(10)
    try:
        assert driver.current_url == 'http://t.pandabus.cc:8080/wanhua/dashboard/index'
        print('login success')
    except Exception as e:
        print('login fail')

    return driver.current_url




