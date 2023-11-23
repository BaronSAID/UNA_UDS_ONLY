# coding=utf8
import wx

# setting app =============================
wind_mode = 1  # tipul rularii Serviciului:
#                   1: server,
#                   2: server + UI testare
#                   3: UDS
emulator_mode = False  # Activarea emulatorului

app_nr_version = 12
app_nr2_version = 7122022
CompanyName = 'Unisim-Soft'
FileDescription = 'Server POS'
InternalName = 'Server_POS'
OriginalFilename = 'Server_POSTerminal2'
ProductName = OriginalFilename
version_app = f'V {app_nr2_version}'
# =========================================

# server setting ==========================
server_listen_una_set = ('127.0.0.1', 8882)
server_pos_set = ('127.0.0.1', 8881)
recv_client_len = 4024000
# ========================================

# BPay service setting ===================
qr_invoice_name = 'qr_invoice.jpg'
url_bpay = 'bpay.md'
timer_invoice = 5
timer_invoice_loop = 2

buff_size = 512
sock_addr = 'tcp-socket.bpay.md'
sock_port = 8001
# ========================================

# QIWI Payment setting
public_key = 'QIWI\\publickey.crt'
private_key = 'QIWI\\pkcs8.key'
# =======================

# Type view form
form_show_method = [
    'SB',  # vizualizare pentru fiecare banca buton aparte
    'CBB', # setare banca, Bpay
    ''
]
# ========================================

CurrencyList = {
    '498': 'MDL',
    '840': 'USD',
    '978': 'EUR',
    '643': 'RUB',
    '509': 'RUP',
}
CurrencyList2 = {
    'MDL': '498',
    'USD': '840',
    'EUR': '978',
    'RUB': '643',
    'RUP': '509',
}

BanckList2 = {
    1:  'VB',    # Victoriabank
    2:  'MICB',  # moldincombank
    3:  'MAIB',  # moldova agro in bank
    4:  'FCB',   # Fincombank
    5:  'BPAY',  # BPay
    6:  'QIWI',  # QIWI
    7:  'SMK',   # SMarketoo
    8:  'APB',   # SAgroPromBank PMR
    9:  'VIRTUAL',   #
    -1: '00',    # Null
}
BanckList = {
    'VB':   1,   # Victoriabank
    'MICB': 2,   # moldincombank
    'MAIB': 3,   # moldova agro in bank
    'FCB':  4,   # Fincombank
    'BPAY': 5,   # BPay
    'QIWI': 6,   # QIWI
    'SMK':  7,   # SMarketoo
    'APB':  8,   # SAgroPromBank PMR
    'VIRTUAL':  9,   #
    '-1':   0,   # Null password-change
}

