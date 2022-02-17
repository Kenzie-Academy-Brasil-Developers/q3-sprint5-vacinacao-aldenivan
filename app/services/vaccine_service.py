
def validation_cpf(cpf):
    
    if len(cpf) != 11:
        raise ValueError

    if not cpf.isdigit():
        raise TypeError

    return True


def validation_types(dict):

    if type(dict.cpf) is not str or type(dict.name) is not str or type(dict.vaccine_name) is not str or type(dict.health_unit_name) is not str:
        raise TypeError

    return True


def validation_keys(**data):

    vaccine_dict = {}

    for key in data:

        if key == "cpf" or key == "name" or key == "vaccine_name" or key == "health_unit_name":
            vaccine_dict[key] = data[key]


    return vaccine_dict