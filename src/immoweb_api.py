import re

import demjson

from bs4 import BeautifulSoup
from selenium import webdriver
from typing import Dict, List

from src.property_detail import PropertyDetail


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
        try:
            driver.get(self.base_search_url.format(page_num))
            soup = BeautifulSoup(driver.page_source, 'lxml')
            for a in soup.find_all('a', attrs={"class": "card__title-link"}):
                properties_list.append(a['href'])
        except Exception:
            # The page scrapping encoured a problem
            # Problem of URL or page index over maximum
            pass
        driver.close()
        return properties_list

    def get_properties_detail(self, annonce_url: str) -> PropertyDetail:
        '''
        This function will return the detail of a property found in
        an 'immoweb annonce' page

        :param annonce_url : url to call
        :return : an object that represent the detail
        '''
        print('[i] get info from ' + annonce_url)
        try:
            driver = webdriver.Firefox()
            driver.get(annonce_url)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            driver.close()

            script = soup.find_all('script')[1].contents[0]

            # Step 1: remove all spaces, new lines and tabs
            script = (re.sub('[\s+;]', '', script))

            # Step 2: convert string to dictionary. Creates a key as "digitalData"
            js_dict = script.split("=")[1]
            js_dict = re.sub(r"\bwindow(.*?),\b", '"",', js_dict)
            my_property_dict = demjson.decode(js_dict)[0]['classified']

            print('[i] Information retrieved from ' + annonce_url)
            return self.get_property_detail(my_property_dict)
        except Exception as e:
            print(f'[!] Information not retrieved from {annonce_url}\nError message : {e}')
            return None


    def get_property_detail(self, dictionary: Dict) -> PropertyDetail:
        '''
        This function will create a PropertyDetail instance from the
        dico scrapped in the immoweb javascript

        :param dictionary: the scrapped dictionnary on immoweb
        :return : An instance of PropertyDetail that will contain
                  all detail of the property
        '''
        # Extract dictionary infos
        if len(dictionary['zip']) > 0:
            locality = dictionary['zip']
        else:
            locality = None
        if len(dictionary['type']) > 0:
            type_of_property = dictionary['type']
        else:
            type_of_property = None
        if len(dictionary['subtype']) > 0:
            subtype_of_property = dictionary['subtype']
        else:
            subtype_of_property = None
        if len(dictionary['price']) > 0:
            price = dictionary['price']
        else:
            price = None
        if len(dictionary['transactionType']) > 0:
            type_of_sale = dictionary['transactionType']
        else:
            type_of_sale = None
        if len(dictionary['bedroom']['count']) > 0:
            nr_of_rooms = dictionary['bedroom']['count']
        else:
            nr_of_rooms = None
        area = None  # ...
        if len(dictionary['kitchen']['type']) > 0:
            equiped_kitchen = dictionary['kitchen']['type']
        else:
            equiped_kitchen = None
        furnished = None  # ...
        open_fire = None  # ...
        if dictionary['outdoor']['exists'] == 'true' :
            terrace = True
            terrace_area = None #...
        else:
            terrace = False
        garden = None  # ...
        if len(dictionary['outdoor']['garden']['surface']) > 0:
            garden_area = dictionary['outdoor']['garden']['surface']
        else:
            garden_area = None
        if len(dictionary['land']['surface']) >= 0:
            total_land_area = dictionary['land']['surface']
        else:
            total_land_area = None
        nr_of_facades = None  # ...
        if len(dictionary['wellnessEquipment']['hasSwimmingPool']) > 0:
            swimming_pool = dictionary['wellnessEquipment']['hasSwimmingPool']
        else:
            swimming_pool = None
        building_condition = None  #

        # Create the return object instance
        my_property_detail = PropertyDetail(locality, type_of_property,
                                            subtype_of_property, price,
                                            type_of_sale, nr_of_rooms,
                                            area, equiped_kitchen,
                                            furnished, open_fire,
                                            terrace, terrace_area,
                                            garden, garden_area,
                                            total_land_area, nr_of_facades,
                                            swimming_pool, building_condition)

        return my_property_detail
