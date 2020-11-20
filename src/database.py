import pandas
import os

from typing import List

from src.property_detail import PropertyDetail


class Database():
    '''
    Class ...
    '''
    def __init__(self, database_file: str):
        self.database_file = database_file
        if os.path.isfile(database_file):
            self.data_frame = pandas.read_csv(database_file)
        else:
            self.data_frame = pandas.DataFrame()

    def add_property_detail(self, property_detail: PropertyDetail):
        if self.data_frame.empty:
            data = property_detail.to_dict()
            self.data_frame = pandas.DataFrame([data], columns=data.keys())
        else:
            self.data_frame = self.data_frame.append(property_detail.to_dict(),
                                                     ignore_index=True)

    def save(self):
        self.data_frame.to_csv(self.database_file, index=False)

    def id_exists(self, id: int) -> bool:
        if self.data_frame.empty:
            return False
        return id in self.data_frame['id'].to_list()
