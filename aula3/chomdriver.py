from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C://Users/guste/Downloads/chromedriver.exe')
driver.get("https://www.google.com.br")