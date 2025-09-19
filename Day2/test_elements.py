from selenium.webdriver.common.by import By
import time
#testar a check da caixa
def test_check_box(driver):
    driver.get("https://demoqa.com/checkbox")
    #time.sleep(2)
    # Expand the tree
    expand_all_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
    expand_all_button.click()
    #time.sleep(2)
    # Select the checkbox "Notes"
    notes_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-notes']")
    notes_checkbox.click()
    #time.sleep(2)
    # Validate if checkbox was ticked
    notes_input = driver.find_element(By.ID, "tree-node-notes")
    assert notes_input.is_selected()
    #time.sleep(2) - bota o time.sleep pra ve as acoes

def test_check_box_commands(driver):
    driver.get("https://demoqa.com/checkbox")
    expand_all_button = driver.find_element(By.CSS_SELECTOR, "button[title='Expand all']")
    expand_all_button.click()
    # Select the checkbox 
    notes_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-commands']")
    notes_checkbox.click()
    time.sleep(2)
    # Validate if checkbox was ticked
    notes_input = driver.find_element(By.ID, "tree-node-commands")
    assert notes_input.is_selected()
    time.sleep(2) #- bota o time.sleep pra ve as acoes