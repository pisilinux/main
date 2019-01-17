# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
import glob

def install():
    shelltools.system("sed -i 's|lrelease-qt5|lrelease|g' setup.py")
    pythonmodules.install(pyVer = "3")

    
    
    
