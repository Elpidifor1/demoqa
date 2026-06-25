import time
from pages.web_tables_page import WebTablesPage


def test_webtables(browser):
    web_tables_page = WebTablesPage(browser)
    web_tables_page.visit()
    assert not web_tables_page.no_rows_found_block.exist()
    while web_tables_page.btns_delete_row.exist():
        web_tables_page.btns_delete_row.click_force()

    time.sleep(2)
    assert web_tables_page.no_rows_found_block.exist()
