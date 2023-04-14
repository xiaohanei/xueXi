from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class mouseAction():
    def openBrowser(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        driver.maximize_window()
        element = driver.find_element(By.CSS_SELECTOR,"#kw")
        element.send_keys("python")
        sleep(2)
        #双击鼠标
        ActionChains(driver).double_click(element).perform()
        sleep(2)
        #鼠标右键
        ActionChains(driver).context_click(element).perform()
        sleep(2)
        #鼠标悬停
        above = driver.find_element(By.CSS_SELECTOR,"[class='pf']")
        ActionChains(driver).move_to_element(above).perform()
        sleep(2)
        driver.quit()


if __name__ == '__main__':
    mouseAction().openBrowser()

