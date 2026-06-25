from pages.koup_page import Koup
from pages.koup_add_page import KoupAdd

def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()

    assert koup_page.link_add.get_text() == "Add/Remove Elements"
    koup_page.link_add.click()
    assert koup_add.equal_url()

    assert koup_add.btn_add.get_text() == "Add Element"

    assert koup_add.btn_add.get_dom_attribute(name = "onclick") == "addElement()"

    # кликнуть на кнопку 4 раза
    for i in range(4):
        koup_add.btn_add.click()

    # проверка для всех элементов
    assert koup_add.btns_delete.check_count_elements(4)

    # пример плохой проверки - т.к. локатор не уникальный, то проверится только первый попавшийся:
    assert koup_add.btns_delete.get_text() == "Delete"

    # кликнуть на каждую кнопку - цикл while - пока кнопки существуют, мы на них кликаем

    while koup_add.btns_delete.exist():
        koup_add.btns_delete.click()
# всё прокликали, условие false -> проволим проверку, что кнопки теперь НЕ существуют
    assert not koup_add.btns_delete.exist()