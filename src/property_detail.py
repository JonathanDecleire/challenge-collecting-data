class PropertyDetail():
    def __init__(self,
                 locality: str,
                 type_of_property: str,
                 subtype_of_property: str,
                 price: int,
                 type_of_sale: str,
                 nr_of_rooms: int,
                 area: float,
                 equipped_kitchen: bool,
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
        self.locality = locality  # from bpost list
        self.type_of_property = type_of_property  # ["house", "apartement", "other"]
        self.subtype_of_property = subtype_of_property  # ["bungalow", "chalet", "mansion", "castle", "cottage", "apartment block", "town house", "farm house", "other"]  
        self.price = price
        # self.type_of_sale = on hold
        self.nr_of_rooms = nr_of_rooms
        self.area = area
        self.equipped_kitchen = equipped_kitchen
        self.furnished = furnished
        self.open_fire = open_fire
        self.terrace = terrace
        self.terrace_area = terrace_area  # if terrace == yes
        self.garden = garden
        self.garden_area = garden_area  # if garden == yes
        self.total_land_area = total_land_area
        self.nr_of_facades = nr_of_facades
        self.swimming_pool = swimming_pool
        self.building_condition = building_condition  # ["new", "as new", "just renovated", "good", "to renovate", "to restore", "other"]
