# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class Frame_UDS_UAMenu
###########################################################################

class Frame_UDS_UAMenu ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"UDS->UAMenu", pos = wx.DefaultPosition, size = wx.Size( 678,553 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bS_main = wx.BoxSizer( wx.VERTICAL )

		self.mp_1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 640,470 ), wx.TAB_TRAVERSAL )
		self.bs_uds = wx.BoxSizer( wx.HORIZONTAL )

		bs_2uds = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		bs_2uds.SetMinSize( wx.Size( 700,-1 ) )
		self.pn_1 = wx.Panel( self.mp_1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.pn_1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.st_spre_plata = wx.StaticText( self.pn_1, wx.ID_ANY, u"Spre plata:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_spre_plata.Wrap( -1 )

		gbSizer7.Add( self.st_spre_plata, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.et_suma_sp = wx.TextCtrl( self.pn_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.et_suma_sp.Enable( False )

		gbSizer7.Add( self.et_suma_sp, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.st_client_id = wx.StaticText( self.pn_1, wx.ID_ANY, u"ID/Nr telefon client:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_client_id.Wrap( -1 )

		gbSizer7.Add( self.st_client_id, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.et_uds_client = wx.TextCtrl( self.pn_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.et_uds_client, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.bt_uds_continue = wx.Button( self.pn_1, wx.ID_ANY, u"Continuare", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.bt_uds_continue, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )


		self.pn_1.SetSizer( gbSizer7 )
		self.pn_1.Layout()
		gbSizer7.Fit( self.pn_1 )
		bs_2uds.Add( self.pn_1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		self.pn_2 = wx.Panel( self.mp_1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.pn_2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.st_uds_total_points = wx.StaticText( self.pn_2, wx.ID_ANY, u"Total puncte loialitate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_total_points.Wrap( -1 )

		gbSizer8.Add( self.st_uds_total_points, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.st_uds_puncte_loialitate = wx.StaticText( self.pn_2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_puncte_loialitate.Wrap( -1 )

		gbSizer8.Add( self.st_uds_puncte_loialitate, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )

		self.st_max_bonus = wx.StaticText( self.pn_2, wx.ID_ANY, u"Max bonus:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_max_bonus.Wrap( -1 )

		gbSizer8.Add( self.st_max_bonus, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_max_bonus_val = wx.StaticText( self.pn_2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_max_bonus_val.Wrap( -1 )

		gbSizer8.Add( self.st_max_bonus_val, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.et_bonus_extract = wx.TextCtrl( self.pn_2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		gbSizer8.Add( self.et_bonus_extract, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.bt_set_non_points = wx.Button( self.pn_2, wx.ID_ANY, u"Fara puncte", wx.DefaultPosition, wx.Size( 130,35 ), 0 )
		self.bt_set_non_points.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer8.Add( self.bt_set_non_points, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.bt_set_points = wx.Button( self.pn_2, wx.ID_ANY, u"Cu puncte", wx.DefaultPosition, wx.Size( 130,35 ), 0 )
		self.bt_set_points.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.bt_set_points.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		gbSizer8.Add( self.bt_set_points, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self.pn_2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		self.m_staticline1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gbSizer8.Add( self.m_staticline1, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.st_spre_plata2 = wx.StaticText( self.pn_2, wx.ID_ANY, u"Spre Plata:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_spre_plata2.Wrap( -1 )

		gbSizer8.Add( self.st_spre_plata2, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_suma_sp2 = wx.StaticText( self.pn_2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_suma_sp2.Wrap( -1 )

		gbSizer8.Add( self.st_suma_sp2, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.st_cash_back = wx.StaticText( self.pn_2, wx.ID_ANY, u"CashBack:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_cash_back.Wrap( -1 )

		gbSizer8.Add( self.st_cash_back, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_cashback_val = wx.StaticText( self.pn_2, wx.ID_ANY, u"0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_cashback_val.Wrap( -1 )

		gbSizer8.Add( self.st_cashback_val, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.st_uds_sum_total = wx.StaticText( self.pn_2, wx.ID_ANY, u"Total:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_sum_total.Wrap( -1 )

		self.st_uds_sum_total.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer8.Add( self.st_uds_sum_total, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_uds_sum_total_val = wx.StaticText( self.pn_2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_sum_total_val.Wrap( -1 )

		self.st_uds_sum_total_val.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer8.Add( self.st_uds_sum_total_val, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.pn_2.SetSizer( gbSizer8 )
		self.pn_2.Layout()
		gbSizer8.Fit( self.pn_2 )
		bs_2uds.Add( self.pn_2, 1, wx.ALL|wx.EXPAND, 5 )

		self.pn_3 = wx.Panel( self.mp_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.st_uds_nrcheck = wx.StaticText( self.pn_3, wx.ID_ANY, u"Nr. Check:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_nrcheck.Wrap( -1 )

		gbSizer9.Add( self.st_uds_nrcheck, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_uds_nrcheck_val = wx.StaticText( self.pn_3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_nrcheck_val.Wrap( -1 )

		gbSizer9.Add( self.st_uds_nrcheck_val, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.st_uds_casir = wx.StaticText( self.pn_3, wx.ID_ANY, u"Casier:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_casir.Wrap( -1 )

		gbSizer9.Add( self.st_uds_casir, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_uds_casir_val = wx.StaticText( self.pn_3, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_casir_val.Wrap( -1 )

		gbSizer9.Add( self.st_uds_casir_val, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticline3 = wx.StaticLine( self.pn_3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer9.Add( self.m_staticline3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.st_spre_plata3 = wx.StaticText( self.pn_3, wx.ID_ANY, u"Spre Plata:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_spre_plata3.Wrap( -1 )

		gbSizer9.Add( self.st_spre_plata3, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_spre_plata3_val = wx.StaticText( self.pn_3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_spre_plata3_val.Wrap( -1 )

		gbSizer9.Add( self.st_spre_plata3_val, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.st_cash_back2 = wx.StaticText( self.pn_3, wx.ID_ANY, u"CashBack:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_cash_back2.Wrap( -1 )

		gbSizer9.Add( self.st_cash_back2, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_cash_back2_val = wx.StaticText( self.pn_3, wx.ID_ANY, u"0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_cash_back2_val.Wrap( -1 )

		gbSizer9.Add( self.st_cash_back2_val, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.st_uds_bonus = wx.StaticText( self.pn_3, wx.ID_ANY, u"Bonus UDS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_bonus.Wrap( -1 )

		gbSizer9.Add( self.st_uds_bonus, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_uds_bonus_val = wx.StaticText( self.pn_3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_bonus_val.Wrap( -1 )

		gbSizer9.Add( self.st_uds_bonus_val, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.st_uds_sum_total2 = wx.StaticText( self.pn_3, wx.ID_ANY, u"Total:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_sum_total2.Wrap( -1 )

		self.st_uds_sum_total2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.st_uds_sum_total2.SetMinSize( wx.Size( 100,-1 ) )

		gbSizer9.Add( self.st_uds_sum_total2, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.st_uds_sum_total2_val = wx.StaticText( self.pn_3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_uds_sum_total2_val.Wrap( -1 )

		self.st_uds_sum_total2_val.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer9.Add( self.st_uds_sum_total2_val, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.bt_uds_pay = wx.Button( self.pn_3, wx.ID_ANY, u"Achita", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bt_uds_pay.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.bt_uds_pay.SetMinSize( wx.Size( 130,35 ) )

		gbSizer9.Add( self.bt_uds_pay, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.st_tatal_poits_befor = wx.StaticText( self.pn_3, wx.ID_ANY, u"Total puncte loialitate dupa achitare:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_tatal_poits_befor.Wrap( -1 )

		self.st_tatal_poits_befor.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer9.Add( self.st_tatal_poits_befor, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.st_tatal_poits_befor_val = wx.StaticText( self.pn_3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_tatal_poits_befor_val.Wrap( -1 )

		self.st_tatal_poits_befor_val.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gbSizer9.Add( self.st_tatal_poits_befor_val, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.pn_3.SetSizer( gbSizer9 )
		self.pn_3.Layout()
		gbSizer9.Fit( self.pn_3 )
		bs_2uds.Add( self.pn_3, 1, wx.ALL|wx.EXPAND, 5 )

		self.pn_4 = wx.Panel( self.mp_1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.st_transaction_id = wx.StaticText( self.pn_4, wx.ID_ANY, u"Transaction ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_transaction_id.Wrap( -1 )

		self.st_transaction_id.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer6.Add( self.st_transaction_id, 0, wx.ALL, 5 )

		self.st_transaction_id = wx.StaticText( self.pn_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_transaction_id.Wrap( -1 )

		self.st_transaction_id.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer6.Add( self.st_transaction_id, 0, wx.ALL, 5 )


		bSizer12.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.st_sum_return = wx.StaticText( self.pn_4, wx.ID_ANY, u"Suma return:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_sum_return.Wrap( -1 )

		bSizer10.Add( self.st_sum_return, 0, wx.ALL, 5 )

		self.et_sum_return = wx.TextCtrl( self.pn_4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.et_sum_return.Enable( False )

		bSizer10.Add( self.et_sum_return, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer12.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.bt_return = wx.Button( self.pn_4, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		self.bt_return.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.bt_return.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer11.Add( self.bt_return, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer12.Add( bSizer11, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.pn_4.SetSizer( bSizer12 )
		self.pn_4.Layout()
		bSizer12.Fit( self.pn_4 )
		bs_2uds.Add( self.pn_4, 1, wx.EXPAND |wx.ALL, 5 )


		self.bs_uds.Add( bs_2uds, 1, wx.EXPAND, 5 )

		self.rt_uds_result = wx.richtext.RichTextCtrl( self.mp_1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.rt_uds_result.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		self.bs_uds.Add( self.rt_uds_result, 1, wx.EXPAND |wx.ALL, 5 )


		self.mp_1.SetSizer( self.bs_uds )
		self.mp_1.Layout()
		bS_main.Add( self.mp_1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bS_main )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.bt_uds_continue.Bind( wx.EVT_BUTTON, self.onclick_bt_uds_continue )
		self.bt_set_non_points.Bind( wx.EVT_BUTTON, self.onclick_bt_set_non_points )
		self.bt_set_points.Bind( wx.EVT_BUTTON, self.onclick_bt_set_points )
		self.bt_uds_pay.Bind( wx.EVT_BUTTON, self.onclick_bt_uds_pay )
		self.bt_return.Bind( wx.EVT_BUTTON, self.onclick_bt_return )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_close( self, event ):
		event.Skip()

	def onclick_bt_uds_continue( self, event ):
		event.Skip()

	def onclick_bt_set_non_points( self, event ):
		event.Skip()

	def onclick_bt_set_points( self, event ):
		event.Skip()

	def onclick_bt_uds_pay( self, event ):
		event.Skip()

	def onclick_bt_return( self, event ):
		event.Skip()


