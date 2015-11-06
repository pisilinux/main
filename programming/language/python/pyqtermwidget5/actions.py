# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("pyqt5")
    #pisitools.dosed("config.py", "/PyQt5","/Py2Qt5")
    #pisitools.dosed("config.py", "​config.sip_bin​", "/usr/bin/py2sip")
    shelltools.system("python config.py")
    pisitools.dosed("Makefile", "^(CXXFLAGS.*)$", "\\1 -fpermissive")
    pisitools.dosed("sipQTermWidgetQTermWidget.cpp", "sipCpp->setColorScheme\(a0\)", "sipCpp->setColorScheme(QString::number(a0))")
    

def build():
    shelltools.cd("pyqt5")
    autotools.make()

def install():
    shelltools.cd("pyqt5")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README")

 
