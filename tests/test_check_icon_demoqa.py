from selenium import webdriver
from selenium.webdriver.common.by import By
#передаем в тело функции
def test_icon_exist(): #всё, что ниже - отступ
    # создаем драйвер
    driver = webdriver.Chrome()
    #в драйвер передаем ссылку на нашу страницу
    driver.get("https://demoqa.com/")
    #создаем объект иконки                           в кавычках передаем локатор
    icon = driver.find_element(By.CSS_SELECTOR,"header > a > img")

    if icon is None:
        print("элемент не найден")
    else:
        print("элемент найден")

test_icon_exist()