ListERR = {
            '000': 'Succesfully',
            '001': 'Failure, appeal to the bank',
            '110': 'Failure, appeal to the bank',
            '002': 'Failure, special term',
            '003': 'Invalid',
            '004': 'Card withdrawal',
            '005': 'Non - payment',
            '006': 'Failure',
            '007': 'Card withdrawal(special)',
            '008': 'Pay with identification',
            '009': 'The inquiry is not finished',
            '010': 'Authorised for the partial sum',
            '011': 'Approved (VIP)',
            '012': 'Transaction not done',
            '013': 'Incorrect sum',
            '014': 'Invalid card',
            '015': 'No connection with clients bank',
            '016': 'Approved, track record 3',
            '017': 'cancelled by the client',
            '018': 'Not confirmed by the client',
            '019': 'Repeat the transaction',
            '020': 'Incorrect answer',
            '021': 'No action taken',
            '022': 'System failure',
            '023': 'Unacceptable size of tax',
            '024': 'Operation not supported',
            '025': 'No initial operation',
            '026': 'Record duplication',
            '027': 'Error in record change',
            '028': 'File is blocked',
            '029': 'Error in file updating',
            '030': 'Incorrect format',
            '031': 'Unapprochable clients bank',
            '032': 'Partly finished',
            '033': 'Card is expired',
            '034': 'Suspicious card',
            '035': 'Appeal to the bank',
            '036': 'Card withdrawal (block)',
            '037': 'Card withdrawal (bank)',
            '038': 'Card withdrawal (PIN)',
            '039': 'No credit account',
            '040': 'Unapprochable function',
            '041': 'Card withdrawal/lost',
            '042': 'No joint account',
            '043': 'Card withdrawal/stolen',
            '044': 'No investment account',
            '051': 'Not enough means',
            '052': 'No account',
            '053': 'No account for savings',
            '054': 'Card is expired',
            '055': 'Invalid PIN',
            '056': 'Unknown card',
            '057': 'Transaction is forbidden',
            '058': 'Transaction is forbidden',
            '059': 'Suspicious operation',
            '060': 'Appeal to the bank',
            '061': 'The limit for the sum is exceeded',
            '062': 'Card is forbidden',
            '063': 'Enciphering error',
            '064': 'Incorrect sum',
            '065': 'The limit of operations is exceeded',
            '066': 'Appeal to the bank',
            '067': 'Card withdrawal/cash dispensal',
            '068': 'The answer recieved late',
            '075': 'The limit of PIN input is exceeded',
            '076': 'Incorrect PIN. The limit is settled',
            '077': 'Operation is impossible.',
            '078': 'Operation not found.',
            '079': 'This sum is cancelled.',
            '080': 'Network error',
            '081': 'Error in a foreign network',
            '082': 'Clients bank is unaprochable',
            '083': 'Impossible to finish',
            '086': 'Unable to verify PIN',
            '088': 'Enciphering error',
            '089': 'Identification error',
            '091': 'Clients bank is unaprochable',
            '092': 'Error in a bank network',
            '093': 'Law infringement',
            '094': 'Double transfer',
            '123': 'ERROR ',
            '096': 'Malfunction in system',
            '201': 'Check number is necessary',
            '202': 'Transaction is not found',
            '203': 'Refusal of sum input',
            '204': 'Refusal of sum input of initial operation',
            '205': 'Refusal of link input',
            '206': 'Incorrect link input',
            '207': 'Incorrect authorisation code',
            '208': 'Refusal of CVV2 input',
            '209': 'Refusal of currency input',
            '210': 'Refusal of authorisation code input',
            '211': 'Refusal of PIN code input',
            '212': 'Refusal of card input',
            '213': 'Refusal of businessman card input',
            '214': 'Incorrect manual input',
            '215': 'Refusal of card type input',
            '216': 'Refusal of operation input',
            '301': 'ID of the terminal is not set',
            '302': 'Impossible to cancel the operation ',
            '303': 'No change number',
            '304': 'The currency is not supported',
            '305': 'Card is not maintanced',
            '312':'Minimsal amount',
            '401': 'Error in card reading',
            '402': 'Connection error',
            '403': 'Connection breakage',
            '404': 'Exchange error',
            '992': 'Operation canceled',
            '984': 'PIN-PAD is busy performing an operation',
            '998': 'Communication error',
            '999': 'Answer code is not received',
            '600': 'NO CONNECTION POS',
            '601': 'Forced closing of the form',
            '602': 'BPay connect monitor error',
            '603': 'Time out expire',
            '604': 'Socket BPay connect error',
            '605': 'Message server UAMenu empty',
            '606': 'Unknown error',
            '607': 'Duplicate payment',
            '608': 'Denied payment',
            '609': 'Expired payment',
            '610': 'QIWI HTTP Eror',
            '611': 'Voucher is used',
            '612': 'Error connection URL'
        }
