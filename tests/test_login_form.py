import time
from pages.form_page import FormPage

def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys("Elpidifor")
    form_page.last_name.send_keys("Nedouckin")
    form_page.user_email.send_keys("test@test.tt")
    form_page.gender_radio_1.click()
    form_page.user_number.send_keys("11111111111111")
    time.sleep(2)
    form_page.btn_submit.click()
    time.sleep(2)






