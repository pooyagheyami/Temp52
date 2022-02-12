# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python

from Allimp import wx , os

#import wx
import wx.dataview
import wx.aui

from GUI.proman import Mymenu
import Database.MenuSet2 as MS


class MyLstPnl2(object):
    LPn = []
    PrP = {}
    def __init__(self):
        self.MyMenu = MS.GetData(u'Menu2.db', u'')

        self.lstpnl = self.MyMenu.AllPanes()
        #dirfil = os.listdir('./GUI/AuiPanel/')
        dirfil = os.listdir('./Src/AUI/')
        for f in dirfil:
            if f[-3:] == '.py':
                self.LPn.append(f)
        #self.LPn.remove('PAui.py')
        #print(self.LPn)
        #print(self.lstpnl)

    def GetAuiPnl(self):
        return self.LPn

    def GetAuiPro(self):
        return self.PrP

    def GetAuiInfo(self, Pname):
        myInfo = wx.aui.AuiPaneInfo()
        for pnl in self.lstpnl:
            if pnl[1] == Pname:
                D1 = self.CreatData1(pnl[10])
                D2 = self.CreatData2([pnl[12],pnl[13],pnl[14]])
                Dok,DL = pnl[15].split(';')
                x,y,i,j=pnl[16].split(';')
                D3 = self.CreatData3( [m for m in DL]+[[int(x),int(y)],int(i),int(j)] )
                D4 = self.CreatData4( [pnl[1],pnl[9],pnl[3],pnl[11],Dok,pnl[2],pnl[4]] )
                myInfo = AuiInfoSet1(D1,myInfo)
                myInfo = AuiInfoSiz1(D2,myInfo)
                myInfo = AuiInfoDok1(D3,Dok,myInfo)
                myInfo = AuiInfoGen1(D4,myInfo)

        return myInfo


    def CreatData1(self, S):
        set1 = ['caption_visible', 'close_button', 'maximize_button', 'minimize_button', 'pine_button',
                'pane_border', 'show', 'gripper', 'center_pane', 'default_pane', 'toolbar_pane', 'moveable']
        data1 = {}
        i = 0
        for b in S:
            if b == 'T':
                data1[set1[i]] = True
            elif b == 'F':
                data1[set1[i]] = False
            else:
                continue
            i += 1
        return data1

    def CreatData2(self,L):
        set2 = [ 'best_size', 'min_size', 'max_size']
        data2 = {}
        i = 0
        for s in set2:
            w,h = L[i].split(';')
            data2[s] = wx.Size(int(w),int(h))
            i += 1
        return data2

    def CreatData3(self,D):
        set3 = ['dock_fixed', 'floatable', 'bottom Dockable', 'Top Dockable', 'Left Dockable', 'Right Dockable',
                'pane_position', 'aui_position', 'aui_row']
        data3 = {}
        i = 0
        for s in set3:
            if D[i] == 'T':
                data3[s] = True
            elif D[i] == 'F':
                data3[s] = False
            else:
                data3[s] = D[i]
            i += 1
        return data3

    def CreatData4(self,D):
        set4 = ['name', 'caption', 'float_size', 'resize', 'dock', 'docking', 'layer']
        data4 = {}
        i = 0
        for s in set4:
            data4[s] = D[i]
            i += 1
        return data4


def AuiInfoSet1(Data,myInfo):
    #myInfo = wx.aui.AuiPaneInfo()
    if not Data['caption_visible']:
        myInfo.CaptionVisible(False)
    if not Data['close_button']:
        myInfo.CloseButton(False)
    if Data['maximize_button']:
        myInfo.MaximizeButton(True)
    if Data['minimize_button']:
        myInfo.MinimizeButton(True)
    if Data['pine_button']:
        myInfo.PinButton(True)
    if not Data['pane_border']:
        myInfo.PaneBorder(False)
    if not Data['show']:
        myInfo.Hide()
    if Data['gripper']:
        myInfo.Gripper(True)
    if Data['center_pane']:
        myInfo.CenterPane()
    if Data['default_pane']:
        myInfo.DefaultPane()
    if Data['toolbar_pane']:
        myInfo.ToolbarPane()
    if not Data['moveable']:
        myInfo.Movable(False)
    return myInfo

def AuiInfoSiz1(Data,myInfo):
    #myInfo = wx.aui.AuiPaneInfo()
    if Data['best_size'] != wx.Size(-1, -1):
        myInfo.BestSize(Data['best_size'])
    if Data['min_size'] != wx.Size(-1, -1):
        myInfo.MinSize(Data['min_size'])
    if Data['max_size'] != wx.Size(-1, -1):
        myInfo.MaxSize(Data['max_size'])
    return myInfo

def AuiInfoDok1(Data,Dok,myInfo):
    #myInfo = wx.aui.AuiPaneInfo()
    if Data['dock_fixed']:
        myInfo.DockFixed(True)
    if not Data['floatable']:
        myInfo.Floatable(False)
    if not Data['bottom Dockable']:
        myInfo.BottomDockable(False)
    if not Data['Top Dockable']:
        myInfo.TopDockable(False)
    if not Data['Left Dockable']:
        myInfo.LeftDockable(False)
    if not Data['Right Dockable']:
        myInfo.RightDockable(False)
    if Dok == 'Float':
        myInfo.FloatingPosition(wx.Point(Data['pane_position'][0],Data['pane_position'][1]))
    if Data['aui_position'] != 0:
        myInfo.Position(Data['aui_position'])
    if Data['aui_row'] != 0:
        myInfo.Row(Data['aui_row'])
    return myInfo

def AuiInfoGen1(Data,myInfo):
    #myInfo = wx.aui.AuiPaneInfo()
    if Data['name'] != '':
        myInfo.Name(Data['name'])
    if Data['caption'] != '':
        myInfo.Caption(Data['caption'])
    if Data['float_size'] != '-1;-1':
        w,h = Data['float_size'].split(';')
        myInfo.FloatingSize(wx.Size(int(w),int(h)))
    if Data['resize'] == 'Resizable':
        myInfo.Resizable()
    if Data['resize'] == 'Fixed':
        myInfo.Fixed()
    if Data['dock'] == 'Dock':
        myInfo.Dock()
    if Data['dock'] == 'Float':
        myInfo.Float()
    if Data['docking'] == 'Top':
        myInfo.Top()
    if Data['docking'] == 'Center':
        myInfo.Center()
    if Data['docking'] == 'Left':
        myInfo.Left()
    if Data['docking'] == 'Right':
        myInfo.Right()
    if Data['docking'] == 'Bottom':
        myInfo.Bottom()
    if Data['layer'] != 0:
        myInfo.Layer(Data['layer'])
    return myInfo