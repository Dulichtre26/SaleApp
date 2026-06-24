import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="12345",
        database="saledb"
    )

    print("Connected!")
    conn.close()

except Exception as e:
    print(type(e))
    print(e)