import pandas as pd

xls_file = pd.ExcelFile("C:/Users/SuJie/Desktop/tmp/2018-12-06OCR.xls")
print(xls_file.sheet_names)

table1 = xls_file.parse("Sheet1")
# print(table1)