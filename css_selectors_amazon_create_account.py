from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/Users/Vitaliy/careerist/Automation/python-selenium-automation/chromedriver.exe')

driver.get('https://www.amazon.com/')

# Sign in page opens
driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList-nav-line-1")

# Create your Amazon account page opens
driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit")

# Amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")

# Create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Your name
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Mobile number or email
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Re-enter password
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# Continue
driver.find_element(By.CSS_SELECTOR, "#continue")

# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_condition_of_use']")

# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice']")

# Sign in
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid.pape.max_auth_age']")


