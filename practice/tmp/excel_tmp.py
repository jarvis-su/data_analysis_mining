import pandas as pd

xls_file = pd.ExcelFile("../3/data/catering_dish_profit.xls")
print(xls_file.sheet_names)

table1 = xls_file.parse("Sheet1")
print(table1)