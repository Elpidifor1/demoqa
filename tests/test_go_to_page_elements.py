from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
# создаем объект нашего класса DemoQa и передаем в него browser (т.е. наш драйвер)
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
# вызываем метод visit, т е посещаем нашу страницу
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn.click()
    assert elements_page.equal_url()