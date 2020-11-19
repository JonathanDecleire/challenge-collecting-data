from typing import List

from src.property_detail import PropertyDetail


class Database():
    '''
    Class ...
    '''
    def __init__(self, database_file: str):
        pass

    def add_property_detail(self, property_detail: PropertyDetail):
        pass

    def load_database(self) -> List[PropertyDetail]:
        pass
    
    
    
import xlsxwriter

 # Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('import_to_excel.xlsx')
worksheet = workbook.add_worksheet()

 # Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

 # Add a number format for cells with money and square.
money_format = workbook.add_format({'num_format': '€#,##0'})

 #Adjust the column width if necessary.
 #worksheet.set_column(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

 # Write the data headers.
worksheet.write('A1', 'locality', bold)
worksheet.write('B1', 'type_of_property', bold)
worksheet.write('C1', 'subtype_of_property', bold)
worksheet.write('D1', 'price', bold)
worksheet.write('D1', 'type_of_sale', bold)
worksheet.write('E1', 'nr_of_rooms', bold)
worksheet.write('F1', 'area', bold)
worksheet.write('G1', 'equipped_kitchen', bold)
worksheet.write('H1', 'furnished', bold)
worksheet.write('I1', 'open_fire', bold)
worksheet.write('J1', 'terrace', bold)
worksheet.write('K1', 'terrace_area', bold)
worksheet.write('L1', 'garden', bold)
worksheet.write('M1', 'garden_area', bold)
worksheet.write('N1', 'total_land_area', bold)
worksheet.write('O1', 'nr_of_facades', bold)
worksheet.write('P1', 'swimming_pool', bold)
worksheet.write('Q1', 'building_condition', bold)

 # Data to be exported.
immos = [property_detail.locality, property_detail.type_of_property, property_detail.subtype_of_property, property_detail.price, property_detail.type_of_sale, property_detail.nr_of_rooms, property_detail.area, property_detail.equipped_kitchen, property_detail.furnished, property_detail.open_fire, property_detail.terrace, property_detail.terrace_area, property_detail.garden, property_detail.garden_area, property_detail.total_land_area, property_detail.nr_of_facades, property_detail.swimming_pool, property_detail.building_condition]
    
     #test (to delete later)
     #['int', 'int', 'int', 0, 'int', 0, 0, 'int', 'int', 'int', 'int', 0, 'int', 0, 0, 0, 'int', 'int'],
     #'int', 'int', 'int', 0, 'int', 0, 0, 'int', 'int', 'int', 'int', 0, 'int', 0, 0, 0, 'int', 'int'],
 

 # Start from the first cell below the headers.
row = 1
col = 0

for locality, type_of_property, subtype_of_property, price, type_of_sale, nr_of_rooms, area, equipped_kitchen, furnished, open_fire, terrace, terrace_area, garden, garden_area, total_land_area, nr_of_facades, swimming_pool, building_condition in (immos):

     worksheet.write_string  (row, col, locality)
     worksheet.write_string  (row, col + 1, type_of_property)
     worksheet.write_string  (row, col + 2, subtype_of_property)
     worksheet.write_number  (row, col + 3, price, money_format)
     worksheet.write_string  (row, col + 4, type_of_sale)
     worksheet.write_number  (row, col + 5, nr_of_rooms)
     worksheet.write_number  (row, col + 6, area)
     worksheet.write_string  (row, col + 7, equipped_kitchen)   
     worksheet.write_string  (row, col + 8, furnished)
     worksheet.write_string  (row, col + 9, open_fire)
     worksheet.write_string  (row, col + 10, terrace)
     worksheet.write_number  (row, col + 11, terrace_area)
     worksheet.write_string  (row, col + 12, garden)
     worksheet.write_number  (row, col + 13, garden_area)
     worksheet.write_number  (row, col + 14, total_land_area)
     worksheet.write_number  (row, col + 15, nr_of_facades)
     worksheet.write_string  (row, col + 16, swimming_pool)
     worksheet.write_string  (row, col + 17, building_condition)
     row += 1


workbook.close()