from helpers.json_serializable import JSONSerializable


class PersonalData(JSONSerializable):
    def __init__(self, name: str, surname: str, phone: str, pesel: str, address: str, **kwargs):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.pesel = pesel
        self.address = address
        self.kwargs = kwargs