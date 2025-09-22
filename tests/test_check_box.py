from selenium.webdriver.common.by import By
from pages.check_box_pages import CheckBoxPage

# tirar tudo q for mapeamento de obejos, clique que vai ser usadao para construir a pagina
def test_check_box(driver):
    # driver.get("https://demoqa.com/checkbox") vira navigate
    check_box = CheckBoxPage(driver)
    check_box.navigate()
    
    # Expand the tree
    # expand_all_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
    # expand_all_button.click()
    check_box.click_expand_all()
    
    # Select the checkbox "Notes"
    # notes_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-notes']")
    # notes_checkbox.click()
    check_box.click_label_notes()
    
    # Validate if checkbox was ticked
    # notes_input = driver.find_element(By.ID, "tree-node-notes")
    assert check_box.check_notes_is_selected()