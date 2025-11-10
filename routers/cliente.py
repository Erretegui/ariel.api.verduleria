from fastapi import APIRouter,Depends
import psycopg
from managers.clientemanager import clientemanager
from managers.conexionManagerSupaBase import getCursor
from models import cliente


router= APIRouter (prefix="/cliente", tags=["clientes routers"])

clientManager = clientemanager()


@router.post("/crear_cliente")
def postCliente(cliente: cliente, cursor: psycopg.Cursor = Depends(getCursor)):
    res = clientManager.addClient(cliente, cursor)
    return {"msg": res}

@router.get("/obtener_clientes")
async def obtener_cliente(cursor: psycopg.Cursor = Depends(getCursor)):
    return clientManager.obtenerCliente(cursor)

