# import requests
# from bs4 import BeautifulSoup
#
# __author__ = "Engine Bai"
# url = "https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228"
#
# req = requests.get(url)
# html = BeautifulSoup(req.text, "html.parser")
# content_tag = html.find("div", attrs={"class": "postArticle-content",
#                                       "data-source": "post_page"})
# print(content_tag)

from selenium import webdriver
from bs4 import BeautifulSoup

__author__ = "Engine Bai"
url = "https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228"

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(url)
content_element = driver.find_element_by_class_name("postArticle-content")
content_html = content_element.get_attribute("innerHTML")

soup = BeautifulSoup(content_html, "html.parser")
p_tags = soup.find_all("p")
for p in p_tags:
    print(p.prettify())
driver.close()