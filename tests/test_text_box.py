from selenium.webdriver.common.by import By
from pages.text_box_page import TextBoxPage

def test_fill_text_box_form_and_validate(driver):
    text_box_page = TextBoxPage(driver)
    text_box_page.navigate()
    full_name = "duda teste"
    email = "teste@gmail.com"
    current_address = "rua 1"
    permanent_address = "do lado da rua 2"

    text_box_page.fill_form(full_name, email, current_address, permanent_address)
    text_box_page.submit()

    output = text_box_page.get_output_text()

    assert full_name in output
    assert email in output
    assert current_address in output
    assert permanent_address in output
