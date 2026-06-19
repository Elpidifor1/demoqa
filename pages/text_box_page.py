from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        super().__init__(driver, self.base_url)
        self.full_name = WebElement(driver, "#userName")
        self.current_address = WebElement(driver, "#currentAddress.form-control")
        self.submit_btn = WebElement(driver, "#submit")
        self.footer_name = WebElement(driver, "#name")
        self.footer_current_address = WebElement(driver, "#currentAddress.mb-1")
        self.Full_Name_Input = "Elpidifor the First"
        self.Current_Address_Input = "Neverland"
