from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox(executable_path='geckodriver')
opts = Options()
opts.set_headless()
assert opts.headless
browser = Firefox(options=opts)
driver.get('https://duckduckgo.com')