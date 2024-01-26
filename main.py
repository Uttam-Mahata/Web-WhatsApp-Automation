from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
baseurl = "https://web.whatsapp.com/"

driver.get(baseurl)
wait = WebDriverWait(driver, 10000)
target = '"Soumyadip"' # Your friend name e.g. Suraj as saved in WhatsApp
string = "Hello Soumadip ! This is an automated message.Supriyo keo send krbo erkm ?"
x_arg = '//span[contains(@title, '+target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
text_box = driver.find_element(By.CLASS_NAME,'_3Uu1_')
for i in range(30):
    text_box.send_keys(string+Keys.ENTER)
time.sleep(10000)

