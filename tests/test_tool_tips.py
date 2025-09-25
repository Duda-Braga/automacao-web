from selenium.webdriver.common.by import By
from pages.tool_tips_page import ToolTipsPage
import json

from utils.data_loader import load_json_data

# chama o q ta dentro de utils para definri test_data como parametro global 
test_data = load_json_data("data/test_data.json") #test_data nao eh mais uma fixture, ele eh uma varivael
#a fixture nao precisa chamar, ele vai direto no pytest e executa ela trazneod pro arquivo do codigo

# ele vai la no conftest procurar o diverer e o test_data e rodar ele qnd passamo como parametro
def test_button_tooltip(driver):
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])

    tool_tips_page.hover_over_button()

    tooltip_text = tool_tips_page.get_tooltip_text()
     # assert tooltip_text == "You hovered over the Button" --> noa vai ser mais hardcode
    assert tooltip_text == (test_data["tool_tip_button_text"])

def test_field_tooltip(driver):
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])

    tool_tips_page.hover_over_field()

    tooltip_text = tool_tips_page.get_tooltip_text()
    assert tooltip_text == (test_data["tool_tip_field_text"])