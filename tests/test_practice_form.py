import pytest
import json
from pages.practice_form_page import PracticeFormPage
from utils.data_loader import load_json_data 
# chama o utils para conseguir rodar


@pytest.mark.parametrize("data", load_json_data("data/practice_form_data.json"))
def test_fill_practice_form(driver, data):
    form_page = PracticeFormPage(driver)
    form_page.navigate()