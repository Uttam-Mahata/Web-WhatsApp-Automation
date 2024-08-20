from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import google.generativeai as genai

# Set your API key
API_KEY = "AIzaSyDrnUNdl2sQO1wT8nPL_rpHik-pVmR9E6Y"

# Configure Gemini API with your API key
genai.configure(api_key=API_KEY)

# Generate dynamic content using Gemini API before starting Selenium
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    print("Generating message... Please wait.")
    
    # Allow time for message generation
    response = model.generate_content("Write a short friendly message to Uttam.")
    
    # Check if the response is valid
    if hasattr(response, 'text') and response.text:
        message = response.text
        print("Generated Message:", message)
    else:
        raise ValueError("Failed to generate a message. Response is empty.")
    
except Exception as e:
    print("Error in generating content:", e)
    message = "Hello! This is an automated message."


driver = webdriver.Chrome()
baseurl = "https://web.whatsapp.com/"

driver.get(baseurl)
wait = WebDriverWait(driver, 10000)
target = '"Soumyadip"' # Your friend name e.g. Soumyadip as saved in WhatsApp
# string = "This is an automated message."
x_arg = '//span[contains(@title, '+target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
text_box = driver.find_element(By.CLASS_NAME,'_ak1l')
for i in range(30):
    text_box.send_keys(message+Keys.ENTER)
time.sleep(10000)


