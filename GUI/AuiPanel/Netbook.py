# In the name of God
# -*- coding: utf-8 -*-
# Windows and Panels main Frame File
#! /usr/bin/env python

import wx

class MyPanel(wx.Panel):
    def __init__(self,parent,id,pos,siz,style):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 142,396 ), style = wx.TAB_TRAVERSAL )

        self.parent = parent

        VSiz = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook2 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH)

        self.m_panel4 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook2.AddPage(self.m_panel4, u"a page", True)
        self.m_panel5 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook2.AddPage(self.m_panel5, u"a page", False)
        self.m_panel6 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook2.AddPage(self.m_panel6, u"a page", False)

        self.SetSizer(VSiz)
        self.Layout()
