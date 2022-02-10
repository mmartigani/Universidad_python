import psycopg2

conexion=psycopg2.connect(user='postgres',
                          host='127.0.0.1',
                          password='admin',
                          port='5432',
                          database='test_db')


try:
    with conexion:
        with conexion.cursor() as cursor:
            #eliminamos un registro
            #sentencia='DELETE FROM persona WHERE id_persona =%s'
            #elimina varios registros
            sentencia='DELETE FROM persona WHERE id_persona IN %s'
            entrada=input('ingrese los id separados por coma: ')
            valores=(tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            registros_eliminados=cursor.rowcount
            print(f'registros eliminados:{registros_eliminados}')
except Exception as e:
    print(f'ocurrio un error : {e}')
finally:
    conexion.close()