import BigWorld
from gui import SystemMessages
from Account import Account

link = Account.onBecomePlayer

def _First(self):
        link(self)
        msg = '<font color="#cc9933"><b>Hello</b></font>'
        type = SystemMessages.SM_TYPE.Information
        SystemMessages.pushMessage(msg, type)

Account.onBecomePlayer = _First
