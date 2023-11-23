# -*- coding: utf-8 -*-
# Created by Nicolae Gaidarji at 11.09.2020
import sys
import threading
import socketserver as socketserver

from win_UDS_UAMenu import *
from UNA_Support.Utility import *
from UNA_Support.getLog import Log
from datetime import *
from UNA_Support.config_util import *
from CONSTANT import *


sys.setrecursionlimit(5000)


class EchoTcpHandlerListenUna(socketserver.BaseRequestHandler):
    def handle(self):
        global app_exit
        """
        syntax: /MSG[operation and parameters]
        ex: /MSG1,1,498
        :return: 
        """
        data = self.request.recv(5096000).strip()
        lmsg_data = 'Mesaj primit de la server, {server_n}:\n\t\t{data}' \
            .format(data=data.decode(), server_n=server_listen_una_set)
        logg_suna.info(lmsg_data)
        # logger_lu.info('MSG primit prin socket, 8882:\n' + data)
        # print ('MSG primit prin socket, 8882:\n' + data)
        msg_client = data.decode("utf-8") + '/'
        msg_client, err_msg = extract_str(msg_client, '/MSG')
        # print msg_client, err_msg, '------------------'
        logg_suna.debug(msg_client + ', ' + err_msg + ' ------------------')
        message_una = msg_client
        app_exit = True if message_una.lower() == 'exit' else app_exit

        v_step1 = message_una.find(',')
        v_op_code = message_una[:v_step1]

        if v_op_code in ['301', '302']:
            if message_una != '-1' and app_exit is False:
                result_una, app_una, close_all_socket_una = show_form_uds(message_una, config, current_path)
                result_una = str(result_una).replace('\'', '\"')
                result_una = str(result_una).replace('None', 'null')
                # result_una = result_una.encode()
            elif app_exit:
                result_una = 'exit ok'
            else:
                result_una = {"code": 1,
                              "message": ListERR['605'],
                              "responcedata": ListERR['605'],
                              }

        logg_suna.info('MSG prelucrat \n' + message_una)
        logg_suna.info('Rezultat trimis inapoi la socket, {server_n}: \n {res}'
                       .format(res=result_una.encode('utf-8').decode('utf-8'), server_n=server_listen_una_set))

        try:
            # len_result = len(str(result_una).encode("utf-8"))
            len_result = len(str(result_una))
            v_msg = f'{len_result}\n{result_una}'.encode("utf-8")
            logg_suna.info(f'Frotmatare mesaj pentru server, {server_listen_una_set}: \n {v_msg.decode("utf-8")}')
            self.request.sendall(v_msg)
        except Exception as err:
            logger.error(err)
        else:
            if str(result_una).find('RespCode=606') > -1:
                os.system("taskkill /IM python.exe /F")
                os.system("taskkill /IM Server_POSTerminal2.exe /F")
                os.system("taskkill /IM Server_POSTerminal2_test.exe /F")
                sys.exit()
            # wx.App.Destroy(app_una) if message_una != '-1' and app_exit is False else ''
            pass

    def finish(self):
        if app_exit:
            # noinspection PyUnresolvedReferences
            server.server_close()

            server_lmsg_listen_una.server_close()


def server_listen_una():
    # noinspection PyGlobalUndefined
    global logger_lu, current_path, server_lmsg_listen_una

    try:
        lmsg_listen_una = '     Server Start UNA\n'
        logg_suna.info(lmsg_listen_una)

        server_lmsg_listen_una = socketserver.TCPServer(server_listen_una_set, EchoTcpHandlerListenUna)
        server_lmsg_listen_una.serve_forever()
    except KeyboardInterrupt:
        lmsg_e_una = ': exit server ok'
        logg_suna.info(lmsg_e_una)
    except Exception as e_listen_una:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        f_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        e_listen_una = str(e_listen_una)
        # e_listen_una = e_listen_una.decode('cp1251', 'ignore')
        e_listen_una = e_listen_una
        lmsg_e_listen_una = f'{server_listen_una_set}\n{exc_type}, {f_name}, {exc_tb.tb_lineno} \n{e_listen_una}'
            # .format(exc_type=exc_type, f_name=f_name, exc_tb=exc_tb.tb_lineno, e=e_listen_una.encode('utf-8'),
            #         server=server_listen_una_set)
        logg_suna.error(lmsg_e_listen_una)


# generare fisier cu setari ============================
config = CFG('setup.ini')

config.conf.add_section('WINDOW')
config.conf.set('WINDOW', 'lang', 'ro')

config.conf.add_section('UDS')
config.conf.set('UDS', 'id_user', '')
config.conf.set('UDS', 'api_key', '')
config.conf.set('UDS', 'operator_id', '11001')
config.conf.set('UDS', 'operator', 'Test Operator')

config.conf.add_section('LOGGING')
config.conf.set('LOGGING', ';LOGGING level: [DEBUG], [INFO] [WARNING] [ERROR] [CRITICAL]', '')
config.conf.set('LOGGING', 'level', 'DEBUG')

config.create_cfg_file()
# ========================================================

# current_path = os.path.dirname(os.getcwd())
import pathlib
current_path = str(pathlib.Path().resolve())
print(current_path)
date_now = datetime.now().strftime("%Y%m%d")
app_exit = False

# setarea afisarii logurilor 'logging'
try:
    os.makedirs(LOG_CONST.LOGSavePath)
except Exception:
    pass

try:
    logging_level = str(config.conf.get('LOGGING', 'level')).upper()
except Exception:
    logging_level = 'INFO'

logFormatter = logging.Formatter("%(asctime)s [%(name)-27.27s] [%(levelname)-8.8s] "
                                 "F:[%(lineno)d: %(funcName)-20.20s] %(message)s",
                                 '%m-%d-%y %H:%M:%S')
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(LOG_CONST.LOGSavePath + date_now + LOG_CONST.name_log)
fileHandler.setFormatter(logFormatter)
fileHandler.setLevel(logging_level)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
rootLogger.setLevel(logging_level)

logging.getLogger('urllib3').setLevel('CRITICAL')
logging.getLogger('future_stdlib').setLevel('CRITICAL')
logging.getLogger('PIL').setLevel('CRITICAL')

logg_main = rootLogger
logg_suna = logging.getLogger('Server UNA')
# ========================================================

logg_main.info('============================================================')
logg_main.info(LOG_CONST.START_APP)
python_v = sys.version
logg_main.info(f'Python version: {python_v}')
logg_main.info('Version module: ' + version_app)
logg_main.info('Emulator mode: {em}'.format(em=emulator_mode))


# creareaa fisierelor cu loguri
logger = Log('Server_POS', current_path + '\\LOG')
logger_lu = Log('Server_listen_una', current_path + '\\LOG')


try:
    if wind_mode == 1:
        logg_main.debug('module win mode: 1 <server>')
        t_listen_una = threading.Thread(target=server_listen_una)
        t_listen_una.start()
    else:
        logg_main.debug('module win mode: not defined')
except Exception as e_main:
    exc_type_m, exc_obj_m, exc_tb_m = sys.exc_info()
    f_name_m = os.path.split(exc_tb_m.tb_frame.f_code.co_filename)[1]

    e_main = str(e_main)
    e_main = e_main.decode('cp1251', 'ignore')
    lmsg_e_main = '{server}\n{exc_type}, {f_name}, {exc_tb} \n{e}' \
        .format(exc_type=exc_type_m, f_name=f_name_m, exc_tb=exc_tb_m.tb_lineno, e=e_main.encode('utf-8'),
                server=server_pos_set)
    logg_main.error(lmsg_e_main)
else:
    pass
