import datetime


class base():
    def __init__(self, driver):
        self.driver = driver



    """Method get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Текущий url = " + get_url)
    def confirm_current_url(self):
        get_url = self.driver.current_url
        print("Перевроверяем, текущий url = " + get_url)

    """Method assert_word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Niiiice")

    """Method screenshot"""

    def screenshot(self):
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = 'Screenshot' + current_date + '.png'
        self.driver.save_screenshot(
            'C:\\Users\\Stango\\Desktop\\' + name_screen)


    """Method assert url for warrior"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Да, мы ищем warrior")

    """Method assert url for cart"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Да, мы оформили заказ")