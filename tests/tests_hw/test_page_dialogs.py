from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa
import time

def test_modal_elements(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.btns_third_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    demoqa_page = DemoQa(browser)

    modal_dialogs_page.visit()
    time.sleep(3)
    modal_dialogs_page.refresh()
    time.sleep(3)
    modal_dialogs_page.main_icon.click()
    time.sleep(3)
    browser.back()
    time.sleep(3)
    browser.set_window_size(900, 400)
    time.sleep(3)
    browser.forward()
    assert demoqa_page.equal_url()
    assert browser.title == "demosite"
    browser.set_window_size(1000, 1000)
