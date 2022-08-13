from selenium import webdriver
import pytest

@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome(executable_path="D:/Sandeep/Driver/chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    yield
    driver.close()

def test_verify_title(setup):
    #driver.get("https://opensource-demo.orangehrmlive.com/")
    assert driver.title == "OrangeHRM"
    #driver.close()

def test_verify_url(setup):
    #driver = webdriver.Chrome(executable_path="D:/Sandeep/Driver/chromedriver.exe")
   # driver.get("https://opensource-demo.orangehrmlive.com/")
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/"
    #driver.close()

