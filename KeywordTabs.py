from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

keyword = input("Keyword: ")
driver = webdriver.Chrome(options=chrome_options)

# One depth sites
websites = []

with open('oneDepth.txt', 'r') as txtfile:
    for line in txtfile:
        website_data = line.strip().split(',')
        websites.append(tuple(website_data))

for url, attribute, value in websites:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    search_input = driver.find_element(by=attribute, value=value)
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)

# Two depth sites
websites = []

with open('twoDepth.txt', 'r') as txtfile:
    for line in txtfile:
        website_data = line.strip().split(',')
        websites.append(tuple(website_data))

for url, attributeOne, attribute, value in websites:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    driver.find_element(By.CLASS_NAME, attributeOne).click()
    search_input = driver.find_element(by=attribute, value=value)
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)

# driver.quit()
