from selenium.webdriver.common.by import By

def test_icon_exist(browser):
    browser.get("https://demoqa.com/")
    icon = browser.find_element(By.CSS_SELECTOR,"header > a > img")

    if icon is None:
        print("элемент не найден")
    else:
        print("элемент найден")

