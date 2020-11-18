import re

import bs4
import requests
import selenium

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ImmowebAPI():
    def __init__(self):
        self.base_url = 'https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE&page=###&orderBy=relevance'
        pass

    def get_properties_list(self):
        driver = webdriver.Firefox()
        driver.get(self.base_url.replace('##', '1'))
        soup = BeautifulSoup(driver.page_source)
        for lien in soup.find_all('a', attrs={"class": "card__title-link"}):
            print(lien)
