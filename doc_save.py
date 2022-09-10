import gspread as gspread
from oauth2client.service_account import ServiceAccountCredentials

from cb_rf_course import get_rub_value
from db_methods import save_values, delete_values

gscope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
gcredentials = 'token.json'
gdocument = 'Копия test'
credentials = ServiceAccountCredentials.from_json_keyfile_name(gcredentials, gscope)
gc = gspread.authorize(credentials)
wks = gc.open(gdocument).sheet1


# get values from google sheets and save it to database
def save_db_values():
    delete_values()

    values_list1 = wks.col_values(1)
    values_list2 = wks.col_values(2)
    values_list3 = wks.col_values(3)
    values_list4 = wks.col_values(4)
    x = len(values_list1)
    i = 1
    while i < x:
        save_values(values_list1[i], values_list2[i], values_list3[i], values_list4[i], round(get_rub_value(int(values_list3[i])), 2))
        i += 1
    print("end save values")
    pass
