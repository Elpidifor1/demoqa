# from selenium.webdriver.common.by import By
# import time
#
# #Базовый класс страниц (всех)
# class BasePage:
#
#     #инициализация
#     def __init__(self, driver):
#         #при инициализации у класса есть 2 атрибуту
#         #driver - принимается в качестве аргумента
#         #base_url - установлено значение по умолчанию
#         self.driver = driver
#         self.base_url = "https://demoqa.com/"
#
#     #метод visit - ничего не принимает, возвращает переход на страницу (.get())
#     def visit(self):
#         return self.driver.get(self.base_url)
#
#     #метод find_element - принимает аргумент locator, возвращает поиск элемента (.find_element()) с помощью By.CSS_SELECTOR
#     def find_element(self,locator):
#         time.sleep((3))
#         return self.driver.find_element(By.CSS_SELECTOR, locator)
#
#     def get_url(self):
#         return self.driver.current_url #обращаемся к нашему драйверу и вызываем у него текущий урл