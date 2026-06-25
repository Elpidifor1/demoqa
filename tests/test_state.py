from pages.form_page import FormPage
import time
from selenium.webdriver.common.keys import Keys

#1 способ - клик по кнопке селекта и по элементу списка
def test_state(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)

#2 способ - отправка теста в поле ввода
def test_state_2(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.inp_state.send_keys("NCR")
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)

#3 способ - клик по кнопке селекта и выбор значения списка стрелочкой
def test_state_3(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.inp_state.send_keys(Keys.PAGE_DOWN)
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)


