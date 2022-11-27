from ..models import Asesor

def get_asesores():
    asesores = Asesor.objects.all()
    return asesores

