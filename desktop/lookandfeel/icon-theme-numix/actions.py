#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

WorkDir = "numix-icon-theme_0.3+929~201712251402~ubuntu17.04.1"

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def install():
	pisitools.insinto("/usr/share/icons", "Numix")
