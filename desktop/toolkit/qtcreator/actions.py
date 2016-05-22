#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="qt-creator-opensource-src-%s" % get.srcVERSION()
def setup():
    
    shelltools.system("qmake-qt5 qtcreator.pro CONFIG+=release QTC_PREFIX=/usr")


def build():
    qt5.make()

def install():
    qt5.install()
    pisitools.rename("/usr/bin/qtcreator", "qtcreator-bin")
    pisitools.domove("/usr/share/qtcreator/debugger/LICENSE.GPL3-EXCEPT", "/usr/share/licenses/qtcreator")
