from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)
        self.btns_third_menu = WebElement(driver, ".element-group:nth-child(3) .btn.btn-light")
        self.main_icon = WebElement(driver, "#root > header > a")