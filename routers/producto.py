from fastapi import APIRouter, Depends
import psycopg 
from managers.productomanager import Productomanager
from managers.conexionManagerSupaBase import getCursor
from models import producto


router = APIRouter(prefix="/producto", tags=["producto"])
productoManager = Productomanager()

@router.post("/crear_producto")
async def crear_habitat(producto: producto, cursor: psycopg.Cursor = Depends(getCursor)):
    return productoManager.AgregarProducto(producto, cursor)


@router.get("/obtener_productos")
async def obtener_producto(cursor:psycopg.Cursor = Depends (getCursor)):
    return productoManager.obtenerProducto(cursor)

