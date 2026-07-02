from pages.demoqa import DemoQa
from pages.radio_button import RadioButtonPage
import pytest

@pytest.mark.skip
def test_decor_3(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.h5_headers.check_count_elements(6)

    for element in demo_qa_page.h5_headers.find_elements():
        assert element.text != ''
#здесь используем просто text (предоставляет селениум), а не get_text (наш), потому что работаем с элементом страницы, а не с нашим готовым

@pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_1(browser):
    radio_button_page = RadioButtonPage(browser)
    radio_button_page.visit()
    radio_button_page.yes_btn.click_force()
    assert radio_button_page.text.get_text() == 'You have selected Yes'

    radio_button_page.impressive_btn.click_force()
    assert radio_button_page.text.get_text() == 'You have selected Impressive'

    assert radio_button_page.no_btn.get_dom_attribute('class') == 'form-check-input disabled'
    #или, чтобы весь класс не переписывать, мжно написать     assert 'disabled' in radio_button_page.no_btn.get_dom_attribute('class')



