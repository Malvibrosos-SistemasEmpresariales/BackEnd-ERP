from ..models import Producto

def get_productos():
    productos = Producto.objects.all()
    return productos

def get_producto_by_id(id):
    id = id.upper()
    producto = Producto.objects.get(pk=id)
    return producto

def create_producto(producto):
    producto_obj = Producto(
        codigo = producto['codigo'],
        nombre = producto['nombre'],
        valor = producto['valor'],
        categoria = producto['categoria'],
    )
    producto_obj.save()
    return producto_obj
