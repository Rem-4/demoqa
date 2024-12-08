from pages.alerts import Alerts
import time
def test_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    assert not alert_page.alert()
    alert_page.btn_alert.click_force()
    time.sleep(2)
    assert alert_page.alert()
def test_alert_text(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.btn_alert.click_force()
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()

def test_check_alert_timer(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.btn_alert_timer.click()
    time.sleep(7)
    assert alert_page.alert()
    alert_page.alert().accept()
    assert not alert_page.alert()