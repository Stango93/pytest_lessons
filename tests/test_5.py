import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import Keys, ActionChains
from base.base_class import base
from pages.login_page_5 import login_page_f
from pages.main_page_5 import main_page_f
from pages.products_5 import products_f
import pytest

@pytest.fixture()
@pytest.mark.run(order=1)
def set_up():
    print("Начинаем")
    yield
    print("Заканчиваем")

@pytest.mark.run(order=2)
def test_buy_some_warrior_gear(set_up):

    driver = webdriver.Chrome(service=ChromeService(executable_path="chromium.chromedriver"))  # Optional argument, if not specified will search path.
    print("Начали тест")

    login = login_page_f(driver)
    login.authorize()

    mp = main_page_f(driver)
    mp.pick_warrior()

    pf = products_f(driver)
    pf.pick_categories()

    checkbox_elems = driver.find_elements(By.CLASS_NAME, 'radio')
    # выводится количество элементов с данным классом. Не привязывался по xpath, так как очень кривые id и наименования параметров, к тому же они меняются раз в день
    # print(len(checkbox_elems))
    checkbox_elems[0].click()
    print("Выбираем хват")
    checkbox_elems[1].click()
    print("Выбираем жёсткость")
    checkbox_elems[2].click()
    print("Выбираем загиб")

    pf = products_f(driver)
    pf.pick_categories_2()

    time.sleep(5)
