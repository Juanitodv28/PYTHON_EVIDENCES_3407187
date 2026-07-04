from fastapi import APIRouter, HTTPException, status
from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..modelos.facturas import Factura
# Quitamos las listas porque ya todo es por base de datos
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_transacciones = APIRouter()


@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones(sesion: Sesion_dependencia):
    consulta = select(Transaccion)
    lista_transacciones = sesion.exec(consulta).all()
    return lista_transacciones


@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int, sesion: Sesion_dependencia): # Agregamos sesion
    # Buscamos directo en la BD
    transaccion_bd = sesion.get(Transaccion, id_transaccion)

    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transaccion con id {id_transaccion}, no existe."
        )
    return transaccion_bd


@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(
    factura_id: int,
    datos_transaccion: TransaccionCrear,
    sesion: Sesion_dependencia
):
    # buscar la factura
    factura_encontrada = sesion.get(Factura, factura_id)

    # mensaje si no existe la factura
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La Factura con id {factura_id}, no existe.",
        )

    # validar datos de la transaccion
    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["factura_id"] = factura_id
    transaccion_val = Transaccion.model_validate(transaccion_dict)

    # guardar en BD
    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)

    return transaccion_val


@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(
    id_transaccion: int,
    datos_transaccion: TransaccionEditar,
    sesion: Sesion_dependencia # Agregamos sesion
):
    # Buscamos en BD
    transaccion_bd = sesion.get(Transaccion, id_transaccion)

    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transaccion con id {id_transaccion}, no existe."
        )

    # Extraemos los datos a actualizar
    datos_nuevos = datos_transaccion.model_dump(exclude_unset=True)
    for key, value in datos_nuevos.items():
        setattr(transaccion_bd, key, value)

    sesion.add(transaccion_bd)
    sesion.commit()
    sesion.refresh(transaccion_bd)

    return transaccion_bd


@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int, sesion: Sesion_dependencia): # Agregamos sesion
    # Buscamos en BD
    transaccion_bd = sesion.get(Transaccion, id_transaccion)

    if not transaccion_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La transaccion con id {id_transaccion}, no existe."
        )

    # Borramos de la BD
    sesion.delete(transaccion_bd)
    sesion.commit()

    return transaccion_bd