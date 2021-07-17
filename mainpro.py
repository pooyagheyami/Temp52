# In the name of God
# Main Program Start
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import wx.adv



#import builtins
#builtins.__dict__['_'] = wx.GetTranslation
import sys 
import glob
import os

import GUI.window as window
import GUI.window2 as window2
import GUI.Start as Strt
from Config.Init import *

#import Utility.user as user

class mainApp(wx.App):

    def OnInit(self):
        #self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.locale = None
        wx.Locale.AddCatalogLookupPathPrefix(LOCALE_PATH)
        self.config = self.GetConfig()
        lang = self.config.Read("Language")
        #print(type(lang))
        if lang == '1':
            langtxt = "English"
        elif lang == '2':
            langtxt = "Turkish"
        elif lang == '3':
            langtxt = "Farsi"
        else:
            langtxt = ""
        #print(langtxt)
        self.UpdateLanguage(langtxt)
        self.SetAppName('Temp5')
        splash = Strt.MySplashScreen(window2)
        splash.Show(True)
        return True

    def GetConfig(self):
        config = wx.FileConfig(appName='Temp5',localFilename=CONFIG_PATH+'option.ini',globalFilename=CONFIG_PATH+'system1.ini')
        return config

    def UpdateLanguage(self, lang):
        supportedLangs = {"English": wx.LANGUAGE_ENGLISH,
                          "Farsi": wx.LANGUAGE_FARSI,
                          "Turkish": wx.LANGUAGE_TURKISH,
                          }
        if self.locale:
            assert sys.getrefcount(self.locale) <= 2
            del self.locale
        if supportedLangs[lang]:
            self.locale = wx.Locale(supportedLangs[lang])
            if self.locale.IsOk():
                self.locale.AddCatalog("wx1fa")
                self.locale.AddCatalog("wx2fa")

                self.locale.AddCatalog("wx2tr")
            else:
                self.locale = None
        else:
            wx.MessageBox("Language support not found please sending an email to us for update new language!")




if __name__ == '__main__':
    app = mainApp()
    app.MainLoop()
