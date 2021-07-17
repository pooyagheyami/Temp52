# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python

import wx
import wx.dataview
import wx.aui
from GUI.proman import Mymenu
import os


class MyLstPnl(object):
    LPn = []
    PrP = {}
    def __init__(self):
        dirfil = os.listdir('./GUI/AuiPanel/')
        for f in dirfil:
            if f[-3:] == '.py':
                self.LPn.append(f)
        self.LPn.remove( 'PAui.py')
        #print(self.LPn)

    def GetAuiPnl(self):
        return self.LPn

    def GetAuiPro(self):
        with open('./GUI/AuiPanel/PAui.p') as fl:
            lines = fl.readlines()
        for l in lines:
            self.PrP[l.split(',')[0]] = l.split(',')[1:]
        return self.PrP

    def GetAuiInfo(self,InfoList):
        myInfo = wx.aui.AuiPaneInfo()
        if ' Left' in InfoList:
            myInfo.Left()
        if ' Right' in InfoList:
            myInfo.Right()
        if ' Top' in InfoList:
            myInfo.Top()
        if ' Bottom' in InfoList:
            myInfo.Bottom()
        if ' PinButton' in InfoList:
            myInfo.PinButton(True)
        if ' Dock' in InfoList:
            myInfo.Dock()
        if ' Resizable' in InfoList:
            myInfo.Resizable()
        return myInfo