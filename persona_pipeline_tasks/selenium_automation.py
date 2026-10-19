from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc


if __name__ == '__main__':
    try:
        
        driver = uc.Chrome(headless=False,use_subprocess=False)
        driver.get("http://chatgpt.com")
        
        time.sleep(5)
        input_area = driver.find_element(By.ID, 'prompt-textarea')
        # update send_keys with a list of questions that we would want to ask the llm.
        questions = "What are certain aspects about a user that create a strong political standing? Why do you think people hold onto their beliefs so firmly? And explain how these beliefs can create limited perspectives that harm others."
        input_area.send_keys(questions)
        input_area.send_keys(Keys.ENTER)
        time.sleep(10)
        
        # response_element = driver.find_element(By.CLASS_NAME, "markdown prose w-full break-words dark:prose-invert light")
        response_element = driver.find_elements(By.TAG_NAME, 'p')
        for e in response_element:
            print(e.text)

        # Print the response
        # print("ChatGPT Response:", response_text)

    finally:
        driver.quit()
        print("all done")

