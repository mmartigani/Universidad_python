
import psycopg2

conexion = psycopg2.connect(user='postgres',
                            host='127.0.0.1',
                            password='admin',
                            port='5432',
                            database='test_db')
#print(conexion)
#creamos un cursor que nos permite ejecutar secuencias sql en postgres

cursor=conexion.cursor()
sentencia='SELECT * FROM persona'
cursor.execute(sentencia)
registros=cursor.fetchall()
print(registros)

cursor.close()
conexion.close()



