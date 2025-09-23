from selenium.webdriver.common.by import By
from pages.tool_tips_page import ToolTipsPage
import json

def test_button_tooltip(driver, test_data):
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])

    tool_tips_page.hover_over_button()

    tooltip_text = tool_tips_page.get_tooltip_text()
     # assert tooltip_text == "You hovered over the Button" --> noa vai ser mais hardcode
    assert tooltip_text == (test_data["tool_tip_button_text"])

def test_field_tooltip(driver, test_data):
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])

    tool_tips_page.hover_over_field()

    tooltip_text = tool_tips_page.get_tooltip_text()
    assert tooltip_text == (test_data["tool_tip_field_text"])