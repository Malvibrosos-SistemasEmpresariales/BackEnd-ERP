from ..models import Asesor
import isla.logic.isla_logic as isla_l


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
        isla = isla_l.get_isla_by_id(asesor['isla'])
    )
    asesor_obj.save()
    return asesor_obj