import psycopg
from models import producto, pedido, cliente



class DB:

    def AgregarCliente(self, cliente, cursor:psycopg.cursor):
        cursor.execute("INSERT INTO cliente (id_cliente, nombre) VALUES (%s, %s)", (cliente.id_cliente, cliente.nombre))
        return{"msg": "cliente agregado"}
    
    def obtenerCliente(self, cursor:psycopg.cursor):
        cursor.execute("SELECT * FROM cliente")
        return {"msg":" cliente obtenido."}
    
    
    def eliminarCliente(self, cliente:cliente, cursor:psycopg.cursor):
        cursor.execute("DELETE FROM cliente WHERE id_cliente= %s AND apellido= %s", (cliente.id_cliente, cliente.apellido))
        return {"msg":"cliente eliminado."}
    

    def AgregarProducto(self, producto:producto, cursor:psycopg.cursor):
        cursor.execute("INSERT INTO producto (id_producto, nombre, precio) VALUES (%s, %s, %s)", (producto.id_producto, producto.nombre, producto.precio))
        return{"msg": "producto agregado"}


    def obtenerProducto(self, cursor:psycopg.cursor):
        cursor.execute("SELECT * FROM producto")
        return {"msg":" producto obtenido."}
    

    def AgregarPedido(self, pedido:pedido, cursor:psycopg.cursor):
        cursor.execute("INSERT INTO pedido (id_pedido, id_cliente, id_producto, cantidad) VALUES (%s, %s, %s, %s)", (pedido.id_pedido, pedido.id_cliente, pedido.id_producto, pedido.cantidad))
        return{"msg": "pedido agregado"}
    

    def obtenerPedido(self, cursor:psycopg.cursor):
        cursor.execute("SELECT * FROM pedido")
        return {"msg":" pedido obtenido."}
    

    def eliminarPedido(self, id_pedido:int, cursor:psycopg.cursor):
        cursor.execute("DELETE FROM pedido WHERE id_pedido= %s", (id_pedido,))
        return {"msg":"pedido eliminado."}