from src.immoweb_api import ImmowebAPI

if __name__ == "__main__":
    my_immoweb_api = ImmowebAPI()
    # Get list on 1st Page
    list_url = my_immoweb_api.get_properties_list()
    for annonce_url in list_url:
        try:
            my_immoweb_api.get_properties_detail(annonce_url)
        except Exception as e:
            print(f'unable to retrieve info from this URL : {annonce_url}\nError message : {e}')
