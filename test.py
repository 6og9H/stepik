from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
import time
import math

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    x= browser.find_element(By.ID, "input_value")
    x_text = x.text
    x1 = float(x_text)
    result = math.log(abs(12*math.sin(x1)))
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(str(result))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()