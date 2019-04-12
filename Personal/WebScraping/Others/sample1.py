import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('prosenjit1994')
search_box.submit()
time.sleep(5)# Let the user actually see something!
print(driver.find_element_by_name('q'))
driver.quit()