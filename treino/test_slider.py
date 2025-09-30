#ta na homme e clicar em widgets
#clicar no meno lateral de slider
#botar o mouse por cima do botao azul
#arrasta o botao 
#verifica se arrastou

from slider_page import Slider
import time

def test_slider(driver):
    slider = Slider(driver)
    #ta na homme e clicar em widgets
    slider.navigate()
    #slider.access_menu_widgets()

    # clicar no menu lateral de slider
    #slider.access_menu_slider()

    #ve o valor inicial do slider
    inicial_value = slider.slider_value_number()

    #achar slider e segurar bolinha com mouse
    slider.click_hold_slider()

    #veririfca se arrastou
    time.sleep(2)
    value = slider.slider_value_number()
    assert value != inicial_value