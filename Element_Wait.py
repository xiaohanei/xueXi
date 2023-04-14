from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import ctime,sleep
from selenium.webdriver.common.by import By
class elementWait():
    def showWait(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("python")
        element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
        element.click()
        sleep(3)
        driver.quit()

    def implicitlyWait(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        try:
            driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("python")
            driver.find_element(By.CSS_SELECTOR,'#su').click()
        except NoSuchElementException as msg:
            print(msg)
        sleep(3)
        driver.quit()
        
if __name__ == '__main__':
    #elementWait().showWait()
    elementWait().implicitlyWait()



