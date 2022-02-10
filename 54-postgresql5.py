import psycopg2

conexion=psycopg2.connect(user='postgres',
                          host='127.0.0.1',
                          password='admin',
                          port='5432',
                          database='test_db')


try:
    with conexion:
        with conexion.cursor() as cursor:
            #nota si queremos actualizar varios registros a la vez
            #debemos hacer lo mismo que cuando insertamos varios 
            #registros solo hacer un atuplas de tupla y cambiar 
            #el executemany (importante al final de la tupla colocar, 1 0 2 ect )
            #actualizar un registro
            sentencia='UPDATE persona SET nombre=%s,apellido=%s , email=%s WHERE id_persona=%s'
            valores=('juan pablo','juarez','j@juarez',1)
            cursor.execute(sentencia,valores)
            registros_actualizados=cursor.rowcount
            print(f'registros actualizados: {registros_actualizados}')
except Exception as e:
    print(f'ocurrio un error : {e}')
finally:
    conexion.close()