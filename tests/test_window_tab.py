from pages.links import LinksPage
import time

def test_window_tab(browser):
    link_page = LinksPage(browser)
    link_page.visit()

    assert link_page.Home_link.get_dom_attribute('href') == 'https://demoqa.com'
    assert link_page.Home_link.get_text() == "Home"

    assert len(browser.window_handles) == 1

    link_page.Home_link.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
