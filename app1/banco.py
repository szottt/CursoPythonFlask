import pymysql

connection = pymysql.connect(user='x', passwd='x',
                                 Host='x',
                                 database='x')

cursor = connection.cursor()

query = ("MYQUERY")

cursor.execute(query)

for item in cursor:
    print item