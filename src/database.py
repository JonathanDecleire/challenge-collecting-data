from typing import List

from src.property_detail import PropertyDetail


class Database():
    '''
    Class ...
    '''
    def __init__(self, database_file: str):
        self.dfs = pandas.read_excel(database_file, sheet_name='Sheet1')

    def add_property_detail(self, property_detail: PropertyDetail):
        pass

    def load_database(self) -> List[PropertyDetail]:
        pass