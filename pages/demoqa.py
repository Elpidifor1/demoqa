from selenium.common.exceptions import NoSuchElementException

#класс наследуется от класса BasePage (при импорте указывается его путь вместе с каталогом)
from pages.base_page import BasePage

from components.components import WebElement

#создаем класс конкретной страницы
class DemoQa(BasePage):
    def __init__(self, driver: object) -> None:
        self.base_url = 'https://demoqa.com/'
        self.footer_text = "© 2013-2026 TOOLSQA.COM | ALL RIGHTS RESERVED."
        super().__init__(driver,self.base_url)
        # данные прокидываются в верхний класс

        self.icon = WebElement(driver,locator='header > a')
        self.btn_elements = WebElement(driver, locator=".category-cards > a")
        self.footer = WebElement(driver,locator='footer > span')
        #заголовки 5 уровня c неуникальным локатором h5
        self.h5_headers = WebElement(driver,'h5')

    def exist_icon(self):
        try:
            #self.find_element(locator='#app > header > a')
            # self.find_element(locator='header > a')
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True
# потом эти метожы тоже закомментировали
# #добавляем новый метод
#     def click_on_the_icon(self):
#         #обращаемся к нашему элементу, т.е. ищем его, локатор такой же, и вызываем готовый из селениума метод click
#         self.find_element(locator="header > a > img").click()
#
#     # добавляем еще один новый метод
#     def click_on_the_btn(self):
#         #обращаемся к нашему элементу, т.е. ищем его, локатор такой же, и вызываем готовый из селениума метод click
#         self.find_element(locator=".category-cards > a").click()

    # добавляем еще один новый метод
    # а потом удаляем его и переносим в base_page
    # def equal_url(self):
    #     if self.get_url() == self.base_url:
    #         return True
    #     else:
    #         return False