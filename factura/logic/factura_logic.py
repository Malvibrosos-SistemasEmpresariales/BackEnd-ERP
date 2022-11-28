from ..models import Factura

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
    for n in factura['factura_detalle']:
            detalle = FacturaDetalle(
                cantidad = n['cantidad'],
                total = n['total'],
                factura = n['factura'],
                producto = n['producto']
            )
            detalle.save()
    isla_obj.save()
    return isla_obj