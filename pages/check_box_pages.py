from selenium.webdriver.common.by import By

#em self ele recebe ele mesmo
class CheckBoxPage():
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/checkbox"
        #mapeia o botao, cria a variavel para poder reutilizar
        self.expand_all_button = (By.CSS_SELECTOR, "button[title='Expand all']")
        self.label_notes = (By.XPATH, "//label[@for='tree-node-notes']")
        self.notes_input = (By.ID, "tree-node-notes")

    def navigate(self):
        self.driver.get(self.url)

    def click_expand_all(self):
        expand = self.driver.find_element(*self.expand_all_button)
        expand.click()
        # pode fazer o click direto sem criacao da variavel expand
        # self.driver.find_element(*self.expand_all_button).click()
    
    def click_label_notes(self):
        self.driver.find_element(*self.label_notes).click()

    #verificar se ta selecionado
    def check_notes_is_selected(self):
        return self.driver.find_element(*self.notes_input).is_selected()

#cria a primeio a page