import pymysql

DATABASE = {
    'host':'47.95.235.115',
    'database':'jarvis_db',
    'user':'jarvis_db',
    'password':'Jarvis%123456',
    'charset':'utf8'
}


db = pymysql.connect(**DATABASE)
cursor = db.cursor()
sql = "select * from DimProduct limit 1000"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
db.close()

