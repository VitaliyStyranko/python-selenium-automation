from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')


driver.find_element(By.ID, "nav-orders").click()

#  Verify 'Sign In' header is visible
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

print("Test case 'Sign In header' - passed")

#  Verify email input field is present
expected_result = ''
actual_result = driver.find_element(By.ID, "ap_email").text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

print("Test case 'Email input field is present' - passed")

driver.quit()