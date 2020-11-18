import re

import bs4
import requests
import selenium
import demjson

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
            properties_list.append(a['href'])
        driver.close()
        return properties_list

    def get_properties_detail(self, annonce_url: str):
        '''
        This function will return the detail of a property found in
        an 'immoweb annonce' page

        :param annonce_url : url to call
        :return : an object that represent the detail
        '''
        driver = webdriver.Firefox()
        driver.get(annonce_url)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        script = soup.find_all('script')[1].contents[0]

        # Step 1: remove all spaces, new lines and tabs
        script = (re.sub('[\s+;]', '', script))

        # Step 2: convert string to dictionary. Creates a key as "digitalData"
        js_dict = script.split("=")[1]
        js_dict = re.sub(r"\bwindow(.*?),\b", '"",', js_dict)
        my_dict = demjson.decode(js_dict)

        # print(my_dict)
        print((my_dict['classified'])['id']) # 9034494
 type(my_dict[0]['classified']['id'])
        driver.close()
