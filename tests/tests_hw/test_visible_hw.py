from pages.accordian import AccordianPage
import time

def test_visible_accordion(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert accordian_page.accordian_section_one.visible()
    accordian_page.accordian_btn_one.click()
    time.sleep(2)
    assert not accordian_page.accordian_section_one.visible()

def test_visible_accordion_default(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()
    assert not accordian_page.accordian_section_two_part_1.visible()
    assert not accordian_page.accordian_section_two_part_2.visible()
    assert not accordian_page.accordian_section_three.visible()


