from typing import List

from src.property_detail import PropertyDetail

import xlsxwriter


class Database():
    '''
    Class ...
    '''
    def __init__(self, database_file: str):
        
        try:
          open('import_to_excel.xlsx')
        except 
    
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
        

    def add_property_detail(self, property_detail: PropertyDetail):
        
         # Start from the first cell below the headers.
        row = 1
        col = 0

        worksheet.write_string  (worksheet.dim_rowmax + 1, col, property_detail.locality)
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 1, property_detail.type_of_property)
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 2, property_detail.subtype_of_property)
        worksheet.write_number  (worksheet.dim_rowmax + 1, col + 3, property_detail.price, money_format)
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 4, property_detail.type_of_sale)
        worksheet.write_number  (worksheet.dim_rowmax + 1, col + 5, property_detail.nr_of_rooms)
        worksheet.write_number  (worksheet.dim_rowmax + 1, col + 6, property_detail.area)
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 7, property_detail.equipped_kitchen)   
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 8, property_detail.furnished)
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 9, property_detail.open_fire)
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 10, property_detail.terrace)
        worksheet.write_number  (worksheet.dim_rowmax + 1, col + 11, property_detail.terrace_area)
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 12, property_detail.garden)
        worksheet.write_number  (worksheet.dim_rowmax + 1, col + 13, property_detail.garden_area)
        worksheet.write_number  (worksheet.dim_rowmax + 1, col + 14, property_detail.total_land_area)
        worksheet.write_number  (worksheet.dim_rowmax + 1, col + 15, property_detail.nr_of_facades)
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 16, property_detail.swimming_pool)
        worksheet.write_string  (worksheet.dim_rowmax + 1, col + 17, property_detail.building_condition)


workbook.close()
        

    def load_database(self) -> List[PropertyDetail]:
        pass
    
    
    




 

