# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import os
import google.generativeai as genai

API_KEY = "AIzaSyDrnUNdl2sQO1wT8nPL_rpHik-pVmR9E6Y"

# Configure Gemini API with your API key
genai.configure(api_key=API_KEY)

# Rest of your code


# # Initialize the WebDriver
# driver = webdriver.Chrome()
# baseurl = "https://web.whatsapp.com/"

# # Open WhatsApp Web
# driver.get(baseurl)
# wait = WebDriverWait(driver, 10000)

# # Specify the target contact name
# target = "Uttam"  # Change this to the name of your contact
# x_arg = f'//span[contains(@title, "{target}")]'

# # Wait for the target contact to appear and click on it
# target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
# target.click()

# # Locate the text box where messages are typed
# text_box = driver.find_element(By.CLASS_NAME, '_ak1l')

# Generate dynamic content using Gemini API
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Write a short friendly message to a friend.")
message = response.text

# # Send the generated message multiple times
# for i in range(30):
#     text_box.send_keys(message + Keys.ENTER)

# # Wait before closing the browser (optional)
# time.sleep(10)

# # Close the WebDriver
# driver.quit()
print(message)
