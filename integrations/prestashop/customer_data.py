from domain.shops.definition import ShopPersonalData


class PrestaShopCustomerData:
    def __init__(self, name: str, surname: str, phone: str, pesel: str, address: str, customer_id: str):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.pesel = pesel
        self.address = address
        self.customer_id = customer_id

    def to_shop_personal_data(self, shop_id: str, shop_name: str):
        return ShopPersonalData(shop_name, shop_id, vars(self))