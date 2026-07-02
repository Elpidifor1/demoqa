from pages.slider import SliderPage
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    slider_page = SliderPage(browser)
    slider_page.visit()
    assert slider_page.slider.exist()
    assert slider_page.slider_value.exist()
    assert slider_page.slider.get_dom_attribute('value') =='25'
#введение значение в интерактивный элемент - через стрелку (цикл while not)

    while not slider_page.slider.get_dom_attribute('value') =='50':
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.slider.get_dom_attribute('value') =='50'
    assert slider_page.slider_value.get_dom_attribute('value') =='50'
