#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("--prefix=/usr \
	\
	--enable-gtk3 --enable-plugin \
	\
	--disable-dependency-tracking")

def build():
	autotools.make("PLUGINDIR=/usr/lib/xfce4/thunar-archive-plugin")

def install():
	autotools.rawInstall("DESTDIR=%s PLUGINDIR=/usr/lib/xfce4/thunar-archive-plugin" % get.installDIR())

	pisitools.dodoc("COPYING", "README")

