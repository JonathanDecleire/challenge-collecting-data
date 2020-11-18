from src.immoweb_api import ImmowebAPI

if __name__ == "__main__":
    my_immoweb_api = ImmowebAPI()
    # Get list on 1st Page
    list_url = my_immoweb_api.get_properties_list()
    print(len(list_url))
    # Get list on 54th Page
    list_url54 = my_immoweb_api.get_properties_list(54)
    print(len(list_url54))
