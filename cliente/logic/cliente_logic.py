from ..models import Cliente

def get_cliente_by_id(id):
    cliente = Cliente.objects.get(pk=id)
    return cliente

def get_clientes():
    clientes = Cliente.objects.all()
    return clientes

def create_cliente(cliente):
    cliente_obj = Cliente(
        nombre = cliente['nombre'],
        apellido = cliente['apellido'],
        correo = cliente['correo'],
        tipoDocumento = cliente['tipoDocumento']
    )
    cliente_obj.save()
    return cliente_obj