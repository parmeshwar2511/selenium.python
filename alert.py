from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.execute("window.scrollBy(0,500)")

source=driver.find_element(By.ID,'//*[@id="draggable"]/p')
target= driver.find_element(By.XPATH,'//*[@id="droppable"]')

act.drag_and_drop(source,target).perform()
