# Programa para probar la conexión a la base de datos de producción
# Lee la tabla de acumuladores y filtra los flejes que corresponden a la MTT2
import pyodbc

def es_maquina2(mtt):
    return mtt[5] == 'MTT2'

consultaSQL = 'select a.xIdPos, a.xIdFleje, a.xIdArticulo, a.xPeso, a.xIdOF, xIdMaquina, art.xdescripcion from imp.tb_tubo_acumulador a inner join imp.tb_tubo_orden o on a.xIdOF = o.xIdOF  left join F126_DATA.imp.pl_articulos art on art.xarticulo_id = a.xIdArticulo' 

try:
    conexion = pyodbc.connect('DRIVER={SQL Server}; SERVER=10.128.0.203;DATABASE=Produccion_BD;UID=reader;PWD=sololectura')
    print('Conexion OK')
    cursor = conexion.cursor()
    cursor.execute(consultaSQL)
    rows = cursor.fetchall()
    flejes = filter(es_maquina2, rows)
    for fleje in flejes:
        print(fleje)

except Exception as Ex:
    print(Ex)

finally:
    conexion.close()
    print('Fin ...')