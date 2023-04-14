from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
class alert():
    def alert(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.baidu.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.CSS_SELECTOR,"#s-usersetting-top").click()
        sleep(3)
        driver.find_element(By.LINK_TEXT,"搜索设置").click()
        sleep(3)
        driver.find_element(By.LINK_TEXT,"保存设置").click()
        sleep(3)
        alert = driver.switch_to.alert
        alert.accept()
        sleep(2)
        driver.quit()


if __name__ == '__main__':
    alert().alert()