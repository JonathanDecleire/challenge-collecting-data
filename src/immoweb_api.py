import re

import demjson

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from typing import Dict, List

from src.property_detail import PropertyDetail


class ImmowebAPI:
    """
    This class allows to scrap the website www.immoweb.be
    By default, the 'base_search_url' includes all house and appartment
    """

    def __init__(self):
        """
        Default constructor
        """
        self.base_search_url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE&page={}&orderBy=relevance"
        pass

    def get_properties_list(self, page_num: int = 1) -> List[str]:
        """
        This function will return the list of properties url found
        on a immoweb search page

        :param page_num : int that representq the page number to inspect
                          If not set, it will be set to 1
        :return         : list of url founded in class "card__title-link"
                          It will be empty if the page is not accessible
                          or if there is no annonce link on the page
        """
        properties_list = []
        # Instanciation of a Headless Firefox driver
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        try:
            # Load the search url with the specified page number
            driver.get(self.base_search_url.format(page_num))
            soup = BeautifulSoup(driver.page_source, "lxml")
            # Collect the links to the annonce links
            for a in soup.find_all("a", attrs={"class": "card__title-link"}):
                properties_list.append(a["href"])
        except Exception:
            # The page scrapping encoured a problem
            # Problem of URL or page index over maximum
            pass

        driver.quit()
        return properties_list

    def get_properties_detail(self, annonce_url: str) -> PropertyDetail:
        """
        This function will return the detail of a property found in
        an 'immoweb annonce' page

        :param annonce_url : url of the annonce
        :return            : PropertyDetail that represents the detail
                             None if error during the scrap process
        """
        try:
            # Instanciation of a Headless Firefox driver
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            # Load the specified annonce
            driver.get(annonce_url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            driver.quit()

            # Extract the javascript containing the property detail infos
            script = soup.find_all("div", class_="classified")[0].find("script").next

            # Convert the javascript to a dictionnary
            # Step 1: remove all spaces, new lines and tabs
            script = re.sub("[\s+;]", "", script)
            # Step 2: remove not desired string
            js_dict = script.replace("window.classified=", "")
            js_dict = re.sub(r"\bwindow(.*?),\b", '"",', js_dict)
            # Step 3: convert the clean string to dict
            my_property_dict = demjson.decode(js_dict)

            # Create and return the PropertyDetail
            return self.get_property_detail(my_property_dict)
        except Exception as e:
            # Uncepted exception -> add info in the terminal
            print(f"[!] Information not retrieved from {annonce_url}")
            print(f"Error : {type(e)}\nError message : {e}")
            return None

    def get_property_detail(self, dictionary: Dict) -> PropertyDetail:
        """
        This function will create a PropertyDetail instance from the
        dico scrapped in the immoweb javascript

        :param dictionary: the scrapped dictionnary on immoweb
        :return          : An instance of PropertyDetail that will contain
                           all detail of the property
        """
        # Extracts dictionary infos
        id = dictionary["id"]
        locality = dictionary["property"]["location"]["postalCode"]
        type_of_property = dictionary["property"]["type"]
        subtype_of_property = dictionary["property"]["subtype"]
        price = dictionary["transaction"]["sale"]["price"]
        type_of_sale = dictionary["transaction"]["type"]
        nr_of_rooms = dictionary["property"]["bedroomCount"]
        area = dictionary["property"]["netHabitableSurface"]
        if not dictionary["property"]["kitchen"] is None:
            equiped_kitchen = dictionary["property"]["kitchen"]["type"]
        else:
            equiped_kitchen = None
        if not dictionary["transaction"]["sale"] is None:
            furnished = dictionary["transaction"]["sale"]["isFurnished"]
        else:
            furnished = None
        open_fire = dictionary["property"]["fireplaceExists"]
        terrace = dictionary["property"]["hasTerrace"]
        terrace_area = dictionary["property"]["terraceSurface"]
        garden = dictionary["property"]["hasGarden"]
        garden_area = dictionary["property"]["gardenSurface"]
        if not dictionary["property"]["land"] is None:
            total_land_area = dictionary["property"]["land"]["surface"]
        else:
            total_land_area = None
        if not dictionary["property"]["building"] is None:
            nr_of_facades = dictionary["property"]["building"]["facadeCount"]
            building_condition = dictionary["property"]["building"]["condition"]
        else:
            nr_of_facades = None
            building_condition = None
        swimming_pool = dictionary["property"]["hasSwimmingPool"]

        # Create the return object instance
        my_property_detail = PropertyDetail(
            id,
            locality,
            type_of_property,
            subtype_of_property,
            price,
            type_of_sale,
            nr_of_rooms,
            area,
            equiped_kitchen,
            furnished,
            open_fire,
            terrace,
            terrace_area,
            garden,
            garden_area,
            total_land_area,
            nr_of_facades,
            swimming_pool,
            building_condition,
        )

        return my_property_detail
