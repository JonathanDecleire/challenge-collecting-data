from threading import Thread, RLock
from time import sleep

from src.immoweb_api import ImmowebAPI
from src.property_detail import PropertyDetail


class DataCollector():
    def __init__(self, page_limit: int = None, max_threads: int=5):
        self.page_limit = page_limit
        self.max_threads = max_threads

    def start(self):
        my_immoweb_api = ImmowebAPI()
        # Load first page
        list_url = my_immoweb_api.get_properties_list()
        page_num = 1

        # Loop while found links to scrap
        # and page limit not reached
        active_threads = []
        while len(list_url) > 0:
            # Scrap each url retrieved
            for annonce_url in list_url:
                # Max Threads limitation - wait
                while len(active_threads) >= self.max_threads:
                    for x in active_threads:
                        if not x.is_alive():
                            active_threads.remove(x)
                # Launch a new thread
                collector_thread = DataCollectorThread(annonce_url)
                collector_thread.start()
                active_threads.append(collector_thread)
                sleep(1)  # To sequence the multithreading

            # Load next page
            if self.page_limit is None or page_num < self.page_limit:
                page_num += 1
                list_url = my_immoweb_api.get_properties_list(page_num)
            else:
                break  # Kill the loop if limit reached

        # Wait the end of all active Threads
        for x in active_threads:
            x.join()


lock_database = RLock()


class DataCollectorThread(Thread):
    def __init__(self, annonce_url: str):
        Thread.__init__(self)
        self.annonce_url = annonce_url
        self.immoweb_api = ImmowebAPI()

    def run(self):
        my_detail = self.immoweb_api.get_properties_detail(self.annonce_url)
        if isinstance(my_detail, PropertyDetail):
            pass  # TODO DataBase management
