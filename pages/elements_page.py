from pages.base_page import BasePage
from components.components import WebElement

#создаем класс конкретной страницы
class ElementsPage (BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        self.centre_text = "Please select an item from left to start practice."
        super().__init__(driver,self.base_url)
        # данные прокидываются в верхний класс
        self.centre = WebElement(driver,locator='#root > div > div > div > div.col-12.mt-4.col-md-6.col-xl-7')
        self.text_elements = WebElement(driver, "#root > div > div > div > div.col-12.mt-4.col-md-6.col-xl-7 ")
        self.icon = WebElement(driver,"header > a > img")
        self.btn_sidebar_first = WebElement(driver, ".col-12.mt-4.col-md-3.col-xl-2 > div > div > div:nth-child(1) > span > div > div.header-text")
        self.btn_sidebar_first_textbox = WebElement(driver, "#item-0 > a > span")
        self.btn_sidebar_first_checkbox = WebElement(driver, "#item-1 > a > span")




    # def equal_url(self):
    #     if self.get_url() == self.base_url:
    #         return True
    #     else:
    #         return False