# In the name of God
# -*- coding: utf-8 -*-
# Windows Back Ground
# ! /usr/bin/env python

import wx
import wx.aui as wxaui
from Config.Init import *

import GUI.proman as pro

_ = wx.GetTranslation


class BGPanel(wx.Panel):
	def __init__(self, parent, BGfile):
		wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
		                  style=wx.TAB_TRAVERSAL)

		# bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.BGfile = BGfile

		self.SetBackgroundStyle(wx.BG_STYLE_ERASE)
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

		self.Bind(wxaui.EVT_AUI_RENDER, self.OnEraseBackground)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class

	def m_bitmap4OnContextMenu(self, event):
		self.PopupMenu(self.m1)



	def OnEraseBackground(self, evt):
		# yanked from ColourDB.py
		# print(evt)
		dc = evt.GetDC()
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			# dc.SetClippingRect(rect)
			dc.SetClippingRegion(rect)
		dc.Clear()
		# bmp = wx.Bitmap(PICS_PATH+self.BGfile)
		bmp = wx.Bitmap(self.BGfile)
		img = bmp.ConvertToImage()
		img2 = img.Scale(wx.GetDisplaySize()[0], wx.GetDisplaySize()[1])
		bmp2 = img2.ConvertToBitmap()

		dc.DrawBitmap(bmp2, 0, 0)

	def ChangeBackGround(self):
		dc = wx.ClientDC(self)
		rect = self.GetUpdateRegion().GetBox()
		dc.SetClippingRegion(rect)
		dc.Clear()
		bmp = wx.Bitmap(self.BGfile)
		img = bmp.ConvertToImage()
		img2 = img.Scale(wx.GetDisplaySize()[0], wx.GetDisplaySize()[1])
		bmp2 = img2.ConvertToBitmap()
		dc.DrawBitmap(bmp2, 0, 0)
		self.Refresh()
