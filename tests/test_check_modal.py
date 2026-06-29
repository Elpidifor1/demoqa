from pages.modal_dialogs import ModalDialogsPage
import time


def test_check_modal(browser):
    modal_dialog_page = ModalDialogsPage(browser)
    modal_dialog_page.visit()

    modal_dialog_page.small_modal_btn.click()
    time.sleep(2)
    assert modal_dialog_page.small_modal.exist()
    modal_dialog_page.close_small_btn.click()
    time.sleep(2)
    assert not modal_dialog_page.small_modal.exist()

    modal_dialog_page.large_modal_btn.click()
    time.sleep(2)
    assert modal_dialog_page.large_modal.exist()
    modal_dialog_page.close_large_btn.click()
    time.sleep(2)
    assert not modal_dialog_page.large_modal.exist()

