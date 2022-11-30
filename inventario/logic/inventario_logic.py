from ..models import Inventario
from isla.logic import isla_logic
from producto.logic import producto_logic
from ..models import InventarioMovimientos

def get_inventarios():
    inventarios = Inventario.objects.all()
    return inventarios

def get_inventarios_by_id(id):
    inventario = Inventario.objects.get(pk=id)
    return inventario

def get_movimientos_by_id_producto(id):
    movimientos = InventarioMovimientos.objects.filter(producto=id)
    return movimientos

def create_inventario(inventario):
    inventario_obj = Inventario(
        cantidad = inventario['cantidad'],
        isla = isla_logic.get_isla_by_id(inventario['isla']),
        producto = producto_logic.get_producto_by_id(inventario['producto'])
    )
    inventario_obj.save()
    return inventario_obj