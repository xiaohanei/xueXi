from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class switchWindow():
    def switchWindow(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        driver.maximize_window()
        handel_1 = driver.current_window_handle
        #print(handel_1)
        driver.find_element(By.LINK_TEXT,"新闻").click()
        sleep(10)
        handel_2 =driver.current_window_handle
        #print(handel_2)
        driver.switch_to.window(handel_1)
        sleep(3)
        driver.find_element(By.LINK_TEXT,"视频").click()
        sleep(2)
        driver.quit()

if __name__ == '__main__':
    switchWindow().switchWindow()
