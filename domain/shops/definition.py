from domain.customers.personal_data import PersonalData
from helpers.json_serializable import JSONSerializable


class ShopPersonalData(JSONSerializable):
    def __init__(self, name: str, shop_id: str, personal_data: dict):
        self.name = name
        self.shop_id = shop_id
        self.personal_data = PersonalData(**personal_data)
