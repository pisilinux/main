# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
import glob

def install():
    pisitools.dosed("setup.py", "lrelease", "lrelease-qt6")
    pythonmodules.install(pyVer = "3")
    
    #pisitools.insinto("/usr/share/welcome/data/media-content", "data/media-content/logo.png")