# Emulator result list ===================
emulator_result = {
    0: 'RespCode=600\nTransactionID=-1\nTerminalID=-1\nRespMSG=NO CONNECTION POS\nRCPT=NO CONNECTION POS',
    1: '''RespCode=000\nTransactionID=026001032145\nTerminalID=92406121\nRespMSG=Succesfully\nRCPT=       (+373) 22 54-89-40                             
     Two Goose S.R.L.         
   Two Goose S.R.L.-Test      
 Chisinau, str.Albisoara, 42    
TERMINAL ID : 92406121                      
            CEC 0046             
PLATA FARA NUMERAR   
SUMA   0.01  ''',
    2: '''RespCode=000\nTransactionID=026003995915\nTerminalID=49866589\nRespMSG=Succesfully\nRCPT=                                
        Тест язык             
        31 августа 141           
      Кишинёв, Малдова         
          МДЛ        
TERMINAL ID : 49866589 
          CEC N 0114           
     АПЛАТА        
     СУМА    0.01       MDL      
         ************6394          
''',
    3: '''RespCode=110\nTransactionID=026012150676\nTerminalID=P0106007\nRespMSG=Failure, appeal to the bank\nRCPT=TERMINAL ID:P0106007
! TRANZACTIE NEREUSITA !
    NU DESERVITI !!!
TERMINAL ID: P0106007
RRN: 026012150676
Autorizare: 000001
AID: A0000000031010
APP: VISA
Tip
tranzactie:Contactless
Client:
************6394 CEC 153
Suma: 0.01 MDL
SUMA NEVALABILA
COD RASPUNS: 110
======================
Va rugam sa contactati 
banca Dvs la numarul de
telefon indicat  pe
versoul cardului pentru
mai multe detalii...
Utilizati cardurile
MasterCard Contactless
pentru  achitari sigure
si comode.
========================''',
    4: '''RespCode=006\nTransactionID=026003995918\nTerminalID=49866589\nRespMSG=Failure\nRCPT=                                
           Test &               
        31 august 141           
      Chisinau, Moldova         
          MDL        
TERMINAL ID : 49866589 
          CEC N 0115           
     ACHITARE        
            EROARE !            
     SUMA    0.01       MDL      
         *******

Process finished with exit code 0
''',
    5: '''RespCode=000\nTransactionID=026003995915\nTerminalID=49866589\nRespMSG=Succesfully\nRCPT=                                
                 ЗАО "ТВКЗ "KVINT"
               KVINT
ID Терминала: 01000343
ID Организации: M00000123
              Чек 8823
               Оплата
              Одобрено
Сумма:                      1.00 RUP
         Комиссия 0.00 RUP
Итого:                      1.00 RUP
AID: A1004150420001    RADUGA Online
TVR: 0000008001            TSI: 0000
CID: 80             B1FF6C92AA776D6B
 
Карта: Clever                  07/23
        910401******1318:00
RRN:                    000557975296
Код авторизации:              2R38B2
Код ответа (хост):               000
Дата: 22/12/22 10:23:18
 
           Сохраните чек
====================================
'''
}
# ========================================


class wxColor:
    red = wx.Colour(240, 29, 29)
    green = wx.Colour(41, 214, 87)
    violet = wx.Colour(107, 55, 97)
    black = wx.Colour(0, 0, 0)


class LOG_CONST:
    name_log = '_Server_POS.log'

    LOGSavePath = 'LOG\\'

    START_APP = 'Run Application'
    CLOSE_APP = 'Close Application'
    ERRORUnknown = 'Unknown error: '

    Error = 'ERROR'
    Info = 'INFO'
    Warning_ = 'WARNING'
    pass


