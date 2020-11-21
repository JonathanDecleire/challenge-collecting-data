import re
from threading import Thread, RLock
from time import sleep

from src.immoweb_api import ImmowebAPI
from src.property_detail import PropertyDetail
from src.database import Database


class DataCollector():
    def __init__(self, page_limit: int = None,
                 max_threads: int = 5,
                 database_name: str = 'immoweb_scrapped.csv'):
        self.page_limit = page_limit
        self.max_threads = max_threads
        self.database = Database(database_name)

    def start(self):
        my_immoweb_api = ImmowebAPI()
        # Load first page
        page_num = 1
        print(f'[i] Load result page {page_num}')
        list_url = my_immoweb_api.get_properties_list()

        # Loop while found links to scrap
        # and page limit not reached
        active_threads = []
        while len(list_url) > 0:
            print(f'[i] urls found : {len(list_url)}')
            # Scrap each url retrieved
            for annonce_url in list_url:
                # Get annonce ID from url
                annonce_id = int(re.findall('/(\d+)',annonce_url)[-1])
                # Load a search only if id not already loaded in the database
                if not self.database.id_exists(annonce_id):
                    # Max Threads limitation - wait
                    while len(active_threads) >= self.max_threads:
                        for x in active_threads:
                            if not x.is_alive():
                                active_threads.remove(x)
                    # Launch a new thread
                    collector_thread = DataCollectorThread(annonce_url, self.database)
                    collector_thread.start()
                    active_threads.append(collector_thread)
                    sleep(3)  # To sequence the multithreading
                else:
                    print(f'******** {annonce_id} - already exist')

            # Load next page
            if self.page_limit is None or page_num < self.page_limit:
                page_num += 1
                print(f'[i] Load result page {page_num}')
                list_url = my_immoweb_api.get_properties_list(page_num)
            else:
                break  # Kill the loop if limit reached

        # Wait the end of all active Threads
        for x in active_threads:
            x.join()

        # Save the data base to file
        self.database.save()


lock_database = RLock()


class DataCollectorThread(Thread):
    def __init__(self, annonce_url: str, database: Database):
        Thread.__init__(self)
        self.annonce_url = annonce_url
        self.immoweb_api = ImmowebAPI()
        self.database = database

    def run(self):
        my_detail = self.immoweb_api.get_properties_detail(self.annonce_url)
        if isinstance(my_detail, PropertyDetail):
            with lock_database:
                self.database.add_property_detail(my_detail)
