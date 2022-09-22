from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/')


# These page elements of Amazon Sign in page

driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()

# Amazon logo
# driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']").click()

# Continue button
# driver.find_element( By.ID, "continue").click()

# Need help link
# driver.find_element(By.XPATH, "//*[@class='a-expander-prompt']").click()

# Forgot your password link
# driver.find_element( By.ID, "auth-fpp-link-bottom").click()

# Other issues with Sign-In link
# driver.find_element( By.ID, "ap-other-signin-issues-link").click()

# Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit").click()

# Conditions of use link
# driver.find_element(By.XPATH, "//a[text()='Conditions of Use']").click()

# Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']").click()

# driver.quit()

