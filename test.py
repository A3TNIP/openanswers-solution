#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
browser.get("https://www.openanswers.co.uk/join-us")

# Time to wait for the question to load
time.sleep(0.3)
# Get the element by ID 'question'
question_element = browser.find_element(By.ID, "question")

# Parse the question text which would involve removing the '=' sign and stripping whitespace
question_text = question_element.text.replace("=", "").strip()

# Debugging: Print the question text to verify
print (question_text)

# Evaluate the question text to get the answer
answer_text = eval(question_text)

# Debugging: Print the answer text to verify
print (answer_text)

# Set the text to the input field with ID 'answer'
answer_element = browser.find_element(By.ID, "answer")
answer_element.send_keys(answer_text)

# Click the button with ID 'submit'
submit_button = browser.find_element(By.ID, "submit")
submit_button.click()

# Add a sleep to keep the browser open for a while to check whether there are other steps involved
time.sleep(1000000)