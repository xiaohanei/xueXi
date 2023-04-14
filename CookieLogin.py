from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def cookieLogin():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    driver.add_cookie({"name":"BAIDUID","value":"CC53458AF133AB58BA127705EBD8F412:SL=0:NR=10:FG=1"})
    driver.add_cookie({"name":"BDUSS","value":"mRTRFRLZjQ0dn5pOGt6cmc4UktNQ2F2Q1NqUEJTU2lGLVBMODZiQ0h3czRKRXBrSVFBQUFBJCQAAAAAAQAAAAEAAAAjPl5mAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADiXImQ4lyJkW"})
    sleep(3)
    driver.refresh()
    sleep(2)
    driver.quit()

if __name__ == '__main__':
    cookieLogin()


