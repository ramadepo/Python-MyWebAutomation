from selenium import webdriver
from configure import Configure as configure


class Driver():
    @staticmethod
    def firefox():
        driver = webdriver.Chrome(executable_path="./driver/chromedriver")
        driver.implicitly_wait(10)
        return driver
