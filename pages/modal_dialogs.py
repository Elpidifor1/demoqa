from pages.base_page import BasePage
from components.components import WebElement

class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)

        self.small_modal_btn = WebElement(driver, '#showSmallModal')
        self.small_modal = WebElement(driver, '#example-modal-sizes-title-sm')
        self.close_small_btn = WebElement(driver, '#closeSmallModal')
        self.large_modal_btn = WebElement(driver, '#showLargeModal')
        self.large_modal = WebElement(driver,'#example-modal-sizes-title-lg')
        self.close_large_btn = WebElement(driver, '#closeLargeModal')


