import allure

class GooglePage:

    def __init__(self, driver):
        self.driver = driver


    def goto(self):
        with allure.step('Открываю главную страницу Гугл'):
            self.driver.get('https://google.com')