FILE_LANG_DICT_NAME = 'UDS_UAMenu_lang.csv'
DEFAULT_LANG_DICT = '''st_spre_plata,Spre plata:,For a fee:,К оплате:
st_client_id,ID/Nr telefon client,Client ID/Nr Phone,ID клиента/номер телефона
bt_uds_continue,Continue,Continue,Продолжать
st_uds_total_points,Total puncte loialitate:,Total loyalty points:,Всего баллов лояльности:
st_max_bonus,Max bonus:,Max bonus:,Максимальный бонус:
bt_set_non_points,Fara puncte,No points,Нет баллов
bt_set_points,Cu puncte,With points,С баллами
st_cash_back,CASHBACK,CASHBACK,CASHBACK
st_uds_sum_total,Total,Total,Сумма
st_uds_nrcheck,Nr. Check:,Nr. Check:,Нр. Чека:
st_uds_casir,Casier:,Unit:,Касир:
st_uds_bonus,Bonus UDS:,UDS Bonuses:,UDS Бонусы:
bt_uds_pay,Achita,Pay,Оплатить
st_transaction_id,ID Trsanzactie,ID Transaction,ИД трансакции
st_sum_return,Suma return,Suma return,Сума вазврата
bt_return,Return,Return,Возврат
v_msg_not_client,Introduceti/Scanati id client,Enter/Scan customer id,Введите/отсканируйте идентификатор клиента
v_err_not_id_popup,Opera?iunea nu poate fi continuat?. Verifica?i v?rog ID/Nr. de telefon client indicat,The operation cannot be continued. Please check ID/No. indicated customer phone number,Операция не может быть продолжена. Пожалуйста. проверьте ID/No. клиента
v_err_not_id_popup2,ID/Nr. Telefon,ID/No. Telephone,ID/№ телефон
v_err_not_id_popup3,Message UDS,Message UDS,Сообщение UDS
v_msg_popup_max_points,Reducerea poate fi aplicata pina la suma,The discount can be applied up to the amount,Скидка может быть применена до суммы
v_transaction_success,Tranzactie cu success,Successful transaction,Успешная транзакция
v_msg_indicate_trans_id,Indicati ID Tranzactie,Indicate Transaction ID,Укажите ид. транзакции
st_tatal_poits_befor,Total puncte loialitate dupa achitare:,Total loyalty points after payment:,Всего баллов лояльности после оплаты:
'''

