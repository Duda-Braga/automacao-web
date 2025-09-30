from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Slider:
    def __init__(self, driver):
        self.driver = driver
        self.url = self.url = "https://demoqa.com/slider"
        self.menu_widgets = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[4]/div/div[2]/svg")
        self.menu_slider = (By.XPATH, "//span[text()='Slider']")

        self.find_button_slider = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/form/div/div[1]/span/input")
        self.find_slider_value = (By.ID, "sliderValue")

        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    
    def navigate(self):
        self.driver.get(self.url)

    def access_menu_widgets(self):
        self.driver.find_element(*self.menu_widgets).click()
    
    def access_menu_slider(self):
        menu_left = self.wait.until(EC.visibility_of_element_located(self.menu_slider))
        menu_left.click()
    
    def click_hold_slider(self):
        button_slider = self.driver.find_element(*self.find_button_slider)
        self.actions.drag_and_drop_by_offset(button_slider, 1, 0).perform()

    def slider_value_number(self):
        slider_value = self.driver.find_element(*self.find_slider_value).text()
        return slider_value
    