# In the name of God
# -*- coding: utf-8 -*-
# !usr/bin/env python

import wx
import DCC1.ToolBar2 as TBV
from Config.Init import *


class telframe(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, style=wx.FRAME_FLOAT_ON_PARENT | wx.DEFAULT_FRAME_STYLE)
        self.parent = parent


        self.panel = TBV.MyPanel1(self)

    def closeit(self):
        self.Close(True)


def size():
    return (-1, -1)


def main(panel=None):
    #locale = wx.Locale(wx.LANGUAGE_ENGLISH)

    parent = panel.GetParent()

    frame = telframe(parent)
    frame.SetTitle(u'Tool Bar Develop')
    frame.SetSize((555, 500))
    frame.Show()


if __name__ == '__main__':
    main()
