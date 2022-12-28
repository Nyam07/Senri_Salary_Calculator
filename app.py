import os
import gspread
from dotenv import load_dotenv

load_dotenv()

sheet_id = os.getenv('SHEET_ID')
sheet_name = os.getenv('SHEET_NAME')
credentials = os.getenv("CREDENTIALS")



def caluclate_salary(sheet_name, sheet_id, credentials):
    sum = 0
    gc = gspread.service_account(credentials)

    spreadsheet = gc.open_by_key(sheet_id)
    worksheet= spreadsheet.worksheet(sheet_name)

    values_list = worksheet.col_values(6)

    none_empty_list= [item for item in values_list if item]

    # Remove last element
    none_empty_list.pop()

    none_empty_list.remove("Total")

    # replace : with .
    replaced = [s.replace(":", ".") for s in none_empty_list]

    # convert to an integer
    int_list = (list(map(float, replaced)))

    for item in int_list:
        if item == 0.0:
            pass
        elif item < 5.0:
            sum+= 150*item

        else:
            sum += 1100

    return sum

print(f"Total salary is {caluclate_salary(sheet_name, sheet_id, credentials)}")