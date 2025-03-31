# Selenium Script Documentation
## Overview
This script automates the process of solving a dynamically generated math question on the Open Answers "Join Us" page using Selenium WebDriver. It retrieves the question, evaluates the answer, and submits the response.

## Prerequisites
- Python 3.x
- Selenium library
- WebDriver for your browser (e.g., ChromeDriver for Google Chrome)
- Google Chrome installed

## Note
The script was generated using the Aqua IDE from jetbrains which contained all the necessary dependencies. The script needs to have the dependencies installed either globally or in the virtual environment.


## Script Breakdown
1. **Imports**: The script imports necessary libraries including `time` from the standard library and `webdriver` alongside `By` from `selenium`.
```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
```
2. **WebDriver Setup**: The script sets up the Chrome WebDriver with options to run in headless mode (without opening a browser window).
```python
browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
browser.get("https://www.openanswers.co.uk/join-us")
```
3. **Initial Wait**: The script waits for around 300ms to ensure the page is fully loaded and the question has been fetched from the backend.
```python
time.sleep(0.3)
```

4. **Question Retrieval**: The script locates the question element on the page using its id and retrieves its text.
and removes the '=' sign from the question text for evaluation.
```python
# Get the element by ID 'question'
question_element = browser.find_element(By.ID, "question")

# Parse the question text which would involve removing the '=' sign and stripping whitespace
question_text = question_element.text.replace("=", "").strip()
```

5. **Answer Evaluation**: The script evaluates the mathematical expression using the `eval` function.
```python
# Evaluate the question text to get the answer
answer_text = eval(question_text)
```
6. **Answer Input**: The script locates the answer input field by its id and enters the evaluated answer.
```python
# Set the text to the input field with ID 'answer'
answer_element = browser.find_element(By.ID, "answer")
answer_element.send_keys(answer_text)
```
7. **Submit Answer**: The script locates the submit button by its id and clicks it to submit the answer.
```python
# Click the button with ID 'submit'
submit_button = browser.find_element(By.ID, "submit")
submit_button.click()
```

8. **Final Wait**: The script waits for 5 seconds to allow the submission process to complete before closing the browser.
```python
# Add a sleep to keep the browser open for a while to check whether there are other steps involved
time.sleep(1000000)
```
This was added to keep the browser open for a long time to check whether there are other steps involved. You can change this to a smaller number if you want to close the browser sooner.

## Other Considerations towards the solution
1. **Not using selenium**: This script used selenium as I had anticipated that the application would have additional steps to complete the process. However, if you are sure that the application will not have any additional steps, you can use the requests library to send a POST request to the server with the answer.
2. **Usage of eval**: The script uses the `eval` function to evaluate the mathematical expression. This generally is not recommended due to security concerns, but given the controlled environment of this script, it is acceptable. If you want to avoid using `eval`, other libraries can be used which can handle these concerns.
3. **Usage of time.sleep**: The script uses `time.sleep` to wait for the page to load and for the answer to be submitted. This is not the most efficient way to handle waiting in Selenium. Instead, you can use WebDriverWait to wait for specific conditions.

## Rationale behind using selenium with python
1. Given the simplicity of the task and my assumption of this being a multi-step process, I tried to keep it as simple as possible with the use of automation. I was also used to writing small scripts like this for automation during my previous role. However, if I had prior knowledge that the application process would not have any additional steps, I would have used the requests library to send a POST request to the server with the answer.
Here is an example of how you can do that:
```python
import requests

question_json = requests.get("https://www.openanswers.co.uk/api/v1/join-us").json()
# Remove the '=' sign and strip whitespace
question = question_json['question'].replace("=", "").strip()
answer = eval(question)
payload = {
    "answer": answer,
    "key": question_json['key']
}
response = requests.post("https://www.openanswers.co.uk/api/v1/join-us", json=payload)
# Print the response
print(response.json())
```
2. There were other considerations also regarding which language to use. I had considered javascript as well for this task because of a similar function it has to evaluate mathematical expressions. However, I thought setting up a cypress environment would be more than what is needed for this task.
