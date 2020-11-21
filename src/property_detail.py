from typing import Dict


class PropertyDetail():
    '''
    This class represents a real estate property details.
    '''
    def __init__(self,
                 id: int,
                 locality: str,
                 type_of_property: str,
                 subtype_of_property: str,
                 price: int,
                 type_of_sale: str,
                 nr_of_rooms: int,
                 area: float,
                 equiped_kitchen: bool,
                 furnished: bool,
                 open_fire: bool,
                 terrace: bool,
                 terrace_area: float,
                 garden: bool,
                 garden_area: float,
                 total_land_area: float,
                 nr_of_facades: int,
                 swimming_pool: bool,
                 building_condition: str):
        '''
        Default constructor
        '''

        self.id = id
        self.locality = locality
        self.type_of_property = type_of_property
        self.subtype_of_property = subtype_of_property
        self.price = price
        self.type_of_sale = type_of_sale
        self.nr_of_rooms = nr_of_rooms
        self.area = area
        self.equiped_kitchen = equiped_kitchen
        self.furnished = furnished
        self.open_fire = open_fire
        self.terrace = terrace
        self.terrace_area = terrace_area
        self.garden = garden
        self.garden_area = garden_area
        self.total_land_area = total_land_area
        self.nr_of_facades = nr_of_facades
        self.swimming_pool = swimming_pool
        self.building_condition = building_condition

    def to_dict(self) -> Dict:
        '''
        This function will return a dictionnary containing each couple
        variable as key : value of the variable

        :return : a dict that represent the PropertyDetail as key - value
        '''
        return {
                'id': self.id,
                'locality': self.locality,
                'type_of_property': self.type_of_property,
                'subtype_of_property': self.subtype_of_property,
                'price': self.price,
                'type_of_sale': self.type_of_sale,
                'nr_of_rooms': self.nr_of_rooms,
                'area': self.area,
                'equiped_kitchen': self.equiped_kitchen,
                'furnished': self.furnished,
                'open_fire': self.open_fire,
                'terrace': self.terrace,
                'terrace_area': self.terrace_area,
                'garden': self.garden,
                'garden_area': self.garden_area,
                'total_land_area': self.total_land_area,
                'nr_of_facades': self.nr_of_facades,
                'swimming_pool': self.swimming_pool,
                'building_condition': self.building_condition,
               }
