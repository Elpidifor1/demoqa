from pages.text_box_page import TextBox

def test_text_box_submit(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()

    assert text_box_page.submit_btn.check_css('color', "rgba(255, 255, 255, 1)")
    assert text_box_page.submit_btn.check_css('backgroundColor', "rgba(13, 110, 253, 1)")
    assert text_box_page.submit_btn.check_css('borderBottomColor', "rgba(13, 110, 253, 1)")


