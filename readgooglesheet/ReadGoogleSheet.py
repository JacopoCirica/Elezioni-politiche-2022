import gspread
import pandas as pd 
from oauth2client.service_account import ServiceAccountCredentials
scopes=[
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds= ServiceAccountCredentials.from_json_keyfile_name('//Users/macssd//Desktop//Pythonproject//data//sole24ore-7af9d91f2757.json', scopes=scopes)
file= gspread.authorize(creds)
workbook= file.open('Indecis')
sheet=workbook.sheet1
#print(sheet.range('A2:A5'))
colonna1=[]
colonna=[]
for cell in sheet.range('J2:J141'):
    colonna1.append(cell.value)
#print(colonna1)
for cell in sheet.range ('M2:M141'):
    colonna.append(cell.value)
print(colonna)
data = {'pd_description': colonna1, 'avs_description': colonna} 
df=pd.DataFrame(data=data)
print(df)
df.to_json('/Users/macssd/Desktop/prova1.json')
