from fastapi import APIRouter, Depends
from managers.conexionManagerSupaBase import getCursor
from managers.pedidomanager import Pedidomanager
from models import pedido
import psycopg 



router = APIRouter(prefix="/pedido", tags=["pedido"])
pedidoManager = Pedidomanager()

@router.post("/agregar_pedido")
async def Agregar_pedido (pedido: pedido , cursor:psycopg.Cursor=Depends(getCursor)):
    res = pedidoManager.Agregarpedido (pedido, cursor)
    return res
 


@router.get("/obtener_pedido")
async def obtener_pedido (cursor:psycopg.Cursor=Depends(getCursor)):
    res = pedidoManager.obtenerPedido (cursor)
    return res

@router.delete("/eliminar/{id_pedido}")
async def eliminar_cuidador(id_pedido: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return pedidoManager.eliminarPedido(id_pedido, cursor)