"""
000=Успешно
001=Отказ, обратитесь банк
002=Отказ спец. условие
003=Неизвестный коммерсант
004=Карточку изъять
005=Не оплачивать
006=Ошибка
007=Карточку изъять (cпец)
008=Оплатить с идентификацией
009=Запрос не завершен
010=Разрешено для частичной суммы
011=Одобрено (VIP)
012=Транзакция не выполнена
013=Неверная сумма
014=Недействительная карточка
015=Нет связи с банком клиента
016=Одобрено, запись дорожки 3
017=Отменено клиентом
018=Не подтвеждено клиентом
019=Повтоpите транзакцию
020=Неправильный ответ
021=No action taken
022=Сбой системы
023=Неприемлемый размер налога
024=Операция не поддерживается
025=Нет исходной операции
026=Дублирование записи
027=Ошибка изменения записи
028=Файл блокирован
029=Ошибка обновления файла
030=Неправильный формат
031=Банк клиента недоступен
032=Завершено частично
033=Карточка просрочена
034=Подозрительная карточка
035=Свяжитесь с банком
036=Карточку изъять (блок.)
037=Карточку изъять (банк)
038=Карточку изъять (ПИН)
039=Нет кредитного счета
040=Функция недоступна
041=Карточку изъять/утеряна
042=Нет общего счета
043=Карточку изъять/украдена
044=Нет инвестиционного счета
051=Недостаточно сpедств
052=Нет счета
053=Нет счета для сбережений
054=Карточка просрочена
055=Неверный ПИН
056=Неизвестная карточка
057=Транзакция запрещена
058=Транзакция запрещена
059=Подозрительная операция
060=Позвоните в банк
061=Превышен лимит на сумму
062=Карточка запрещена
063=Ошибка шифрования
064=Неправильная сумма
065=Превышен лимит операций
066=Позвоните в банк
067=Карточку изъять/банкомат
068=Ответ получен поздно
075=Лимит ввода ПИН исчерпан
076=Неверный ПИН. Лимит исчерпан
077=Операция не доступна.
078=Операция не найдена.
079=Эта сумма уже отменена.
080=Ошибка в сети
081=Ошибка в зарубежной сети
082=Недоступен банк клиента
083=Невозможно завершить
086=Не могу проверить ПИН
088=Ошибка шифрования
089=Ошибка идентификации
091=Недоступен банк клиента
092=Ошибка в сети банка
093=Нарушение закона
094=Двойная передача
096=Неисправность в системе
201=Необходим номер чека
202=Транзакция не найдена
203=Отказ ввода суммы
204=Отказ ввода суммы исходной операции
205=Отказ ввода RRN
206=Неверный ввод ссылки
207=Неверный код авторизации
208=Отказ ввода CVV2
209=Отказ выбора валюты
210=Отказ ввода кода авторизации
211=Отказ ввода пин-кода
212=Отказ ввода карты
213=Отказ ввода карты кассира
214=Не верный ручной ввод
215=Отказ подтверждения типа карты
216=Отказ ввода операции
217=ОТМЕНА ПО ЧУЖОЙ КАРТЕ
218=ОПЕРАЦИЯ УЖЕ ОТМЕНЕНА
222=Ошибка формата Track2
230=Отказ ввода кода авторизации (Amex)
233=Карта не прочитана
234=Ошибка чтения чиповой карты
235=Превышение суммы оригинальной операции ( отмена / возврат)
250=Карта вытащена из ридера до окончания операций
301=Не задан ID терминала
302=Невозможно отменить операцию
303=Журнал переполнен, закрыть смену
304=Валюта не поддерживается
305=Карта не обслуживается
320=ОТКАЗ ОТ ПОДПИСИ 
321=СЛИШКОМ БОЛЬШАЯ СУММА
401=Ошибка чтения карты
402=Транзакция не поддерживается (ошибка конфигурации)
403=Ошибка настройки точки доступа (ошибка конфигурации)
404=Ошибка формата ответа хоста
405=НЕТ ОТЛОЖЕННЫХ ОПЕРАЦИЙ
410=Ошибка загрузки рабочего ключа
411=ARCUS: Истек тайм-аут чтения карты 
500=НЕ УДАЛОСЬ СОЗДАТЬ СЧЕТ В СИСТЕМЕ MOBICASH
501=СЧЕТ В СИСТЕМЕ MOBICASH НЕ БЫЛ ОПЛАЧЕН ЗА ОТВЕДЕННОЕ ВРЕМЯ
502=НЕ УДАЛОСЬ ОТМЕНИТЬ СЧЕТ В СИСТЕМЕ MOBICASH
503=НЕ УДАЛОСЬ ВЫПОЛНИТЬ ВОЗВРАТ
504=НЕКОРРЕКТНАЯ ПАРА ЛОГИН/ПАРОЛЬ
505=НЕ УДАЛОСЬ ЗАПРОСИТЬ СОСТОЯНИЕ СЧЕТА В СИСТЕМЕ MOBICASH
941=Не задан список операций (конфигурация ПО)
984=ПИН-ПАД занят выполнением операции
985=операция MIFARE DIRECT прекращена
987=Таймаут чтения карты
988=Ошибка формата данных на карте/ПЕРЕПОЛНЕНА ПАМЯТЬ СЛИПОВ
989=Ошибка чтения Track2
990=Отказ ввода карты
992=ОПЕРАЦИЯ ПРЕРВАНА КАССИРОМ ИЛИ КЛИЕНТОМ
996=Ошибка формата запроса с кассы
998=ОШИБКА СВЯЗИ, ПОЗВОНИТЕ В БАНК

600=НЕТ СВЯЗИ С POS
601=Forced closing of the form

"""