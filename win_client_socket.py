# -*- coding: utf-8 -*-
# Created by Nicolae Gaidarji at 11.09.2020
from CONSTANT import *
from uis.Form_client_Socket import *
import socket
import os

class _mainFrame(mainForm):
    def __init__(self, arg):
        mainForm.__init__(self, arg)
        hostname = socket.gethostname()
        host = socket.gethostbyname(hostname)
        self.te_ip_addr.SetValue('127.0.0.1')
        self.te_port.SetValue('8882')
        self.rt_code.WriteText('/MSG1,1,498')

    def onclick_bt_clear(self, event):
        self.rt_result.Clear()

    def onclick_bt_send(self, event):
        code = self.rt_code.GetValue()
        ip_addr = self.te_ip_addr.GetValue()
        port = int(self.te_port.GetValue())
        print(code)

        if code == '':
            wx.MessageBox('Cimpul code este pustiu', LOG_CONST.Info, wx.OK | wx.ICON_INFORMATION)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip_addr, port))
            print('ok')

            msg = code
            sock.sendall(str(msg).encode())
            result = sock.recv(345666)
            self.rt_result.Clear()
            self.rt_result.WriteText(result)
            print(result)

def show_form():
    app = []
    Form_main = []

    app = wx.App()
    Form_main = _mainFrame(None)
    Form_main.Show()
    app.MainLoop()

    return 1


show_form()
