from asesor.models import Asesor
from cliente.models import Cliente
from isla.models import Isla
from producto.models import Producto
from ..models import Factura
from ..models import FacturaDetalle
from cliente.logic import cliente_logic as cl
from asesor.logic import logic_asesor as al
from producto.logic import producto_logic as pl
from django.utils.dateparse import parse_date

def delete_factura(id):
    factura = Factura.objects.get(pk=id)
    factura.delete()

def get_factura_by_id(id):
    factura = Factura.objects.get(pk=id)
    return factura

def get_factura_detail_by_id_factura(id):
    factura_detail = FacturaDetalle.objects.filter(factura=id)
    return factura_detail

def get_factura_by_date(date):
    facturas = Factura.objects.filter(fecha=date)
    return facturas

def get_facturas():
    facturas = Factura.objects.all()
    return facturas

def create_factura_detail(detail, factura_):
    detalle = FacturaDetalle(
        cantidad = detail['cantidad'],
        valor = detail['valor'],
        factura = factura_,
        producto = Producto(codigo = detail['producto']['codigo'],
                            nombre = detail['producto']['nombre'],
                            valor = detail['producto']['valor'],
                            categoria = detail['producto']['categoria'])
    )
    detalle.save()
    return detalle

def create_factura(factura):
    isla_obj = Factura(
        id = factura['id'],
        fecha = parse_date('2022-12-01'),
        total = factura['total'],
        cliente = Cliente(
                        id = factura['cliente']['id'],
                        nombre = factura['cliente']['nombre'],
                        apellido = factura['cliente']['apellido'],
                        correo = factura['cliente']['correo'],
                        tipoDocumento = factura['cliente']['tipoDocumento'],),
        asesor = Asesor(id = factura['asesor']['id'],
                        nombre = factura['asesor']['nombre'],
                        apellido = factura['asesor']['apellido'],
                        correo = factura['asesor']['correo'],
                        tipoDocumento = factura['asesor']['tipoDocumento'],
                        isla = Isla(
                        id = factura['asesor']['isla']['id'],
                        centroComercial = factura['asesor']['isla']['centroComercial'],
                        ciudad = factura['asesor']['isla']['ciudad'],
                        ))
    )
    isla_obj.save()
    return isla_obj