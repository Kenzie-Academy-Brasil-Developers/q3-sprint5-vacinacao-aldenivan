
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

    wrong_keys = []

    for key in data:

        if key != "cpf" and key != "name" and key != "vaccine_name" and key != "health_unit_name":
            wrong_keys.append(key)
        print(key)

    return wrong_keys


def tranforming_upper_case(data):

    for value in data.values():
        
        if value is str:
            value.upper()
    