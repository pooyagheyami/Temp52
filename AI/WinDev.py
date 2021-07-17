#In the name of GOD
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import wx


class MWC(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None)

    @property
    def CreateWin(self):
        return self.Create(self,None,1,'Main Window')

    def CreateMenu(self):
        pass

    def CreateTBar(self):
        pass

    def CreateStus(self):
        pass

    def CreatePans(self):
        pass

    def UpDateWin(self):
        pass

    def UpDateMenu(self):
        pass

    def UpDateTBar(self):
        pass

    def UpDateStus(self):
        pass

    def UpDatePans(self):
        pass


class WinDevUp(object):
    def __init__(self):
        pass

    def __getstate__(self):
        pass

    def getMenuBar(self):
        pass

    def getMenuItem(self):
        pass

    def getToolBar(self):
        pass

    def getStatue(self):
        pass

