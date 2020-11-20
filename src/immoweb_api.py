import re

import demjson

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
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
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)

            driver.get(annonce_url)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            driver.close()

            # script = soup.find_all('script')[1].contents[0]
            script = soup.find_all('div', class_='classified')[0].find('script').next


            # Step 1: remove all spaces, new lines and tabs
            script = (re.sub('[\s+;]', '', script))

            # Step 2: convert string to dictionary. Creates a key as "digitalData"
            js_dict = script.replace('window.classified=','')
            js_dict = re.sub(r"\bwindow(.*?),\b", '"",', js_dict)
            my_property_dict = demjson.decode(js_dict)

            return self.get_property_detail(my_property_dict)
        except Exception as e:
            print(f'[!] Information not retrieved from {annonce_url}')
            print(f'Error : {type(e)}\nError message : {e}')
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
        id = dictionary['id']
        locality = dictionary['property']['location']['postalCode']
        type_of_property = dictionary['property']['type']
        subtype_of_property = dictionary['property']['subtype']
        price = dictionary['transaction']['sale']['price']
        type_of_sale = dictionary['transaction']['type']
        nr_of_rooms = dictionary['property']['bedroomCount']
        area = dictionary['property']['netHabitableSurface']
        if not dictionary['property']['kitchen'] is None:
            equiped_kitchen = dictionary['property']['kitchen']['type']
        else:
            equiped_kitchen = None
        if not dictionary['transaction']['sale'] is None:
            furnished = dictionary['transaction']['sale']['isFurnished']
        else:
            furnished = None
        open_fire = dictionary['property']['fireplaceExists']
        terrace = dictionary['property']['hasTerrace']
        terrace_area = dictionary['property']['terraceSurface']
        garden = dictionary['property']['hasGarden']
        garden_area = dictionary['property']['gardenSurface']
        if not dictionary['property']['land'] is None:
            total_land_area = dictionary['property']['land']['surface']
        else:
            total_land_area = None
        if not dictionary['property']['building'] is None:
            nr_of_facades = dictionary['property']['building']['facadeCount']
            building_condition = dictionary['property']['building']['condition']
        else:
            nr_of_facades = None
            building_condition = None
        swimming_pool = dictionary['property']['hasSwimmingPool']

        # Create the return object instance
        my_property_detail = PropertyDetail(id,
                                            locality, type_of_property,
                                            subtype_of_property, price,
                                            type_of_sale, nr_of_rooms,
                                            area, equiped_kitchen,
                                            furnished, open_fire,
                                            terrace, terrace_area,
                                            garden, garden_area,
                                            total_land_area, nr_of_facades,
                                            swimming_pool, building_condition)

        return my_property_detail
