from pages.demoqa import DemoQa

def test_check_title_demoqa(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title == "demosite"