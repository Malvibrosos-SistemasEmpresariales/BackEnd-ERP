from ..models import Factura
from ..models import FacturaDetalle

def get_factura_by_id(id):
    factura = Factura.objects.get(pk=id)
    return factura

def get_facturas():
    islas = Factura.objects.all()
    return islas

def create_factura(factura):
    isla_obj = Factura(
        id = factura['id'],
        fecha = factura['fecha'],
        total = factura['total'],
        cliente = factura['cliente'],
        asesor = factura['asesor']   
    )
    isla_obj.save()
    for n in factura['factura_detalle']:
            detalle = FacturaDetalle(
                cantidad = n['cantidad'],
                total = n['total'],
                factura = factura['id'],
                producto = n['producto']
            )
            detalle.save()
    return isla_obj