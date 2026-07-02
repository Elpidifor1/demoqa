import time

from pages.progress_bar import ProgressBarPage
from selenium.webdriver.common.keys import Keys


def test_progress_bar(browser):
    progress_bar_page = ProgressBarPage(browser)
    progress_bar_page.visit()
    time.sleep(2)
    progress_bar_page.start_btn.click()

    while True:
        if progress_bar_page.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            progress_bar_page.start_btn.click()
            break

    time.sleep(2)

    assert progress_bar_page.progress_bar.get_text() == '51%'