import time
from pages.web_tables_page import WebTablesPage


def test_webtables_add(browser):
    web_tables_page = WebTablesPage(browser)
    web_tables_page.visit()
    web_tables_page.btn_add.click()
    assert web_tables_page.registration_form.exist()
    web_tables_page.btn_submit_reg_form.click()
    assert web_tables_page.registration_form.exist()
    web_tables_page.first_name.send_keys(web_tables_page.first_name_input)
    web_tables_page.last_name.send_keys(web_tables_page.last_name_input)
    web_tables_page.email.send_keys(web_tables_page.email_input)
    web_tables_page.age.send_keys(web_tables_page.age_input)
    web_tables_page.salary.send_keys(web_tables_page.salary_input)
    web_tables_page.department.send_keys(web_tables_page.department_input)
    web_tables_page.btn_submit_reg_form.click()
    time.sleep(2)
    assert not web_tables_page.registration_form.exist()
    assert web_tables_page.first_name_in_table.get_text() == web_tables_page.first_name_input
    assert web_tables_page.last_name_in_table.get_text() == web_tables_page.last_name_input
    assert web_tables_page.age_in_table.get_text() == web_tables_page.age_input
    assert web_tables_page.email_in_table.get_text() == web_tables_page.email_input
    assert web_tables_page.salary_in_table.get_text() == web_tables_page.salary_input
    assert web_tables_page.department_in_table.get_text() == web_tables_page.department_input
    web_tables_page.btn_edit_4_row.click_force()
    assert web_tables_page.registration_form.exist()
    web_tables_page.first_name.clear()
    web_tables_page.first_name.send_keys(web_tables_page.first_name_input_new)
    web_tables_page.btn_submit_reg_form.click()
    time.sleep(2)
    assert not web_tables_page.registration_form.exist()
    assert web_tables_page.first_name_in_table.get_text() == web_tables_page.first_name_input_new
    assert web_tables_page.last_name_in_table.get_text() == web_tables_page.last_name_input
    assert web_tables_page.age_in_table.get_text() == web_tables_page.age_input
    assert web_tables_page.email_in_table.get_text() == web_tables_page.email_input
    assert web_tables_page.salary_in_table.get_text() == web_tables_page.salary_input
    assert web_tables_page.department_in_table.get_text() == web_tables_page.department_input
    web_tables_page.btn_delete_4_row.click_force()
    assert not web_tables_page.first_name_in_table.exist()
    assert not web_tables_page.last_name_in_table.exist()
    assert not web_tables_page.age_in_table.exist()
    assert not web_tables_page.email_in_table.exist()
    assert not web_tables_page.salary_in_table.exist()
    assert not web_tables_page.department_in_table.exist()





