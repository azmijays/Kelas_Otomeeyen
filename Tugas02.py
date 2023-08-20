from selenium import webdriver
from selenium.webdriver.common.by import By
from _pytest import mark
from _pytest.mark.structures import Mark

import pytest
import time

data1 = [
    ("Satoru","Gojo","150","satoru6969@gmail.com","3000000","Product"),
    ("Chopper","Jumawa","45","Media@gmail.com","5000000","HSSE"),
    ("azzmol","Jays","30","jays@gmail.com","50000000","PQM")
]

@pytest.fixture
def setup():
    driver = webdriver.Chrome(executable_path='C:/Users/azmij/chromedriver.exe')
    driver.get("https://demoqa.com/webtables")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()
    
@pytest.mark.input
@pytest.mark.parametrize('a,b,c,d,e,f',data1)
def test_input (setup,a,b,c,d,e,f):
    setup.find_element(By.ID,"addNewRecordButton").click()
    setup.find_element(By.ID,"firstName").send_keys(a)
    setup.find_element(By.ID,"lastName").send_keys(b)
    setup.find_element(By.ID,"userEmail").send_keys(c)
    setup.find_element(By.ID,"age").send_keys(d)
    setup.find_element(By.ID,"salary").send_keys(e)
    setup.find_element(By.ID,"department").send_keys(f)
    setup.find_element(By.ID,"submit").click()
