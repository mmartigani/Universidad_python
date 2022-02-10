import psycopg2

conexion=psycopg2.connect(user='postgres',
                          host='127.0.0.1',
                          password='admin',
                          port='5432',
                          database='test_db')

#con with nos permite que se cierre automaticamente
try:
    with conexion:
        with conexion.cursor() as cursor:
            #sentencia='SELECT * FROM persona' #muestra toda la tabla
            sentencia='SELECT * FROM persona WHERE id_persona=3'#solo el registro 3
            cursor.execute(sentencia)
            registros=cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'ocurrio un error : {e}')
finally:
    conexion.close()
    