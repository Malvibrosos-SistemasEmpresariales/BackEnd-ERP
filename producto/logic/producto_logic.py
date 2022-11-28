from ..models import Producto

def get_productos():
    productos = Producto.objects.all()
    return productos

def get_producto_by_id(id):
    producto = Producto.objects.get(pk=id)
    return producto

def create_producto(producto):
    producto_obj = Producto(
        id = producto['id'],
        nombre = producto['nombre'],
        precio = producto['precio'],
        descripcion = producto['descripcion'],
        tipo = producto['tipo']
    )
    producto_obj.save()
    return producto_obj