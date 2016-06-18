#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pythonmodules.compile()
    pythonmodules.install()

    #Remove history-manager from systemsettings, we have a painful crash because of the thread problem of pykde/python
    #pisitools.remove("/usr/kde/4/share/kde4/services/kcm_historymanager.desktop")
