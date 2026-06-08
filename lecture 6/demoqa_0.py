# from selenium.common.exceptions import NoSuchElementException
#
# #класс наследуется от класса BasePage (при импорте указывается его путь вместе с каталогом)
# from pages.base_page_0 import BasePage
#
# #создаем класс конкретной страницы
# class DemoQa(BasePage):
#     #класс пока не имеет атрибутов, конструктор не требуется
# #создаем метод exist_icon: он вызывает метод find_elements родительского класса и передает в него наш локатор locator='#app > header > a'
#     def exist_icon(self):
#         try:
#             #self.find_element(locator='#app > header > a')
#             self.find_element(locator='header > a > img')
#         except NoSuchElementException:
#             return False
#         return True
# #добавляем новый метод
#     def click_on_the_icon(self):
#         #обращаемся к нашему элементу, т.е. ищем его, локатор такой же, и вызываем готовый из селениума метод click
#         self.find_element(locator="header > a > img").click()
#
#     # добавляем еще один новый метод
#     def equal_url(self):
#         if self.get_url() == "https://demoqa.com/":
#             return True
#         else:
#             return False