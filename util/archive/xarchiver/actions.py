#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

t = 'PLUGINDIR=/usr/lib/xfce4/thunar-archive-plugin'

def setup():
	autotools.configure("--disable-gtk2 --enable-plugin --disable-dependency-tracking")

def build():
	autotools.make(t)

def install():
	autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(), t))

	pisitools.dodoc("COPYING", "README")

