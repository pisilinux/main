#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("JOBS", get.makeJOBS().replace("-j5", "5"))
options="WXPORT=gtk3 WX_CONFIG=/usr/bin/wx-config-gtk3"

def build():
    pythonmodules.compile(options)

def install():
    pythonmodules.install(options)
    # install only python libraries
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/share")
