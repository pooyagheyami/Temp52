#In the name of GOD
#please put your code under here
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import wx.aui
from  Config.Init import *

def main( panel=None ):
	mw = wx.FindWindowByName('main')
	#wx.aui.AuiManager.GetAllPanes()
	lstpane = mw.m_mgr.GetAllPanes()

	#print(lstpane)
	for pnl in lstpane:
		if not pnl.IsShown():
			pnl.Show()

	mw.m_mgr.Update()

if __name__ == '__main__':
	main()
