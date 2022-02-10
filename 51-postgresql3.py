import psycopg2

conexion=psycopg2.connect(user='postgres',
                          host='127.0.0.1',
                          password='admin',
                          port='5432',
                          database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            #sentencia='SELECT * FROM persona' #muestra toda la tabla
            #sentencia='SELECT * FROM persona WHERE id_persona IN (1,2,3,4)'
            #muestra los registros que le indiquemos 
            #insertamos un nuevo registro solo 1 a la vez 
            sentencia='INSERT INTO persona(nombre,apellido,email)VALUES(%s, %s, %s)'
            valores =(('oiyt','aaaa','l@aa'),
                      ('reee','bbbb','l@bb'),
                      ('rrrr','cccc','l@cc'))
            #insertamos varios registros no se modifica el query 
            #se modifica la tupla y el metodo executemany
            #cursor.execute(sentencia, valores)
            cursor.executemany(sentencia,valores)
            registros_insertados=cursor.rowcount
            print(f'registros insertados: {registros_insertados}')
            #registros=cursor.fetchall()
            #for registro in registros:
                #print(registros)
except Exception as e:
    print(f'ocurrio un error : {e}')
finally:
    conexion.close()
    