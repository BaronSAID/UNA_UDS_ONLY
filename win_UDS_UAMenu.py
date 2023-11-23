# coding=utf8
# Created by Nicolae Gaidarji at 19.01.2022
import logging
import csv

from CONSTANT import *
from uis.Form_UDS_UAMenu import *
from UDS_driver.uds_lib import UdsLib

DL_RESULT = {
    'OK': 0,
    'ERR': 1
}

file_transaction_lists = 'file_transaction_lists.txt'

logg_win = logging.getLogger(__name__)


def write_to_file(p_file_name, p_text_to_append, p_delete_lines=False):
    try:
        f = open(p_file_name, 'r')
        f.close()
    except FileNotFoundError:
        f = open(p_file_name, 'w')
        f.close()

    if p_delete_lines:
        with open(p_file_name, "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if p_text_to_append not in line:
                    f.write(line)
            f.truncate()
        f.close()
    else:
        with open(p_file_name) as file_object:
            v_data = file_object.read()
        file_object.close()

        with open(p_file_name, "w+") as file_object:
            v_text_line = f'{p_text_to_append} \n'
            file_object.write(f'{v_text_line}{v_data}')
        file_object.close()


def round_down(p_number, p_n_d=0):
    v_num_str = str(p_number).split('.')
    v_int = v_num_str[0]
    try:
        v_decimal = v_num_str[1]
    except IndexError:
        v_decimal = ''

    return float(f'{v_int}.{v_decimal[0:p_n_d]}')


class MainFrame(Frame_UDS_UAMenu):
    def __init__(self, arg, mess_una, config_file, current_path):
        Frame_UDS_UAMenu.__init__(self, arg)
        logg_win.info(f'Init MainFrame {current_path}')

        self.result_global = {'code': 1,
                              'message': '',
                              'responcedata': '',
                              }
        self.close_all_socket = False
        self.v_max_point_10 = 0
        self.cashback_points = ''
        self.total_point_before_pay = 0
        self.v_cashback_points = 0
        self.v_uds_current_points = 0

        self.cfg = config_file
        self.uds_id_user = str(self.cfg.conf.get('UDS', 'id_user'))
        self.uds_api_key = str(self.cfg.conf.get('UDS', 'api_key'))
        self.uds_operator_id = str(self.cfg.conf.get('UDS', 'operator_id'))
        self.uds_operator = str(self.cfg.conf.get('UDS', 'operator'))

        try:
            self.language = str(self.cfg.conf.get('WINDOW', 'lang'))
        except Exception as err:
            logg_win.error(err)
            self.language = 'ro'

        self.uds = UdsLib(self.uds_id_user, self.uds_api_key, self.uds_operator)

        # ======================================
        self.set_lan_value()

        v_step1 = mess_una.find(',')
        v_step2 = mess_una.find(',', v_step1 + 1)
        v_step3 = mess_una.find(',', v_step2 + 1)
        v_step3 = len(mess_una) if v_step3 == -1 else v_step3

        self.op_code = mess_una[:v_step1]
        self.nr_check = mess_una[v_step1 + 1:v_step2]
        self.amount = mess_una[v_step2 + 1:v_step3]
        self.transaction_id = mess_una[v_step3 + 1:]

        self.et_suma_sp.Value = self.amount
        self.et_sum_return.Value = self.amount
        self.st_transaction_id.Label = self.transaction_id
        logg_win.info(f'amm {self.amount}')

        if self.op_code == '302':  # return
            self.uds_panel_init(4)
        else:  # other operation
            self.uds_panel_init()

        # Setare dimensiune, imagine footbar, titlu + versiune =======
        effective_size = self.GetEffectiveMinSize()
        self.SetSize(wx.Size(effective_size))
        self.SetMinSize(wx.Size(effective_size))
        self.SetMaxSize(wx.Size(effective_size))
        # ==============================================================


        logg_win.info(
            f'uds_id_user: {self.uds_id_user}, uds_operator: {self.uds_operator}, uds_operator_id: {self.uds_operator_id}')

        self.res_step1 = None

        self.last_transaction_id = 0

    def set_lan_value(self):
        """
        Localizarea variabililor statice de pe forma
        """

        self.st_spre_plata.Label = get_val_lang('st_spre_plata', self.language)
        self.st_spre_plata2.Label = get_val_lang('st_spre_plata', self.language)
        self.st_spre_plata3.Label = get_val_lang('st_spre_plata', self.language)
        self.st_client_id.Label = get_val_lang('st_client_id', self.language)
        self.bt_uds_continue.Label = get_val_lang('bt_uds_continue', self.language)
        self.st_uds_total_points.Label = get_val_lang('st_uds_total_points', self.language)
        self.st_max_bonus.Label = get_val_lang('st_max_bonus', self.language)
        self.bt_set_non_points.Label = get_val_lang('bt_set_non_points', self.language)
        self.bt_set_points.Label = get_val_lang('bt_set_points', self.language)
        self.st_cash_back.Label = get_val_lang('st_cash_back', self.language)
        self.st_cash_back2.Label = get_val_lang('st_cash_back', self.language)
        self.st_uds_sum_total.Label = get_val_lang('st_uds_sum_total', self.language)
        self.st_uds_sum_total2.Label = get_val_lang('st_uds_sum_total', self.language)
        self.st_uds_nrcheck.Label = get_val_lang('st_uds_nrcheck', self.language)
        self.st_uds_casir.Label = get_val_lang('st_uds_casir', self.language)
        self.st_uds_bonus.Label = get_val_lang('st_uds_bonus', self.language)
        self.bt_uds_pay.Label = get_val_lang('bt_uds_pay', self.language)
        self.st_transaction_id.Label = get_val_lang('st_transaction_id', self.language)
        self.st_sum_return.Label = get_val_lang('st_sum_return', self.language)
        self.bt_return.Label = get_val_lang('st_sum_return', self.language)
        self.st_tatal_poits_befor.Label = get_val_lang('st_tatal_poits_befor', self.language)

    def uds_panel_init(self, p_step=1):
        logg_win.info(f'init panel: {p_step}')
        if p_step == 1:
            self.pn_1.Show()
            self.pn_2.Hide()
            self.pn_3.Hide()
            self.pn_4.Hide()
        if p_step == 2:
            self.pn_1.Hide()
            self.pn_2.Show()
            self.pn_3.Hide()
            self.pn_4.Hide()
        if p_step == 3:
            self.pn_1.Hide()
            self.pn_2.Hide()
            self.pn_3.Show()
            self.pn_4.Hide()
        if p_step == 4:
            self.pn_1.Hide()
            self.pn_2.Hide()
            self.pn_3.Hide()
            self.pn_4.Show()

        self.bs_uds.Layout()

    def fill_uds_result(self, p_result):
        logg_win.info(f'write result: {p_result}')
        v_result = str(p_result)
        v_result = v_result.replace("{", '\n{')
        v_result = v_result.replace(",", ',\n')
        self.rt_uds_result.SetValue(v_result)

    def onclick_bt_uds_continue(self, event):
        logg_win.info(f'start: [{event}]')

        wait = wx.BusyCursor()
        print(wait)
        v_sum_sp = float(self.et_suma_sp.Value)
        v_id_user = self.et_uds_client.Value

        logg_win.info(f'v_sum_sp: {v_sum_sp}, v_id_user: {v_id_user}')

        if v_id_user == '':
            # v_msg_not_client = 'Introduceti/Scanati id client'
            v_msg_not_client = get_val_lang('v_msg_not_client', self.language)
            logg_win.info(v_msg_not_client)
            wx.MessageBox(v_msg_not_client, LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)
        else:
            self.uds.get_user_info(v_id_user, v_sum_sp)
            v_res = self.uds.result_uds
            self.res_step1 = v_res
            logg_win.info(f'res_step1: {self.res_step1}')
            if str(v_id_user).find('+') > -1:
                self.v_max_point_10 = 0
            else:
                self.v_max_point_10 = (v_sum_sp * 10) / 100
                # self.v_max_point_10 = round(self.v_max_point_10, 2)
                self.v_max_point_10 = round_down(self.v_max_point_10, 2)

            if v_res['response'] == 200:
                self.v_uds_current_points = float(v_res['points'])
                if self.v_uds_current_points < float(self.v_max_point_10):
                    self.v_max_point_10 = self.v_uds_current_points

                if v_res['points'] is None or v_res['points'] == '' or v_res['points'] == ' ':
                    self.total_point_before_pay = 0
                else:
                    self.total_point_before_pay = v_res['points']
                self.v_cashback_points = round((int(v_res['cashbackRate']) / 100) * (v_sum_sp - self.v_max_point_10), 2)

                self.st_uds_puncte_loialitate.SetLabel(str(v_res['points']))
                self.cashback_points = f"({round((int(v_res['cashbackRate']) / 100) * (v_sum_sp - self.v_max_point_10), 2)} points)"
                self.st_cashback_val.Label = f"{str(v_res['cashbackRate'])}% {self.cashback_points}"
                # self.st_max_bonus_val.Label = str(v_res['max_points'])
                # self.et_bonus_extract.Value = str(v_res['max_points'])
                self.st_max_bonus_val.Label = str(self.v_max_point_10)
                self.et_bonus_extract.Value = str(self.v_max_point_10)

                self.st_suma_sp2.Label = str(v_sum_sp)
                self.st_uds_sum_total_val.Label = str(v_sum_sp)

                self.uds_panel_init(2)
            else:
                # v_msg_info = f'Operațiunea nu poate fi continuată, Verificați vărog ID/Nr. de telefon client indicat \n' \
                #              f"ID/Nr. Telefon: {v_id_user}\n\n" \
                #              f"Message UDS: {v_res['err_message']}"
                v_msg_info = f'{get_val_lang("v_err_not_id_popup", self.language)} \n' \
                             f"{get_val_lang('v_err_not_id_popup2', self.language)}: {v_id_user}\n\n" \
                             f"{get_val_lang('v_err_not_id_popup3', self.language)}: {v_res['err_message']}"
                wx.MessageBox(v_msg_info, LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)
                self.fill_uds_result(v_res['json_data'])

        del wait

    def set_point_for_pay(self, p_type=1):
        """Pregatirea datelor pentru plata

           param.
           p_type: 1-achitarea inclusiv punctele de loialitate
                   2-achitarea fara puncte de loialitate
        """
        logg_win.info(f'start: [{p_type}]')
        v_bonus_extract = self.et_bonus_extract.Value
        v_bonus_extract = 0 if p_type == 2 else v_bonus_extract
        logg_win.info(f'v_bonus_extract: {v_bonus_extract}')

        if float(v_bonus_extract) > self.v_max_point_10:
            # v_msg_max_points = f"Reducerea poate fi aplicata pina la suma: {self.v_max_point_10}"
            v_msg_max_points = f"{get_val_lang('v_msg_popup_max_points', self.language)}: {self.v_max_point_10}"
            logg_win.info(v_msg_max_points)
            wx.MessageBox(v_msg_max_points, LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)
        else:
            # v_nr_check = f'{random.randint(100, 999)}-{random.randint(100, 999)}'
            v_nr_check = self.nr_check
            self.st_uds_nrcheck_val.Label = v_nr_check
            self.st_uds_casir_val.Label = self.uds_operator
            self.st_spre_plata3_val.Label = str(self.res_step1['total'])
            self.st_cash_back2_val.Label = f"{str(self.res_step1['cashbackRate'])}% {self.cashback_points}"
            self.st_uds_bonus_val.Label = str(v_bonus_extract)

            self.total_point_before_pay = round((self.total_point_before_pay + self.v_cashback_points - float(v_bonus_extract)), 2)
            self.st_tatal_poits_befor_val.Label = str(self.total_point_before_pay)

            if v_bonus_extract == 0:
                v_total_pay = str(self.res_step1['total'])
            else:
                v_total_pay = round(self.res_step1['total'] - float(v_bonus_extract), 2)
            self.st_uds_sum_total2_val.Label = str(v_total_pay)

            self.uds_panel_init(3)

    def onclick_bt_set_points(self, event):
        logg_win.info(f'start: [{event}]')
        self.set_point_for_pay(1)

    def onclick_bt_set_non_points(self, event):
        logg_win.info(f'start: [{event}]')
        self.set_point_for_pay(2)

    def onclick_bt_uds_pay(self, event):
        logg_win.info(f'start: [{event}]')
        v_id_user = self.et_uds_client.Value
        v_points = self.st_uds_bonus_val.Label
        v_nr_check = self.st_uds_nrcheck_val.Label
        v_cash = self.st_uds_sum_total2_val.Label

        logg_win.info(f'v_id_user: {v_id_user}, v_points: {v_points}, v_nr_check: {v_nr_check}, v_cash: {v_cash}')

        self.uds.post_operation(p_code=v_id_user,
                                p_total=str(self.res_step1['total']),
                                p_skip_loyalty_total=self.res_step1['skip_loyalty_total'],
                                p_points=v_points,
                                p_cash=v_cash,
                                p_external_id=self.uds_operator_id,
                                p_name=self.uds_operator,
                                p_number=v_nr_check
                                )
        v_res = self.uds.result_uds
        logg_win.info(f'v_res: {v_res}')
        # print('*'*100)
        # print(self.last_transaction_id)

        if v_res['response'] == 200:
            # v_msg_succcess = f'Tranzactie cu success'
            v_msg_succcess = get_val_lang('v_transaction_success', self.language)
            logg_win.info(v_msg_succcess)
            wx.MessageBox(v_msg_succcess, LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)
            # self.reset_form()
            self.last_transaction_id = v_res['json_data']['id']

            write_to_file(file_transaction_lists, f"{v_res['json_data']['dateCreated']} {v_res['json_data']['id']}")
            v_res_code = 0
            v_res_msg_global = 'Success'
        else:
            v_msg_err = f"error code: {v_res['response']} \n message: {v_res['err_message']} \nurl: {v_res['url']}"
            logg_win.error(v_msg_err)
            v_res_code = 1
            v_res_msg_global = v_msg_err
            wx.MessageBox(v_msg_err, LOG_CONST.Warning_, wx.OK | wx.ICON_WARNING)

        v_res_json = v_res
        self.result_global['code'] = v_res_code
        self.result_global['message'] = v_res_msg_global
        self.result_global['responcedata'] = v_res_json
        self.Destroy()
        self.close_all_socket = True

    def reset_form(self):
        logg_win.info('start reset')
        self.uds_panel_init()
        self.fill_uds_result('')
        self.uds.result_uds = None
        self.et_uds_client.SetValue('')
        self.rt_uds_result.SetValue('...')
        self.Layout()

    def onclick_bt_return(self, event):
        logg_win.info(f'Return transaction id: {self.transaction_id}')

        if len(self.transaction_id) == 0:
            self.reward_set()
        else:
            self.reward_pay(self.transaction_id)

    def reward_set(self):
        # v_msg_id_transaction = f"Indicati ID Tranzactie:"
        v_msg_id_transaction = get_val_lang('v_msg_indicate_trans_id', self.language)
        logg_win.info(v_msg_id_transaction)
        dlg = wx.TextEntryDialog(self, v_msg_id_transaction, '')
        if dlg.ShowModal() == wx.ID_OK:
            v_id_transaction = dlg.GetValue()
            if len(v_id_transaction) > 0:
                self.reward_pay(v_id_transaction)
            else:
                self.fill_uds_result('Nu sa introdus id  operatiune')

    def reward_pay(self, p_id_transaction):
        v_partial_amount = self.et_sum_return.Value
        try:
            v_partial_amount = -1 if len(v_partial_amount) == 0 else float(v_partial_amount)
        except ValueError as err:
            v_msg_succcess = f'Suma return introdusa incorect \n{err}'
            logg_win.info(v_msg_succcess)
            wx.MessageBox(v_msg_succcess, LOG_CONST.Error, wx.OK | wx.ICON_ERROR)
            return

        self.uds.reward(p_id_transaction, p_partial_amount=v_partial_amount)
        v_res = self.uds.result_uds
        logg_win.info(f'v_res: {v_res}')

        if v_res['response'] == 200:
            # v_msg_succcess = f'Tranzactie cu success'
            v_msg_succcess = get_val_lang('v_transaction_success', self.language)
            logg_win.info(v_msg_succcess)
            wx.MessageBox(v_msg_succcess, LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)

            write_to_file(file_transaction_lists, f"{p_id_transaction}", True)

            v_res_code = 0
            v_res_msg_global = 'Success'
        else:
            v_msg_err = f"error code: {v_res['response']} \n message: {v_res['err_message']} \nurl: {v_res['url']}"
            logg_win.error(v_msg_err)
            v_res_code = 1
            v_res_msg_global = v_msg_err
            wx.MessageBox(v_msg_err, LOG_CONST.Warning_, wx.OK | wx.ICON_WARNING)

        self.fill_uds_result(v_res)

        v_res_json = v_res
        self.result_global['code'] = v_res_code
        self.result_global['message'] = v_res_msg_global
        self.result_global['responcedata'] = v_res_json
        self.Destroy()
        self.close_all_socket = True

    def on_close(self, event):
        # self.logger.info('Close window')
        logg_win.info('Close window')

        self.Destroy()
        self.close_all_socket = True
        self.result_global['code'] = 1
        self.result_global['message'] = ListERR['601']
        self.result_global['responcedata'] = ListERR['601']


def show_form_uds(mess_una, config_file, current_path):
    wx.Log.EnableLogging(False)
    logg_win.debug('Func. show_form, param: [{}], [{}], [{}]'
                   .format(mess_una, config_file, current_path))
    app = []
    form_main = []
    print(app, form_main)

    app = wx.App()
    wx.DisableAsserts()
    form_main = MainFrame(None, mess_una, config_file, current_path)
    form_main.Show()
    app.MainLoop()
    result = form_main.result_global

    logg_win.debug('Func. show_form, return: [{}], [{}], [{}]'
                   .format(result, app, form_main.close_all_socket))
    close_all_socket = form_main.close_all_socket
    wx.App.Destroy(app)

    return result, app, close_all_socket


def create_lang_dict():
    logg_win.info('Check file lang dict')
    v_file_name = FILE_LANG_DICT_NAME
    try:
        with open(v_file_name, newline='') as csvfile:
            pass
    except FileNotFoundError:
        logg_win.info('Create file lang dict')
        with open(v_file_name, 'w', encoding="utf-8") as f:
            f.write(DEFAULT_LANG_DICT)


def get_lang_dict():
    with open(FILE_LANG_DICT_NAME, newline='', encoding="utf-8") as csvfile:
        print(csvfile)
        v_lang_dict_ = list(csv.reader(csvfile))

    v_lang_dict = {}
    for row in v_lang_dict_:
        v_key = str(row[0]).lower()
        v_lang_dict[v_key] = {'ro': row[1], 'en': row[2], 'ru': row[3]}

    return v_lang_dict

create_lang_dict()
g_lang_dict = get_lang_dict()


def get_val_lang(p_key, p_lang):
    try:
        v_result = g_lang_dict[p_key][p_lang]
    except KeyError:
        v_result = p_key

    return v_result
