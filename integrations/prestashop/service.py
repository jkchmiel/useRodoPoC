from typing import List

from domain.shops.definition import ShopPersonalData
from helpers.json_serializable import JSONSerializable
from integrations.prestashop.client import PrestaShopClient
from integrations.consts import PRESTA_SHOPS


class ShopsPersonalDataResponse(JSONSerializable):
    def __init__(self, email: str, shops_personal_data: List[ShopPersonalData]):
        self.email = email
        self.shops_personal_data = shops_personal_data


class PrestaShopService:

    def search_customer_in_shops(self, email: str, shops: List[str] = PRESTA_SHOPS):
        shops_personal_data = []
        for shop in shops:
            shop_personal_data = PrestaShopClient.get_customer_data(email, shop)
            if shop_personal_data:
                shops_personal_data.append(shop_personal_data)

        return ShopsPersonalDataResponse(email, shops_personal_data)

    def delete_customer_data_in_shop(self, email: str, shop_name: str) -> str:
        return PrestaShopClient.delete_customer_data(email, shop_name)

if __name__ == "__main__":
    print(PrestaShopService().search_customer_in_shops("wkowalski@example.com", ["zbivan", "testytesty_ovh"]))