from pages.base_page import BasePage
from components.components import WebElement

class WebTablesPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)
        self.no_rows_found_block = WebElement(driver, "div.rt-noData")
        self.btns_delete_row = WebElement(driver, '*[title = "Delete"]')
        self.btn_add = WebElement(driver, "#addNewRecordButton")
        self.registration_form = WebElement(driver, "#registration-form-modal")
        self.btn_submit_reg_form = WebElement(driver, "#submit")
        self.first_name = WebElement(driver, "#firstName")
        self.first_name_input = "Elpidifor"
        self.last_name = WebElement(driver, "#lastName")
        self.last_name_input = "The First"
        self.email = WebElement(driver, "#userEmail")
        self.email_input = "123@456.uu"
        self.age = WebElement(driver, "#age")
        self.age_input = '99'
        self.salary = WebElement(driver, "#salary")
        self.salary_input = '1000000'
        self.department = WebElement(driver, '#department')
        self.department_input = "ДИС_ОТВКС"
        self.first_name_in_table = WebElement(driver, "table > tbody > tr:nth-child(4) > td:nth-child(1)")
        self.last_name_in_table = WebElement(driver, "table > tbody > tr:nth-child(4) > td:nth-child(2)")
        self.age_in_table = WebElement(driver, "table > tbody > tr:nth-child(4) > td:nth-child(3)")
        self.email_in_table = WebElement(driver, "table > tbody > tr:nth-child(4) > td:nth-child(4)")
        self.salary_in_table = WebElement(driver, "table > tbody > tr:nth-child(4) > td:nth-child(5)")
        self.department_in_table = WebElement(driver, 'table > tbody > tr:nth-child(4) > td:nth-child(6)')
        self.btn_edit_4_row = WebElement(driver, '#edit-record-4')
        self.first_name_input_new = 'Akakij'
        self.btn_delete_4_row = WebElement(driver, '#delete-record-4')
        self.table_rows = WebElement(driver, 'table > tbody > tr')
        self.btn_next = WebElement(driver,".pagination > div > div:nth-child(1) > div > button:nth-child(3)")
        self.btn_previous = WebElement(driver, '.pagination > div > div:nth-child(1) > div > button:nth-child(2)')
        self.page_count = WebElement(driver,'.pagination > div > div:nth-child(2)')
