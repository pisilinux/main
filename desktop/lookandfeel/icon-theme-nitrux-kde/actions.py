#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

WorkDir = "nitrux-icon-theme-kde-3.5.3/Nitrux"

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def install():
	pisitools.insinto("/usr/share/icons/Nitrux", "./actions")
	pisitools.insinto("/usr/share/icons/Nitrux", "./apps")
	pisitools.insinto("/usr/share/icons/Nitrux", "./categories")
	pisitools.insinto("/usr/share/icons/Nitrux", "./devices")
	pisitools.insinto("/usr/share/icons/Nitrux", "./emblems")
	pisitools.insinto("/usr/share/icons/Nitrux", "./mimetypes")
	pisitools.insinto("/usr/share/icons/Nitrux", "./places")
	pisitools.insinto("/usr/share/icons/Nitrux", "./status")
	pisitools.insinto("/usr/share/icons/Nitrux", "./index.theme")
	pisitools.insinto("/usr/share/icons/Nitrux", "./CREDITS")
	pisitools.insinto("/usr/share/icons/Nitrux", "./COPYING")
	

