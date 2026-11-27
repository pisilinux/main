#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

WorkDir = "numix-icon-theme_20.03.20+202005150555~ubuntu20.04.1"

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def install():
	pisitools.insinto("/usr/share/icons", "Numix-Light")
