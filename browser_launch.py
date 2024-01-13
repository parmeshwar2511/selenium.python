import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

chkbox1 = driver.find_element(By.ID,'checkbox1')
if chkbox1.is_selected():
    pass
else:
    chkbox1.click()
chkbox2 = driver.find_element(By.ID,'checkbox2')
if chkbox2.is_selected():
    pass
else:
    chkbox2.click()




