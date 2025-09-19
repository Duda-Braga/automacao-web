# test_demo.py
#agora com o conftest pode deixar assim
def test_verify_demoqa_title(driver):
    driver.get("https://demoqa.com")
    assert "DEMOQA" in driver.title