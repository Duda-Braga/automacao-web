from selenium.webdriver.common.by import By
import pytest

from pages.test_elements_page import Elementspage

@pytest.mark.smoke
def test_navigate_to_elements_page(driver):
    elements_page = Elementspage(driver)
    elements_page.navigate()
    assert "elements" in driver.current_url

@pytest.mark.regression
@pytest.mark.smoke
def test_locate_by_id(driver):
    elements_page = Elementspage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_id_visible()
    assert elements_page.get_menu_check_box_id_text() == "Text Box"

@pytest.mark.regression
def test_locate_by_css_selector(driver):
    elements_page = Elementspage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_css_visible()

def test_locate_by_xpath(driver):
    elements_page = Elementspage(driver)
    elements_page.navigate()
    assert elements_page.is_check_box_path_visible()



""""
no init recebe ele mesmo e o dirver
define ele mesmo.driver como dirver
coloca o url da pagina que vamos acessar
bota self. nome de cada elemento mapeado
depois faz as funcoes que vao ser chaadas no test
"""