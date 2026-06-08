#эту штуку тоже можно удалить:
#from selenium.webdriver.common.by import By
#чтобы работать с классом, надо его импортировать
from pages.demoqa_0 import DemoQa
import time #импортируем библиотеку time

#def test_icon_exist(browser):
    # browser.get("https://demoqa.com/")
    # icon = browser.find_element(By.CSS_SELECTOR,"header > a > img")
    #
    # if icon is None:
    #     print("элемент не найден")
    # else:
    #     print("элемент найден")

# создаем объект нашего класса DemoQa и передаем в него browser (т.е. наш драйвер)
def test_icon_exist(browser):
    demo_qa_page = DemoQa(browser)
    #испольльзуем функцию visit, т.е. посещаем нашу страницу
    demo_qa_page.visit()
    #перед кликом пишем time.sleep
    time.sleep(3)
    # теперь вызываем клик после посещения
    demo_qa_page.click_on_the_icon()
    time.sleep(3) #страничка перезагрузится
    #вызывая метод assert, проверяем, что такой элемент действительно есть на странице
    assert demo_qa_page.exist_icon()

#код стал гораздо меньше

