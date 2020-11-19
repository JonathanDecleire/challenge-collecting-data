from src.data_collector import DataCollector

if __name__ == "__main__":
    # Start the Data Collection
    my_data_collector = DataCollector(2)

    print('[i] Start DataColector')

    my_data_collector.start()

    print('[i] End DataColector')

    '''
    # DEBUG MODE - TO TEST A SPECIFIC URL
    annonce_url = 'https://www.immoweb.be/fr/annonce/studio/a-vendre/uccle/1180/8997289?searchId=5fb59dc213eae'
    my_immoweb_api.get_properties_detail(annonce_url)
    '''
