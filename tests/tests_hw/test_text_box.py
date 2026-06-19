import time
from pages.text_box_page import TextBox

def test_clear(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_box_page.full_name.send_keys(text_box_page.Full_Name_Input)
    time.sleep(2)
    text_box_page.current_address.send_keys(text_box_page.Current_Address_Input)
    time.sleep(2)
    text_box_page.submit_btn.click()
    time.sleep(2)
    assert text_box_page.footer_name.get_text() == "Name:" + text_box_page.Full_Name_Input
    assert text_box_page.footer_current_address.get_text() == "Current Address :" + text_box_page.Current_Address_Input