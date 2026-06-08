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


    # def equal_url(self):
    #     if self.get_url() == self.base_url:
    #         return True
    #     else:
    #         return False