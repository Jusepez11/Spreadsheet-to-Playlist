import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time

scopeSpreadSheet = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('TestSpreadsheet.json', scopeSpreadSheet)
client = gspread.authorize(creds)

sheet = client.open('Pysheets').sheet1

def red(value, y, x = 2, str_or_int = 0):#red stands for reduction 
    value = str(value)
    if x == 2:
        value = value.replace("<Cell R" + str(y) + "C2 'https://www.youtube.com/watch?v=", "")
    else:
        value = value.replace("<Cell R" + str(y) + "C" + str(x) + " '", "")
    value = value.replace("'>","")
    if str_or_int == 0:
        return int(value)
    elif str_or_int == 1:
        return str(value)

def isOld(value):#this checks if the link had been checked before
    value = str(value)
    if value == 1:
        return True
    else:
        return False

row = 1

while str(sheet.row_values(row)) != "[]":
    for i in range(sheet.row_count):
        print("Start\n")
        row = i+3
        print(row)
        ID = red(sheet.cell(row,2), row, 2, 1)
        if (red(sheet.cell(row, 1), row, 1, 1) != '') and (isOld(red(sheet.cell(row, 5), row, 5, 1)) == False): #sheet.cell(row, 1) == ('<Cell R"+ str(row) +"C1 ''>') and
            sheet.update_cell(row, 4, ID)
            sheet.update_cell(row, 5, 1)
        print(sheet.row_values(row))#Row Values
        print("\nEnd")
        time.sleep(2)

print("The Program Works Correctly")
