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
from pages.stick_parameters import stick_p

class products_f(base):

    # Locators
    category_button = "//*[@id='content']/div/div[1]/div[1]/div/select"
    sticks = "//*[@id='content']/div/div[1]/div[1]/div/select/option[3]"
    apply_button = "//*[@id='button-search']"
    stick_qre_10_sr = "//*[@id='content']/div/div[4]/div[1]/div/div[2]/div[4]/div[2]/button"
    to_cart = "//*[@id='button-cart']/span[2]"
    proceed_btn = "//*[@id='rm-popup-cart']/div/div/div[2]/div[3]/div/a"
    confirm_order = "/html/body/div[3]/div[3]/div/div/div/div/div/div[4]/div[1]/input"


    # Getters
    def get_category_button(self):
        return self.driver.find_element(By.XPATH, self.category_button)
    def get_sticks(self):
        return self.driver.find_element(By.XPATH, self.sticks)
    def get_apply_button(self):
        return self.driver.find_element(By.XPATH, self.apply_button)
    def get_stick_qre_10_sr(self):
        return self.driver.find_element(By.XPATH, self.stick_qre_10_sr)
    def get_to_cart(self):
        return self.driver.find_element(By.XPATH, self.to_cart)
    def get_proceed_btn(self):
        return self.driver.find_element(By.XPATH, self.proceed_btn)
    def get_confirm_order(self):
        return self.driver.find_element(By.XPATH, self.confirm_order)
    # Actions
    def click_category_button(self):
        self.get_category_button().click()
        print("Выбираем категорию")
    def click_sticks(self):
        self.get_sticks().click()
        print("Выбираем клюшки")
    def click_apply_button(self):
        self.get_apply_button().click()
        print("Нажимаем 'Поиск'")
    def click_stick_qre_10_sr(self):
        self.get_stick_qre_10_sr().click()
        print("Выбираем WARRIOR QRE 10 SR")
    def click_to_cart(self):
        self.get_to_cart().click()
        print("Добавляем в корзину")
    def click_proceed(self):
        self.get_proceed_btn().click()
        print("Подтверждаем")
    def click_confirm_order(self):
        self.get_confirm_order().click()
        print("Завершаем заказ")
    # Methods
    def pick_categories(self):
        self.click_category_button()
        time.sleep(1)
        self.click_sticks()
        time.sleep(1)
        self.click_apply_button()
        self.driver.execute_script("window.scrollTo(0, 800)")
        time.sleep(1)
        self.click_stick_qre_10_sr()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        self.get_current_url()

    def pick_categories_2(self):
        self.confirm_current_url()
        time.sleep(1)
        self.click_to_cart()
        time.sleep(1)
        self.click_proceed()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)
        self.click_confirm_order()
        time.sleep(1)
        self.assert_url('https://hock5.ru/index.php?route=checkout/success')
        time.sleep(1)
        self.get_current_url()