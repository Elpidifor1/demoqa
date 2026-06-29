from pages.alerts import AlertsPage
import time

def test_alert_5_sec(browser):
    alert_page = AlertsPage(browser)
    alert_page.visit()
    assert not alert_page.alert()
    alert_page.timer_alert_btn.click()
    time.sleep(7)
    assert alert_page.alert()
    alert_page.alert().accept()

