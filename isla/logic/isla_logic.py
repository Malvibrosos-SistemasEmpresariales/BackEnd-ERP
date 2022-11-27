from ..models import Isla

def get_isla_by_id(id):
    isla = Isla.objects.get(pk=id)
    return isla