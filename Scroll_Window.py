from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class scrollWindow():
    def scrollWindow(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
       # driver.maximize_window()
        driver.implicitly_wait(5)
        try:
            driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("python")
            driver.find_element(By.CSS_SELECTOR,'#su').click()
        except NoSuchElementException as msg:
            print(msg)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(10)
        
        # js = 'var action=document.documentElement.scrollTop=0'
        # driver.execute_script(js)
        # sleep(3)
        # driver.quit()


if __name__ == '__main__':
    scrollWindow().scrollWindow()
