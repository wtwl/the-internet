import allure
from selenium import webdriver
from assertpy import assert_that

@allure.title('Тест главной страницы Гугл')
def test_google():
    driver = webdriver.Chrome()
    with allure.step('Открываю главную страницу Гугл'):
        driver.get('https://google.com')

    with allure.step('Проверяю что url содержит google.com'):
        assert_that(driver.current_url).contains('gom')