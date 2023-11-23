# -*- coding: utf-8 -*-
# Created by Nicolae Gaidarji at 01.12.2021
import logging
import requests

logger = logging.getLogger(__name__)


class UdsLib:
    def __init__(self, p_id_user, p_api_key, p_operator='Test', p_uds_url='https://api.uds.app/partner/v2'):
        logger.info(f'Init module UDS, param: [{p_id_user}], [{p_operator}], [{p_uds_url}]')
        self.id_user = p_id_user
        self.api_key = p_api_key
        self.operator = p_operator
        self.uds_url = p_uds_url

        self.result_uds = {
            'response': None,
            'err_message': None,
            'json_data': None,
            'displayName': None,
            'user_uid': None,
            'cashbackRate': None,
            'discountRate': None,
            'user_id': None,
            'points': None,
            'total': None,
            'max_points': 0,
            'op_id': None,
            'op_name': None,
            'url': None,
        }

    def write_result(self
                     , p_response=None
                     , p_json_data=None
                     , p_err_message=None
                     , p_code=None
                     , p_tran_id=None
                     , p_display_name=None
                     , p_user_uid=None
                     , p_cashback_rate=None
                     , p_discount_rate=None
                     , p_user_id=None
                     , p_points=None
                     , p_total=None
                     , p_max_points=None
                     , p_skip_loyalty_total=None
                     , p_op_name=None
                     , p_op_id=None
                     , p_url=None
                     ):
        self.result_uds = {
            'response': p_response,
            'json_data': p_json_data,
            'err_message': p_err_message,
            'code': p_code,
            'transaction_id': p_tran_id,
            'displayName': p_display_name,
            'user_uid': p_user_uid,
            'cashbackRate': p_cashback_rate,
            'discountRate': p_discount_rate,
            'user_id': p_user_id,
            'points': p_points,
            'total': p_total,
            'max_points': p_max_points,
            'skip_loyalty_total': p_skip_loyalty_total,
            'op_id': p_op_id,
            'op_name': p_op_name,
            'url': p_url,
        }
        logger.info(f'result_uds: {self.result_uds}')

    def get_user_info(self, p_id_client, p_total, p_skip_loyalty_total=0):
        logger.info(f'Run func. param: [{p_id_client}]')
        v_is_phone = False

        if p_skip_loyalty_total == 0:
            v_skip_loyalty_total = ''
        else:
            v_skip_loyalty_total = f'&skipLoyaltyTotal={p_skip_loyalty_total}'

        if p_id_client[0] == '+':
            # self.write_result(p_response=200
            #                   , p_points=' '
            #                   , p_total=p_total
            #                   , p_skip_loyalty_total=p_skip_loyalty_total
            #                   , p_cashback_rate=3
            #                   , p_max_points=0
            #                   )

            p_id_client = str(p_id_client).replace('+', '%2B')
            v_is_phone = True
            v_url = f'{self.uds_url}/customers/find?phone={p_id_client}&total={p_total}'
            logger.info(f'URL request: {v_url}')
        else:
            v_url = f'{self.uds_url}/customers/find?code={p_id_client}&exchangeCode=true' \
                    f'&total={p_total}{v_skip_loyalty_total}'
            logger.info(f'URL request: {v_url}')

        v_req = requests.get(v_url, auth=(self.id_user, self.api_key))
        v_status_code = v_req.status_code
        v_res = v_req.json()

        if v_status_code == 200:
            self.write_result(p_response=v_status_code
                              , p_json_data=v_res
                              , p_code=v_res['code']
                              , p_display_name=v_res['user']['displayName']
                              , p_user_uid=v_res['user']['uid']
                              , p_cashback_rate=v_res['user']['participant']['cashbackRate']
                              , p_discount_rate=v_res['user']['participant']['discountRate']
                              , p_user_id=v_res['user']['participant']['id']
                              , p_points=v_res['user']['participant']['points']
                              , p_total=v_res['purchase']['total']
                              , p_skip_loyalty_total=v_res['purchase']['skipLoyaltyTotal']
                              , p_max_points=v_res['purchase']['maxPoints']
                              )
        elif v_status_code == 404 and v_is_phone:
            self.write_result(p_response=200
                              , p_points=' '
                              , p_total=p_total
                              , p_skip_loyalty_total=p_skip_loyalty_total
                              , p_cashback_rate=3
                              , p_max_points=0
                              )
        else:
            self.write_result(p_response=v_status_code, p_json_data=v_req,
                              p_err_message=v_res['message'],
                              p_url=v_url)

        # if v_status_code != 200:
        #     self.write_result(p_response=v_status_code, p_json_data=v_req,
        #                       p_err_message=v_res['message'],
        #                       p_url=v_url)
        # else:
        #     self.write_result(p_response=v_status_code
        #                       , p_json_data=v_res
        #                       , p_code=v_res['code']
        #                       , p_display_name=v_res['user']['displayName']
        #                       , p_user_uid=v_res['user']['uid']
        #                       , p_cashback_rate=v_res['user']['participant']['cashbackRate']
        #                       , p_discount_rate=v_res['user']['participant']['discountRate']
        #                       , p_user_id=v_res['user']['participant']['id']
        #                       , p_points=v_res['user']['participant']['points']
        #                       # , p_total=p_total if v_is_phone else v_res['purchase']['total']
        #                       # , p_skip_loyalty_total=p_skip_loyalty_total if v_is_phone else v_res['purchase']['skipLoyaltyTotal']
        #                       # , p_max_points=int(p_total)*0.15 if v_is_phone else v_res['purchase']['maxPoints']
        #                       , p_total=v_res['purchase']['total']
        #                       , p_skip_loyalty_total=v_res['purchase']['skipLoyaltyTotal']
        #                       , p_max_points=v_res['purchase']['maxPoints']
        #
        #                       )

    def post_operation(self, p_code, p_total, p_skip_loyalty_total, p_points, p_cash, p_external_id, p_name, p_number):
        logger.info(f'Run func. param: [{p_code}] [{p_total}] [{p_skip_loyalty_total}]')

        if len(p_code) > 6:
            v_code = ''
            v_phone = p_code
        else:
            v_code = p_code
            v_phone = ''

        v_skip_loyalty_total = 0.01 if p_skip_loyalty_total == 0 else p_skip_loyalty_total
        v_data_load = {
                        "code": f"{v_code}",
                        "participant": {
                            "uid": '',
                            "phone": v_phone
                            },
                        "nonce": '',
                        "cashier": {
                            "externalId": p_external_id,
                            "name": str(p_name)
                            },
                        "receipt": {
                            "total": float(p_total),
                            "cash": p_cash,
                            "points": float(p_points),
                            "number": p_number,
                            "skipLoyaltyTotal": float(v_skip_loyalty_total)
                            }
                        }

        v_url = f'{self.uds_url}/operations'
        logger.info(f'URL request: {v_url}')
        logger.info(f'Load data post: {v_data_load}')

        v_headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

        v_req = requests.post(v_url, auth=(self.id_user, self.api_key),  headers=v_headers, json=v_data_load)
        v_status_code = v_req.status_code
        v_res = v_req.json()
        print(str(v_res))

        try:
            v_customer_uid = v_res['customer']['uid']
        except KeyError:
            v_customer_uid = ''

        try:
            v_customer_id = v_res['customer']['id']
        except KeyError:
            v_customer_id = ''

        if v_status_code != 200:
            self.write_result(p_response=v_status_code, p_json_data=v_req,
                              p_err_message=v_res['message'],
                              p_url=v_url)
        else:
            self.write_result(p_response=v_status_code
                              , p_json_data=v_res
                              , p_tran_id=v_res['id']
                              , p_display_name=v_res['customer']['displayName']
                              , p_user_uid=v_customer_uid
                              , p_user_id=v_customer_id
                              , p_points=v_res['points']
                              , p_total=v_res['total']
                              , p_op_id=v_res['cashier']['id']
                              , p_op_name=v_res['cashier']['displayName']
                              )

        return self.result_uds

    def reward(self, p_transaction_id, p_partial_amount=-1):
        logger.info(f'Reward: [{p_transaction_id}] [{p_partial_amount}]')

        if p_partial_amount > 0:
            v_partial_amount = p_partial_amount
        else:
            v_partial_amount = ''

        v_data_load = {
            "partialAmount": f"{v_partial_amount}"
        }

        v_url = f'{self.uds_url}/operations/{p_transaction_id}/refund'
        logger.info(f'URL request: {v_url}')
        logger.info(f'Load data post: {v_data_load}')

        v_headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

        v_req = requests.post(v_url, auth=(self.id_user, self.api_key), headers=v_headers, json=v_data_load)
        v_status_code = v_req.status_code
        v_res = v_req.json()

        if v_status_code != 200:
            self.write_result(p_response=v_status_code, p_json_data=v_req,
                              p_err_message=v_res['message'],
                              p_url=v_url)
        else:
            self.write_result(p_response=v_status_code
                              , p_json_data=v_res
                              )

        return self.result_uds
