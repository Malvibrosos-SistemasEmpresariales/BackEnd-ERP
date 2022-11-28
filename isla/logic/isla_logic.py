from ..models import Isla

def get_isla_by_id(id):
    isla = Isla.objects.get(pk=id)
    return isla

def get_islas():
    islas = Isla.objects.all()
    return islas

def create_isla(isla):
    isla_obj = Isla(
        centroComercial = isla['centroComercial'],
        ciudad = isla['ciudad']
    )
    isla_obj.save()
    return isla_obj