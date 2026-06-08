from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time

def test_check_text_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == demo_qa_page.footer_text

def test_check_text_centre(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn.click()
    time.sleep(3)
    assert elements_page.centre.get_text() == elements_page.centre_text