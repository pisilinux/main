#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

WorkDir = "elementary-xfce-0.7"

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def install():
	pisitools.insinto("/usr/share/icons", "elementary-xfce-dark")

