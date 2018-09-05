import json
import time
from typing import Iterable

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def google(keyword: str, limit=100) -> Iterable[str]:
    """Search in google search engine

    Args:
         keyword: keyword for search
         limit: limit image scrap

    Return:
        List of image url
    """
    keyword = keyword.replace(" ", "+")
    url = f'https://www.google.co.in/search?q={keyword}&source=lnms&tbm=isch'

    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)

    body = browser.find_element_by_tag_name("body")

    page = 20
    for _ in range(page):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    images = browser.find_elements_by_class_name("rg_meta")
    for image in images[:limit]:
        json_content = image.get_attribute('innerHTML')
        yield json.loads(json_content)["ou"]

    browser.close()
