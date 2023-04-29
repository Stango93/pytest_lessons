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

class login_page_f(base):

    url = 'https://hock5.ru/'

    # Locators
    account_button = "//span[@class='d-flex align-items-center']"
    mail = "//*[@id='emailLoginInput']"
    password = "//*[@id='passwordLoginInput']"
    enter_button = "//*[@id='popup-login-button']"

    # Getters
    def get_account_button(self):
        return self.driver.find_element(By.XPATH, self.account_button)
    def get_mail(self):
        return self.driver.find_element(By.XPATH, self.mail)
    def get_password(self):
        return self.driver.find_element(By.XPATH, self.password)
    def get_enter_button(self):
        return self.driver.find_element(By.XPATH, self.enter_button)

    # Actions
    def click_account_button(self):
        self.get_account_button().click()
        print("Кликнули кнопку личного кабинета")

    def input_mail(self, mail_5):
        self.get_mail().send_keys(mail_5)
        print("Ввели почту")

    def input_password(self, password_5):
        self.get_password().send_keys(password_5)
        print("Ввели пароль")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Кликнули кнопку входа")

    def authorize(self):
    # def authorize(self, login_name_1, login_password_1):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_account_button()
        time.sleep(1)
        self.input_mail("stan_go@mail.ru")
        time.sleep(1)
        self.input_password("5_hockey")
        time.sleep(1)
        self.click_enter_button()
        time.sleep(3)