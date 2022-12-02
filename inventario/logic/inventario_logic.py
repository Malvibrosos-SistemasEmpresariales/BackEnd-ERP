from isla.models import Isla
from producto.models import Producto
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

def get_movimientos():
    movimientos = InventarioMovimientos.objects.all()
    return movimientos

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
        isla = Isla(inventario['isla']['id'],
                    inventario['isla']['centroComercial'],
                    inventario['isla']['ciudad']),
        producto = Producto(inventario['producto']['codigo'],
                            inventario['producto']['nombre'],
                            inventario['producto']['valor'],
                            inventario['producto']['categoria'])
    )
    inventario_obj.save()
    return inventario_obj

def update_inventario(inventario, update):
    inventario_obj = Inventario(
        cantidad = inventario['cantidad']+update,
        isla = Isla(inventario['isla']['id'],
                    inventario['isla']['centroComercial'],
                    inventario['isla']['ciudad']),
        producto = Producto(inventario['producto']['codigo'],
                            inventario['producto']['nombre'],
                            inventario['producto']['valor'],
                            inventario['producto']['categoria'])
    )
    inventario_obj.save()
    return inventario_obj