from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

a=1
b=2
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

wait = WebDriverWait(driver, 10)
lan = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
lan.click()


while a+b!=1:
    wait = WebDriverWait(driver, 15)
    cookie=wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
    cookie.click()
    
while a+b!=1:
    wait = WebDriverWait(driver,30)
    curser=wait.until(EC.element_to_be_clickable((By.ID, "product0")))
    curser.click()
    
    
if driver.(By.ID, "cookies")==15:
    
    




