import time

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import base

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(
    executable_path="chromium.chromedriver"))

class main_page_f(base):

    # Locators
    search_product = "//*[@id='input_search']"

    # Getters
    def get_search_product(self):
        return self.driver.find_element(By.XPATH, self.search_product)

    # Actions
    def click_search_product(self):
        self.get_search_product().send_keys("warrior")
        self.get_search_product().send_keys(Keys.RETURN)
        print("Ищем продукцию warrior")

    # Methods
    def pick_warrior(self):
        self.click_search_product()
        self.get_current_url()
        self.assert_url('https://hock5.ru/search?search=warrior')