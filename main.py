import pandas

from src.data_collector import DataCollector
from src.property_detail import PropertyDetail

if __name__ == "__main__":
    list_pd = []
    pd = PropertyDetail('Bruxelles', 'type_of_property', 'subtype_of_property',
                        350000, 'type_of_sale', 3, 100, True, False, False, False,
                        None, True, 300, 350, 4, False, 'HAS_NEW')
    list_pd.append(pd)
    print(((((((((())))))))))
    pd = PropertyDetail('Waremme', 'type_of_property', 'subtype_of_property',
                        350000, 'type_of_sale', 3, 100, True, False, False, False,
                        None, True, 300, 350, 4, False, 'HAS_NEW')
    list_pd.append(pd)
    df = pandas.DataFrame([d.__dict__() for d in list_pd])

    pd = PropertyDetail('Liege', 'type_of_property', 'subtype_of_property',
                        350000, 'type_of_sale', 3, 100, True, False, False, False,
                        None, True, 300, 350, 4, False, 'HAS_NEW')

    df = df.append(pd.__dict__(), ignore_index=True)

    df2 = pandas.DataFrame([pd.__dict__()])


    print(df)

    dfs = pandas.read_excel('import_to_excel.xlsx', sheet_name='Sheet1')
    print(dfs)
    '''
    # Start the Data Collection
    my_data_collector = DataCollector(2)

    print('[i] Start DataColector')

    my_data_collector.start()

    print('[i] End DataColector')
    '''
    '''
    # DEBUG MODE - TO TEST A SPECIFIC URL
    annonce_url = 'https://www.immoweb.be/fr/annonce/studio/a-vendre/uccle/1180/8997289?searchId=5fb59dc213eae'
    my_immoweb_api.get_properties_detail(annonce_url)
    '''
