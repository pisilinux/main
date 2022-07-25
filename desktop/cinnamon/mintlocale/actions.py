#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def install():
    shelltools.system("./makepot")
    pisitools.insinto("/usr/", "usr/*")
    #pisitools.insinto("/usr/bin/", "usr/bin/*")
    #pisitools.insinto("/usr/lib/linuxmint/mintlocale/", "usr/lib/linuxmint/mintlocale/*.py")
    #pisitools.insinto("/usr/lib/linuxmint/mintlocale/ImConfig/", "usr/lib/linuxmint/mintlocale/ImConfig/*.py")
    #pisitools.insinto("/usr/share/applications/", "usr/share/applications/*")
    #pisitools.insinto("/usr/share/icons/hicolor", "usr/share/icons/hicolor/*")
    #pisitools.insinto("/usr/share/linuxmint/adjustments/", "usr/share/linuxmint/adjustments/*")
    #pisitools.insinto("/usr/share/linuxmint/mintlocale/", "usr/share/linuxmint/mintlocale/*")
    #pisitools.insinto("/usr/share/polkit-1/actions/", "usr/share/polkit-1/actions/*")
