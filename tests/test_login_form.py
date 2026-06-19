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
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("11111111111111")
    form_page.hobbies.click_force()
    form_page.current_address.send_keys("talalushkino")
    time.sleep(2)
    #заполнение поля State and City
    form_page.state.scroll_to_element()
    form_page.state.click()
    time.sleep(2)
    form_page.state_drop_down.click()
    time.sleep(2)
    form_page.city.click()
    form_page.city_drop_down.click()
    time.sleep(2)
    form_page.btn_submit.click()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()





