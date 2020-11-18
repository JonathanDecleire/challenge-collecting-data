import re

import bs4
import requests
import selenium

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from typing import List


class ImmowebAPI():
    def __init__(self):
        self.base_search_url = 'https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE&page={}&orderBy=relevance'
        pass

    def get_properties_list(self, page_num: int = 1) -> List[str]:
        '''
        This function will return the list of properties url found
        on a immoweb search page

        :param page_num : int that represent the page number to inspect
        :return : a list of url founded in class "card__title-link"
        '''
        properties_list = []
        driver = webdriver.Firefox()
        driver.get(self.base_search_url.format(page_num))
        soup = BeautifulSoup(driver.page_source, 'lxml')
        for a in soup.find_all('a', attrs={"class": "card__title-link"}):
            print(a['href'])
            properties_list.append(a)
        driver.close()
        return properties_list
    
    def get_properties_detail(self):
        pass
