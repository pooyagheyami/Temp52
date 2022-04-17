# In the name of God
# Configuration Program
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil

#### Main Application Path = MAP , Os name and Slash of OS
MAP = os.getcwd()
MyOsIs = os.name
if sys.platform == u'win32':
    SLASH = u'\\'
else:
    SLASH = u'/'

####  Some Utility function
def opj(path):
    """Convert paths to the platform-specific separator"""
    st = os.path.join(*tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    #print st
    return st

def _displayHook(obj):
    """
    Custom display hook to prevent Python stealing '_'.
    """
    if obj is not None:
        print(repr(obj))

#### Path of Program source for use inside of program
DATABASE_PATH = os.path.join(MAP,opj(u'Database')+SLASH)

AI_PATH       = os.path.join(MAP,opj(u'AI')+SLASH)
ML_PATH       = os.path.join(AI_PATH,opj(u'MLA')+SLASH)
DL_PATH       = os.path.join(AI_PATH,opj(u'DL')+SLASH)
DCC_PATH      = os.path.join(MAP,opj(u'DCC1')+SLASH)

GUI_PATH      = os.path.join(MAP,opj(u'GUI')+SLASH)
RES_PATH      = os.path.join(MAP,opj(u'Res')+SLASH)
SRC_PATH      = os.path.join(MAP,opj(u'Src')+SLASH)

ICONS_PATH    = os.path.join(RES_PATH,opj(u'Icons')+SLASH)
ICON16_PATH   = os.path.join(ICONS_PATH,opj(u'16x16')+SLASH)
ICON32_PATH   = os.path.join(ICONS_PATH,opj(u'32x32')+SLASH)
ICONS_MENU    = os.path.join(ICONS_PATH,opj(u'Menu')+SLASH)
ICONS_TOOL    = os.path.join(ICONS_PATH,opj(u'Toolbar')+SLASH)

PICS_PATH     = os.path.join(RES_PATH,opj(u'Pics')+SLASH)
IMAGE_PATH    = os.path.join(RES_PATH,opj(u'Images')+SLASH)
SPALSH_PATH   = os.path.join(RES_PATH,opj(u'Splash')+SLASH)

UTILITY_PATH  = os.path.join(MAP,opj(u'Utility')+SLASH)
CONFIG_PATH   = os.path.join(MAP,opj(u'Config')+SLASH)
LOGS_PATH     = os.path.join(MAP,opj(u'Logs')+SLASH)

LOCALE_PATH   = os.path.join(MAP,opj(u'Locale')+SLASH)

TEMPS_PATH    = os.path.join(MAP,opj(u'Temps')+SLASH)

#### Source pass for user

Src_api = os.path.join(SRC_PATH,opj(u'API')+SLASH)
Src_aui = os.path.join(SRC_PATH,opj(u'AUI')+SLASH)
Src_dbf = os.path.join(SRC_PATH,opj(u'DBF')+SLASH)
Src_gui = os.path.join(SRC_PATH,opj(u'GUI')+SLASH)
Src_mla = os.path.join(SRC_PATH,opj(u'MLA')+SLASH)
Src_mlp = os.path.join(SRC_PATH,opj(u'MLP')+SLASH)
Src_prg = os.path.join(SRC_PATH,opj(u'PRG')+SLASH)


####  List of language to use in application
LANGUAGE_LIST = {1:"English",2:"Farsi",3:"French",4:"German",5:"Spanish",6:"Turkish"}
Database_type = {1:"sqlite",2:"mysql",3:"postgresql",4:"oracle",5:"sqlserver"}

#### other function to use in application
def thistxt(filename):
    with open(LOGS_PATH+filename,mode='r',encoding='utf-8') as f:
        lines = f.readlines()
    txt = ''
    for t in range(len(lines)):
            txt = txt + '\n' + lines[t]
    #print txt
    return txt

def fil2txt(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
    txt = ''
    for t in range(len(lines)):
        txt = txt + lines[t]
    return txt

def OpenListML():
    with open(CONFIG_PATH+u'MLmethod.ini', mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    MLlst = {}
    MLAlg = {}
    for t in range(len(lines)):
        #print(lines[t])
        if ':' in lines[t]:
            #print(lines[t].split(':'))
            L1 = lines[t].split(':')
            l1 = L1[1].split(';')
            #print(L1,l1)
            MLlst[(int(l1[0]),int(l1[1].rstrip('\n')))] = L1[0].strip(' ')

        if ',' in lines[t]  and '    ' == lines[t][:4]:
            #print(lines[t].split(','))
            L1 = lines[t].split(',')
            l0 = L1[0].strip(' ')
            l1 = L1[1].split(';')
            MLAlg[(int(l1[0]),int(l1[1].rstrip('\n')))] = l0

    #print(MLlst,MLAlg)
    return MLlst,MLAlg

def CopyIcon(iconfile):
    shutil.copy(iconfile, ICONS_PATH)