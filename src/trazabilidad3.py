import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=10.128.0.203;"
    "DATABASE=Produccion_BD;"
    "UID=reader;"
    "PWD=sololectura;"
    "TrustServerCertificate=yes;"
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Obtener OF activa ---
consulta_of = """
    SELECT xIdOF, xIdGrupo
    FROM imp.tb_tubo_orden
    WHERE xActivada <> 0
    AND xIdMaquina = ?
"""
cursor.execute(consulta_of, ('MTT1',))
fila = cursor.fetchone()
xIdOF = fila.xIdOF if fila else None
xIdGrupo = fila.xIdGrupo if fila else None
print(f'Máquina MTT1 sin trazabilidad. OF activa: {xIdOF}. Grupo {xIdGrupo}')

cursor.close()
conn.close()