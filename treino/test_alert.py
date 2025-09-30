import time
from treino.alert_pages import AlertPage

def test_simple_alert(driver):
    page_alert = AlertPage(driver)
    page_alert.navigate()

    page_alert.access_menu_alert_frame_window()
    page_alert.access_menu_alert()

    page_alert.click_simple_alert_button()

    texto = page_alert.check_simple_alert_text()
    assert texto == "You clicked a button"
    time.sleep(1)

    page_alert.accept_alert()
    time.sleep(1)

def test_five_sec_alert(driver):
    page_alert = AlertPage(driver)
    page_alert.navigate()

    page_alert.access_menu_alert_frame_window()
    page_alert.access_menu_alert()

    page_alert.click_time_alert_button()

    texto = page_alert.check_simple_alert_text()
    assert texto == "This alert appeared after 5 seconds"
    time.sleep(1)

    page_alert.accept_alert()
    time.sleep(1)
