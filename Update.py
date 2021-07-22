#In the name of God
#Script for Update Project
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, zipfile

list_of_main_file = {u'AI':[u'Analiz',u'Generats',u'OpnFil',u'WinDev'],
                     u'Config':[u'Init'],
                     u'Database':[u'MenuSet2',u'PostGet',u'wxsq'],
                     u'DCC1':[u'AuiPan2',u'DBDev2',u'ListMenu1',u'MenuDev2',u'ProgDev2',u'ToolBar2'],
                     u'GUI':[u'BG2',u'MainMenu2',u'MainTool',u'proman',u'Start',u'window2'],
                     u'GUI.AuiPanel':[u'PAui'],
                     u'GUI.Main':[u'DBv1',u'MDv1',u'PAv1',u'PGv1',u'PPv1',u'TBv1',u'TPv1'],
                     u'GUI.Temp':[u'buyit',u'untitle'],
                     u'Utility':[u'DigitClack',u'eCalClak1',u'Tclacal3'],
                     }

def chk_update(lst_update,zip_file_name):
    for dir in list_of_main_file.keys():
        for fil in  list_of_main_file[dir] :
            if fil in lst_update:
                update_file(zip_file_name,fil,dir)


def update_file(zip_file_name,file_need_update,path_file):
    if zipfile.is_zipfile(zip_file_name):
        zipfil = zipfile.ZipFile(zip_file_name,u'r')
        nmlst = zipfil.namelist()
        for fil in nmlst:
            zipfil.extract(fil,path_file)
        zipfil.close()
