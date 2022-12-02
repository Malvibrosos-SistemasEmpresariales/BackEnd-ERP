from ..models import Inventario
from isla.logic import isla_logic
from producto.logic import producto_logic
from ..models import InventarioMovimientos
from django.utils.dateparse import parse_date

def delete_inventario(id):
    inventario = Inventario.objects.get(pk=id)
    inventario.delete()
    
def get_inventarios():
    inventarios = Inventario.objects.all()
    return inventarios

def get_inventarios_by_id(id):
    inventario = Inventario.objects.get(pk=id)
    return inventario

def get_movimientos_by_id_producto(id):
    movimientos = InventarioMovimientos.objects.filter(inventario=id)
    return movimientos

def create_movimiento(movimiento):
    movimiento_obj = InventarioMovimientos(
        cantidad = movimiento['cantidad'],
        fecha = parse_date(movimiento['fecha']),
        inventario = get_inventarios_by_id(movimiento['inventario'])
    )
    movimiento_obj.save()
    return movimiento_obj

def create_inventario(inventario):
    inventario_obj = Inventario(
        cantidad = inventario['cantidad'],
        isla = isla_logic.get_isla_by_id(inventario['isla']),
        producto = producto_logic.get_producto_by_id(inventario['producto'])
    )
    inventario_obj.save()
    return inventario_obj