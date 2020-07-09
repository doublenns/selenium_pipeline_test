#!/usr/bin/env python3

from selenium import webdriver


# Add options to use
options = webdriver.ChromeOptions()
#options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://scrapethissite.com")
print("URl of current page:", driver.current_url)
print(f"Title of current page: <{driver.title}>")
driver.quit()
