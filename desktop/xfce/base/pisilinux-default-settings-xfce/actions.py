#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
	shelltools.chmod("etc/xdg/additional-logout", mode = 0755)

def install():
	pythonmodules.install()
	pisitools.insinto("/etc/skel/.config", "./etc/skel/xfce4", "xfce4")

