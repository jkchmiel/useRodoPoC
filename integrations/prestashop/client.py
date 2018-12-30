## ToDO - client with authentication in DB
import json
from typing import Optional

import os

import sys

from subprocess import call
from domain.shops.definition import ShopPersonalData
from integrations.prestashop.customer_data import PrestaShopCustomerData


class PrestaShopClient:

    @staticmethod
    def get_customer_data(email: str, shop_name: str) -> Optional[ShopPersonalData]:
        file_name = os.path.join(os.path.dirname(sys.modules['__main__'].__file__), f"tmp/integrations/prestashop/data/{shop_name}/{email}.json")
        print(f"get customer data for file: {file_name}")
        try:
            customer_personal_data = json.load(open(file_name))
            print(f"Customer data got: {customer_personal_data}")
            return PrestaShopCustomerData(**customer_personal_data).to_shop_personal_data("1234", shop_name)
        except FileNotFoundError:
            return None

    @staticmethod
    def delete_customer_data(email: str, shop_name: str) -> str:
        file_name = os.path.join(os.path.dirname(sys.modules['__main__'].__file__),
                                 f"tmp/integrations/prestashop/data/{shop_name}/{email}.json")
        print(f"delete customer data for email: {email} and shop: {shop_name} in file {file_name}")
        try:
            call(['rm', file_name])
            return f"Customer (email={email} data in shop={shop_name} were deleted"
        except FileNotFoundError:
            return f"Customer (email={email} data in shop={shop_name} were not deleted because ..."

if __name__ == "__main__":
    # print(json.load(open(os.path.join(os.path.dirname(sys.modules['__main__'].__file__), f"../../tmp/integrations/prestashop/data/zbivan/kowalski@example.com.json"))))
    print(PrestaShopClient.get_customer_data("asdasd", "zbivan"))
    print(PrestaShopClient.get_customer_data("kowalski@example.com", "zbivan"))
    # print(json.load(open(f"../../tmp/integrations/prestashop/data/zbivan/kowalski@example.com.json")))
    # tmp / integrations / prestashop / data / data / zbivan / kowalski @ example.com.json

    print(PrestaShopClient.delete_customer_data("kowalski@example.com", "zbivan"))