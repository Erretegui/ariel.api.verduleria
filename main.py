from fastapi import FastAPI
from routers.cliente import router as router_cliente
from routers.pedido import router as router_pedido
from routers.producto import router as router_producto

app = FastAPI()
app.include_router(router_cliente)
app.include_router(router_pedido)
app.include_router(router_producto)