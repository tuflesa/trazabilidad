# Programa que lee los flejes en los acumuladores y los envía al backend 
# para actualizar la tabla de flejes
import requests
import pyodbc
import time

consultaSQL = 'select a.xIdPos, a.xIdFleje, a.xIdArticulo, a.xPeso, a.xIdOF, xIdMaquina, art.xdescripcion from imp.tb_tubo_acumulador a inner join imp.tb_tubo_orden o on a.xIdOF = o.xIdOF  left join F126_DATA.imp.pl_articulos art on art.xarticulo_id = a.xIdArticulo WHERE xPesoConsumido = 0 and xTrazabilidad = 0' 

SERVER = 'http://10.128.100.242:8000/'
# SERVER = 'http://localhost:8000/'
HEADERS = {'Authorization': 'token 7e3f7c728e4b6c68de306db3da6e321f43222201'}

while (True):
    # Lee los datos de la base de datos de producción
    lectura_ProduccionDB_OK = True
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.128.0.203;DATABASE=Produccion_BD;UID=reader;PWD=sololectura')
        print('Conexion OK')
        cursor = conexion.cursor()
        cursor.execute(consultaSQL)
        flejes = cursor.fetchall()
        datos = []
        for fleje in flejes:
            f = {
                'pos': fleje[0],
                'idProduccion': fleje[1],
                'IdArticulo': fleje[2],
                'peso': fleje[3],
                'of': fleje[4],
                'maquina_siglas': fleje[5],
                'descripcion': fleje[6]
            }
            datos.append(f)

    except Exception as Ex:
        lectura_ProduccionDB_OK = False
        print(Ex)

    finally:
        if lectura_ProduccionDB_OK:
            conexion.close()
            print('Conexion cerrada')
        else:
            print('Error de lectura en produccionDB ...')

    if lectura_ProduccionDB_OK :
        try:
            r = requests.post(SERVER + 'api/trazabilidad/leerFlejes/', 
                json = datos,
                headers = HEADERS
                )
            if(r.status_code == 201):
                print('Datos enviados')
        except Exception as ex:
            print('Error al escribir en servidor')
            print(ex)
    
    time.sleep(10)