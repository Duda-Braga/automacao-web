# conftest.py
import pytest
from selenium import webdriver
import json
from pathlib import Path
import time 
import os, pytest_html

@pytest.fixture #notacao do pytest
def driver():
    # Setup: initialize the WebDriver
    driver_instance = webdriver.Chrome()
    yield driver_instance #executa ate aq faz uma pausa e retrona pra qm chamou ele, conceitou do pyytest
    #alem de retornar ele divide a feature em duas 
    # Teardown: close the WebDriver
    driver_instance.quit() #qnd terminar de rodar o test ele vai fechar o browsers

# vai gerar na raiz do projeto um test duration
LOG_FILE = Path("test_durations.log")

@pytest.fixture #notacao do pytest
def test_data(): #feature para carregar o json
    with open("data/test_data.json") as f:
        return json.load(f)
    
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    item.start_time = time.time()
    item.start_str = time.strftime("%H:%M:%S", time.localtime())
    msg = f"\n[START] Test '{item.nodeid}' - {item.start_str}"
    print(msg)
    
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    duration = time.time() - item.start_time
    msg = f"[END] Test '{item.nodeid}' finished in {duration:.2f} seconds."
    print(msg)

    # salva em arquivo
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" and report.failed:
        # Create screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        # Take screenshot
        driver = item.funcargs['driver']
        screenshot_file = os.path.join("screenshots", f"{item.name}_error.png")
        driver.save_screenshot(screenshot_file)
        # Add screenshot to the HTML report
        if screenshot_file:
            html = f'<div><img src="{screenshot_file}" alt="screenshot" style="width:304px;height:228px;" ' \
           f'onclick="window.open(this.src)" align="right"/></div>'
            extra.append(pytest_html.extras.html(html))
    report.extra = extra