import time
from pages.web_tables_page import WebTablesPage


def test_webtables_pagination(browser):
    web_tables_page = WebTablesPage(browser)
    web_tables_page.visit()
    for i in range(2):
        web_tables_page.btn_add.click()
        web_tables_page.first_name.send_keys(web_tables_page.first_name_input)
        web_tables_page.last_name.send_keys(web_tables_page.last_name_input)
        web_tables_page.email.send_keys(web_tables_page.email_input)
        web_tables_page.age.send_keys(web_tables_page.age_input)
        web_tables_page.salary.send_keys(web_tables_page.salary_input)
        web_tables_page.department.send_keys(web_tables_page.department_input)
        web_tables_page.btn_submit_reg_form.click()
        time.sleep(2)

    assert web_tables_page.table_rows.check_count_elements(5)
    assert web_tables_page.btn_next.get_dom_attribute("disabled")
    assert web_tables_page.btn_previous.get_dom_attribute("disabled")
    assert not "2" in web_tables_page.page_count.get_text()

    for i in range(6):
        web_tables_page.btn_add.click()
        web_tables_page.first_name.send_keys(web_tables_page.first_name_input)
        web_tables_page.last_name.send_keys(web_tables_page.last_name_input)
        web_tables_page.email.send_keys(web_tables_page.email_input)
        web_tables_page.age.send_keys(web_tables_page.age_input)
        web_tables_page.salary.send_keys(web_tables_page.salary_input)
        web_tables_page.department.send_keys(web_tables_page.department_input)
        web_tables_page.btn_submit_reg_form.click()
        time.sleep(2)
    #
    # assert web_tables_page.table_rows.check_count_elements(11)
    assert web_tables_page.page_count.get_text() == "Page 1 of 2"
    assert not web_tables_page.btn_next.get_dom_attribute("disabled")

    web_tables_page.btn_next.click_force()
    assert web_tables_page.page_count.get_text() == "Page 2 of 2"
    web_tables_page.btn_previous.click()
    assert web_tables_page.page_count.get_text() == "Page 1 of 2"




