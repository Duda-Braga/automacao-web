from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/"
        self.menu_alert_frame_window = (By.XPATH, "//*[text()='Alerts, Frame & Windows']")
        self.menu_alert = (By.XPATH, "//span[text()='Alerts']")
        self.simple_alert_button = (By.ID,"alertButton")
        self.time_alert_button = (By.ID, "timerAlertButton")
        
        self.wait = WebDriverWait(self.driver, 10)

    def navigate(self):
        self.driver.get(self.url)

    def access_menu_alert_frame_window(self):
        self.driver.find_element(*self.menu_alert_frame_window).click()
    
    def access_menu_alert(self):
        menu_left = self.wait.until(EC.visibility_of_element_located(self.menu_alert))
        menu_left.click()

    def click_simple_alert_button(self):
        self.driver.find_element(*self.simple_alert_button).click()

    def click_time_alert_button(self):
        self.driver.find_element(*self.time_alert_button).click()

    def check_simple_alert_text(self):
        simple_alert = self.wait.until(EC.alert_is_present())
        return simple_alert.text
    
    def accept_alert(self):
        simple_alert = self.wait.until(EC.alert_is_present())
        return simple_alert.accept
    











'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# cria classe para testar os alertas
class Alert:
    def __init__(self,driver):
        self.dirver = driver
        # testa primeiro direto em alert, dps faz comecando da home
        self.url = "https://demoqa.com/alerts" ##MUDR DEPOIS

        self.wait = WebDriverWait(self.driver, 10)

        #mapear itens da pagina
        self.tab_alert = (By.ID, "item-1") #opcoes de botoes de alerta
        # botoes da pagina de alert
        self.see_alert_button = (By.ID, "alertButton")
        self.timer_alert_button = (By.ID, "timerAlertButton")
        self.confirm_button = (By.ID, "confirmButton")
        self.prompt_button = (By.ID, "promtButton")

    def navigate(self):
        # entrar direto na pagina por enquanto
        self.driver.get(self.url)

    #ir para aba de alerts
    /html/body/div[2]/div/div/div[2]/div/div[3]/div/div[1] fuul xpath



    def click_alert_button(self):
        self.dirver.find_element(*self.see_alert_button).click() #clicar no botao um
        
    def check_alert_text(self): #retorna texto do pop up
        #web dirver para o o alerta aparecer
        alert_popup = self.wait.until(EC.alert_is_present())
        return alert_popup.text
    
    def click_timer_alert_button(self): 
        self.driver.find_element(*self.timer_alert_button).click() #clicar no botao dois
    
    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click() #clicar no botao tres
    
    def select_ok(self):
        alert_popup = self.wait.until(EC.alert_is_present())
        alert_popup.accept #aperta em ok

    def click_prompt_button(self):
        self.driver.find_element(*self.prompt_button).click() #clicar no botao quatro


    def fill_popup(self): #digita texto
        alert_popup = self.wait.until(EC.alert_is_present())
        alert_popup.send_keys("teste")





'''

