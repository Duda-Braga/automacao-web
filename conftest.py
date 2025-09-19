# conftest.py
import pytest
from selenium import webdriver
@pytest.fixture #notacao do pytest
def driver():
    # Setup: initialize the WebDriver
    driver_instance = webdriver.Firefox()
    yield driver_instance #executa ate aq faz uma pausa e retrona pra qm chamou ele, conceitou do pyytest
    #alem de retornar ele divide a feature em duas 
    # Teardown: close the WebDriver
    driver_instance.quit() #qnd terminar de rodar o test ele vai fechar o browser