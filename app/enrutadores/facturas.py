from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar, FacturaConCliente
from ..modelos.clientes import Cliente
# Ya no ocupamos importar la lista_facturas aca porque todo va por BD
# from ..listas import lista_clientes, lista_facturas
from ..conexion_bd import Sesion_dependencia
from sqlmodel import select

rutas_facturas = APIRouter()

@rutas_facturas.get("/facturas", response_model=list[FacturaConCliente])
async def listar_facturas(sesion: Sesion_dependencia):
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas


@rutas_facturas.get("/facturas/{factura_id}", response_model=FacturaConCliente)
async def listar_factura(factura_id: int, sesion: Sesion_dependencia):
    factura_bd = sesion.get(Factura, factura_id)
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )
    return factura_bd


@rutas_facturas.post("/facturas/{cliente_id}", response_model=FacturaConCliente)
async def crear_factura(
    cliente_id: int,
    datos_factura: FacturaCrear,
    sesion: Sesion_dependencia
):
    cliente_encontrado = sesion.get(Cliente, cliente_id)
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe.",
        )

    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)

    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)

    return factura_val


@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(
    factura_id: int, 
    datos_factura: FacturaEditar, 
    sesion: Sesion_dependencia # Aca inyectamos la sesion de la bd
):
    # Buscamos la factura directo en la bd
    factura_bd = sesion.get(Factura, factura_id)
    
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )

    # Actualizamos solo los datos que vengan en la petición
    datos_nuevos = datos_factura.model_dump(exclude_unset=True, exclude={"vr_total"})
    for key, value in datos_nuevos.items():
        setattr(factura_bd, key, value)

    sesion.add(factura_bd)
    sesion.commit()
    sesion.refresh(factura_bd)
    
    return factura_bd


@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int, sesion: Sesion_dependencia): # La sesion aca tmbn
    factura_bd = sesion.get(Factura, factura_id)
    
    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id}, no existe."
        )

    # La borramos de la bd
    sesion.delete(factura_bd)
    sesion.commit()
    
    return factura_bd