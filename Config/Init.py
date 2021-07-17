#In the name of God

import sys
import os
#import codecs


MAP = os.getcwd()

if MAP.find(u'\\') > 0:
    SLASH = u'\\'
else:
    SLASH = u'/'
    


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

DATABASE_PATH = os.path.join(MAP,opj(u'Database')+SLASH)

AI_PATH       = os.path.join(MAP,opj(u'AI')+SLASH)
ML_PATH       = os.path.join(AI_PATH,opj(u'ML')+SLASH)

DCC_PATH      = os.path.join(MAP,opj(u'DCC')+SLASH)

GUI_PATH      = os.path.join(MAP,opj(u'GUI')+SLASH)
RES_PATH      = os.path.join(MAP,opj(u'Res')+SLASH)

ICONS_PATH    = os.path.join(RES_PATH,opj(u'Icons')+SLASH)
ICON16_PATH   = os.path.join(ICONS_PATH,opj(u'16x16')+SLASH)
ICON32_PATH   = os.path.join(ICONS_PATH,opj(u'32x32')+SLASH)

PICS_PATH     = os.path.join(RES_PATH,opj(u'Pics')+SLASH)
SPALSH_PATH   = os.path.join(RES_PATH,opj(u'Splash')+SLASH)

UTILITY_PATH  = os.path.join(MAP,opj(u'Utility')+SLASH)
CONFIG_PATH   = os.path.join(MAP,opj(u'Config')+SLASH)
LOGS_PATH     = os.path.join(MAP,opj(u'Logs')+SLASH)

LOCALE_PATH   = os.path.join(MAP,opj(u'Locale')+SLASH)

TEMPS_PATH    = os.path.join(MAP,opj(u'Temps')+SLASH)


def thistxt(filename):
    with open(LOGS_PATH+filename,mode='r',encoding='utf-8') as f:
        lines = f.readlines()

    txt = ''
    for t in range(len(lines)):
            txt = txt + '\n' + lines[t]
    #print txt
    return txt