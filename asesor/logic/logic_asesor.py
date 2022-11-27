from ..models import Asesor

def get_asesores():
    asesores = Asesor.objects.all()
    return asesores

def get_asesor_by_id(id):
    asesor = Asesor.objects.get(pk=id)
    return asesor

def create_asesor(asesor):
    asesor_obj = Asesor(
        id = asesor['id'],
        nombre = asesor['nombre'],
        apellido = asesor['apellido'],
        correo = asesor['correo'],
        tipoDocumento = asesor['tipoDocumento'],
        isla = asesor['isla']
    )
    asesor_obj.save()
    return asesor_obj