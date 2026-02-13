import pyodbc

consultaSQL =  """
    SELECT *
    FROM imp.tb_tubo_orden
    WHERE xIdOF = ?
"""

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=10.128.0.203;"
    "DATABASE=Produccion_BD;"
    "UID=reader;"
    "PWD=sololectura;"
    "TrustServerCertificate=yes;"
)
conexion = pyodbc.connect(conn_str)
cursor = conexion.cursor()
cursor.execute(consultaSQL, '26T00025')
fila = cursor.fetchone()
grupo = fila.xIdGrupo
cursor.close()
conexion.close()
print(f'Grupo {grupo}')