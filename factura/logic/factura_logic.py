from ..models import Factura
from ..models import FacturaDetalle
from cliente.logic import cliente_logic as cl
from asesor.logic import logic_asesor as al
from producto.logic import producto_logic as pl

def get_factura_by_id(id):
    factura = Factura.objects.get(pk=id)
    return factura

def get_factura_detail_by_id_factura(id):
    factura_detail = FacturaDetalle.objects.filter(factura=id)
    return factura_detail

def get_facturas():
    facturas = Factura.objects.all()
    return facturas

def create_factura_detail(detail, factura_):
    detalle = FacturaDetalle(
        cantidad = detail['cantidad'],
        total = detail['total'],
        factura = factura_,
        producto = pl.get_producto_by_id(detail['producto'])
    )
    detalle.save()
    return detalle

def create_factura(factura):
    isla_obj = Factura(
        id = factura['id'],
        fecha = factura['fecha'],
        total = factura['total'],
        cliente = cl.get_cliente_by_id(factura['cliente']),
        asesor = al.get_asesor_by_id(factura['asesor']) 
    )
    isla_obj.save()
    return isla_obj