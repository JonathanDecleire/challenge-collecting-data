import pandas
import os

from typing import List

from src.property_detail import PropertyDetail


class Database:
    """
    Class that will manages the database
    """

    def __init__(self, database_file: str):
        """
        Default constructor

        :param database_file : str that set the csv database filename
        """
        self.database_file = database_file
        # Load the database if exists
        if os.path.isfile(database_file):
            self.data_frame = pandas.read_csv(database_file)
        # Or create an empty one
        else:
            self.data_frame = pandas.DataFrame()

    def add_property_detail(self, property_detail: PropertyDetail):
        """
        This method add an PropertyDetail to the database

        :param property_detail : PropertyDetail to add to de database
        """
        print(f"[i] Add {property_detail.id}")
        if self.data_frame.empty:
            # If the DataFrame is empty, create a new one
            data = property_detail.to_dict()
            self.data_frame = pandas.DataFrame([data], columns=data.keys())
        else:
            # Append the PropertyDetail to the database
            self.data_frame = self.data_frame.append(
                property_detail.to_dict(), ignore_index=True
            )

    def save(self):
        """
        This method save the database to the csv file
        """
        self.data_frame.to_csv(self.database_file, index=False)

    def id_exists(self, id: int) -> bool:
        """
        This function check if a specific annonce ID is already in
        the database

        :return : bool True if exists
        """
        if self.data_frame.empty:
            return False
        return id in self.data_frame["id"].to_list()
