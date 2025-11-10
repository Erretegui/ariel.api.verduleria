import psycopg
from models import cliente

class clientemanager:

    def addClient(self, cliente:cliente, cursor:psycopg.Cursor):
        cursor.execute(
            "INSERT INTO cliente (nombre, apellido) VALUES (%s,%s)",
            (cliente.nombre, cliente.apellido)
        )
        return f"cliente creado"
    

    def obtenerCliente(self, cursor:psycopg.Cursor):
        res = cursor.execute("SELECT id_cliente, nombre, apellido FROM cliente").fetchall()
        return [{"id": row [0],  "nombre": row [1], "apellido": row [2]} for row in res]
    

        
    def deleteClient(self, id: int, cursor: psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM cliente WHERE id = %s", (id,))
        return "Cliente eliminado"

