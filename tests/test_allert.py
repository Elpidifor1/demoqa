from pages.alerts import AlertsPage
import time

def test_alert(browser):
    alert_page = AlertsPage(browser)
    alert_page.visit()
    #проверка, что НЕТ активного алерта
    assert not alert_page.alert()

    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert()
#driver.close() при открытом алерте даёт ошибку. Нужно принять алерт перед завершением теста.
    alert_page.alert().accept()

def test_alert_text(browser):
    alert_page = AlertsPage(browser)
    alert_page.visit()
    alert_page.alertButton.click()
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()

def test_confirm(browser):
    alert_page = AlertsPage(browser)
    alert_page.visit()
    alert_page.confirmButton.click()
    time.sleep(2)
    #alert() - обращение к всплывающему окну
    #dismiss() - отмена вызова
    alert_page.alert().dismiss()
    assert alert_page.confirmResult.get_text() == 'You selected Cancel'

def test_prompt(browser):
    alert_page = AlertsPage(browser)
    name = "Elpidifor"
    alert_page.visit()
    alert_page.promptButton.click()
    time.sleep(2)
    alert_page.alert().send_keys(name)
    alert_page.alert().accept()
    assert alert_page.promptResult.get_text() == f"You entered {name}"
