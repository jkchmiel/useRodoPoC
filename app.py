import sys

from flask import Flask

from helpers.file_copies import SampleDataInTmp
from integrations.prestashop.service import PrestaShopService

app = Flask(__name__)




@app.route('/')
def homepage():
    SampleDataInTmp.make_copy("integrations/prestashop")
    return "<h1> RODO PoC builder under: </h1><p>Python: {ver}</p>".format(ver=sys.version)


@app.route('/emails/<email>', methods=['GET'])
def get_email(email):
    print(f"Search for email: {email}")
    return PrestaShopService().search_customer_in_shops(email).to_json()


@app.route('/delete/emails/<email>/shops/<shop_name>', methods=['GET'])
def delete_customer_data_in_shop(email, shop_name):
    print(f"Search for email: {email}")
    return PrestaShopService().delete_customer_data_in_shop(email, shop_name)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
