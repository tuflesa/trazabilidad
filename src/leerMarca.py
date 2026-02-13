import snap7
from snap7.util import get_bool

# Crear cliente
client = snap7.client.Client()

# Conectar al PLC (IP, rack, slot)
client.connect('10.128.1.140', 0, 1)

# Leer un bloque de memoria que contenga la marca deseada
# M11.2 está en el byte 11, bit 2
# Por lo tanto, leemos al menos 1 byte desde la dirección 11
data = client.read_area(snap7.type.Areas.MK, 0, 11, 1)

# Extraer el bit 2 del byte leído
valor = get_bool(data, 0, 2)

print("M11.2 =", valor)

# Cerrar conexión
client.disconnect()