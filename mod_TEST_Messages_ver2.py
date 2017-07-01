# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: TEST_Messages_ver2
# Compiled at: 2017-07-01 20:38:07
from PlayerEvents import g_playerEvents
from gui import SystemMessages
from gui.SystemMessages import SM_TYPE
URLLINK='http://www.twitter.com/alphasave1'

def init():
    g_playerEvents.onAccountBecomePlayer += __onAccountBecomePlayer


def __onAccountBecomePlayer():
    SystemMessages.pushMessage("<font color='#BFE9FF'>mod_TestMessages</font>\n", type=SystemMessages.SM_TYPE.GameGreeting)
    SystemMessages.pushMessage("<font color='#BFE9FF'>Twitter</font> Page:\n<font color='#C5AB5D'>at <a href='event:" + URLLINK + "'>here</a>.</font>\n", type=SystemMessages.SM_TYPE.GameGreeting)
