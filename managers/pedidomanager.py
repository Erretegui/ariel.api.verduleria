import psycopg
from models import pedido  

class Pedidomanager:

    def Agregarpedido(self, pedido:pedido, cursor:psycopg.cursor):
        cursor.execute("INSERT INTO pedido ( id_cliente, id_producto) VALUES (%s, %s)", ( pedido.id_cliente, pedido.id_producto))
        return{"msg": "pedido agregado"}
    
    def obtenerPedido(self, cursor:psycopg.cursor):
        res = cursor.execute("SELECT id_cliente, id_producto  FROM pedido").fetchall()
        return [{"id_cliente": row [0],  "id_producto": row [1]} for row in res]
    

    def eliminarPedido(self, id_pedido:int, cursor:psycopg.cursor) -> str:
        cursor.execute("DELETE FROM pedido WHERE id_producto = %s", (id_pedido,))
        return "Pedido eliminado"