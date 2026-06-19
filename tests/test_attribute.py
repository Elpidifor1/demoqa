from pages.text_box_page import TextBox

def test_placeholder(browser):
    # проверка значения атрибута элемента
    text_box_page = TextBox(browser)
    text_box_page.visit()
    assert text_box_page.full_name.get_dom_attribute(name="placeholder") == "Full Name"