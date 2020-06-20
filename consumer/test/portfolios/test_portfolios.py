import json
import requests
from test.base import BaseTestCase
from api.main import db
from run import app

#############################################################################
# Class for testing service business logic
#############################################################################
# class TestFileUpload(BaseTestCase):
#
#     def test_valid_file(self):
#         domain = app.config['ALLOWED_HOST']
#         headers = {
#             'Content-type': 'multipart/form-data'
#         }
#         data = []
#         print('{}units_20190101.csv'.format(app.config['UPLOAD_FOLDER']))
#         data = {
#             'file': open(os.path.join(app.config['UPLOAD_FOLDER'] + 'units_20190101.csv'), 'rb'),  # we use StringIO to simulate file object
#         }
#         url = '{}/{}/'.format(domain, 'file')
#         print(url)
#         response_dict = requests.post(url, data=data, headers=headers)
#         print('testing')
#         print(response_dict)
#         print('validated')
#         response_dict = json.loads(response_dict)
#         self.assertTrue(response_dict['code'], 200)

class TestPortfolioUrl(BaseTestCase):
    def test_valid_asset(self):
        """ Base Tests """

        def test_valid_portfolio_list(self):
            domain = app.config['ALLOWED_HOST']
            headers = {
                'Content-type': 'application/json'
            }
            url = domain + '/portfolios'
            response_dict = json.loads(requests.get(url, headers=headers).text)

            self.assertTrue(response_dict['code'] is 200)


    def test_valid_portfolio_detail(self):
        domain = app.config['ALLOWED_HOST']
        headers = {
            'Content-type': 'application/json'
        }
        url = domain + '/portfolios'
        response_dict = json.loads(requests.get(url, headers=headers).text)

        self.assertTrue(response_dict['code'] is 200)
