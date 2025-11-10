from pydantic import BaseModel

class producto(BaseModel):
    id_producto: int
    nombre: str
    precio: int

class pedido(BaseModel):
    id_producto: int
    id_cliente: int
    nombre: str

    
class cliente(BaseModel):
    id_cliente: int
    nombre: str
    apellido: str
    