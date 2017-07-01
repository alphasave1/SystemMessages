#===============================================================================================
# ÑKÑÄÑ~ÑÉÑÑÑpÑ~ÑÑÑç
#===============================================================================================

widthBW = 1000
heightBW = 600

#===============================================================================================
# ÑRÑÄÑxÑtÑpÑ~ÑyÑu ÑÜÑÖÑ~Ñ{ÑàÑyÑy ÑrÑçÑxÑÄÑrÑp ÑÄÑ{Ñ~Ñp ÑrÑÉÑÑÑÇÑÄÑuÑ~Ñ~ÑÄÑsÑÄ ÑqÑÇÑpÑÖÑxÑuÑÇÑp
#===============================================================================================

from adisp import process
from helpers import dependency
from skeletons.gui.game_control import IBrowserController

class BrowserWindow(object):

    @process
    def openBrowserWindow(self, url, title, browserID): 
        global widthBW, heightBW
        width = int(widthBW)
        height = int(heightBW)
        browserSize = [width, height]
        browserCtrl = dependency.instance(IBrowserController) 
        yield browserCtrl.load(url=url, title=title, browserID=browserID, browserSize=browserSize, showActionBtn=True, showCloseBtn=True, showWaiting=True)

g_browserWindow = BrowserWindow()

#===============================================================================================
# ÑRÑÄÑxÑtÑpÑ~ÑyÑu ÑÄÑ{Ñ~Ñp Ñr ÑàÑuÑ~ÑÑÑÇÑu ÑÖÑrÑuÑtÑÄÑ}Ñ|ÑuÑ~ÑyÑy ÑÉ Ñ{Ñ~ÑÄÑÅÑ{ÑÄÑz
#===============================================================================================

import BigWorld
import AccountCommands
import ArenaType
from gui import SystemMessages
from gui import DialogsInterface
from messenger import MessengerEntry
from notification.NotificationListView import NotificationListView
from notification.NotificationPopUpViewer import NotificationPopUpViewer
from notification.settings import NOTIFICATION_BUTTON_STATE
    
def messages():
    return {
        'typeID': 1,
        'message': {
            'bgIcon': '',
            'defaultIcon': '',
            'savedData': 0,
            'timestamp': -1,
            'filters': [],
            'buttonsStates': {'cancel': NOTIFICATION_BUTTON_STATE.HIDDEN},
            'buttonsLayout': [
                {
                    'action': 'action_1',
                    'type': 'submit',
                    'label': u'ÑKÑ~ÑÄÑÅÑ{Ñp 1',
                    'width': 80
                },
                {
                    'action': 'action_2',
                    'type': 'submit',
                    'label': u'ÑKÑ~ÑÄÑÅÑ{Ñp 2',
                    'width': 80
                }
            ],
            'type': 'black',
            'icon': '',
            'message': 'ÑPÑÇÑyÑ}ÑuÑÇ - ÑÅÑuÑÇÑuÑáÑÄÑt ÑÅÑÄ ÑÉÑÉÑçÑ|Ñ{Ñu',
        },
        'entityID': 99999,
        'auxData': ['GameGreeting']
    }

orig_getMessagesList = NotificationListView._NotificationListView__getMessagesList

def custom_getMessagesList(self):
    result = orig_getMessagesList(self)
    if self._NotificationListView__currentGroup in 'info':
        result.append(messages())
    return result

orig_onClickAction = NotificationListView.onClickAction

def custom_onClickAction(self, typeID, entityID, action):
    if action == 'action_1':
        BigWorld.wg_openWebBrowser('https://worldoftanks.ru/')
    elif action == 'action_2':
        g_browserWindow.openBrowserWindow("https://koreanrandom.com/forum/", "Koreanrandom", "99999")
    else:
        orig_onClickAction(self, typeID, entityID, action)

NotificationListView._NotificationListView__getMessagesList = custom_getMessagesList
NotificationListView.onClickAction = custom_onClickAction
