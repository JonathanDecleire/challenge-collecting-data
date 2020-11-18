from src.immoweb_api import ImmowebAPI

if __name__ == "__main__":
    my_immoweb_api = ImmowebAPI()
    # Get list on 1st Page
    list_url = my_immoweb_api.get_properties_list()
    for annonce_url in list_url:
        my_immoweb_api.get_properties_detail(annonce_url)
