from selenium.webdriver.common.by import By
import time

#Базовый класс страниц (всех)
class BasePage:

    #инициализация
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    #метод visit - ничего не принимает, возвращает переход на страницу (.get())
    def visit(self):
        return self.driver.get(self.base_url)

    #метод find_element - принимает аргумент locator, возвращает поиск элемента (.find_element()) с помощью By.CSS_SELECTOR
    # def find_element(self,locator):
    #     time.sleep((3))
    #     return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url #обращаемся к нашему драйверу и вызываем у него текущий урл

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False


