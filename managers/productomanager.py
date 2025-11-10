import psycopg
from models import producto

class Productomanager:

    def AgregarProducto(self, producto:producto, cursor:psycopg.cursor):
        cursor.execute("INSERT INTO producto (id_producto, nombre, precio) VALUES (%s, %s, %s)", (producto.id_producto, producto.nombre, producto.precio))
        return{"msg": "producto agregado"}


    def obtenerProducto(self, cursor:psycopg.cursor):
        res = cursor.execute("SELECT id_producto, nombre, precio FROM producto").fetchall()
        return [{"id_producto": row [0],  "nombre": row [1], "precio": row [2]} for row in res]