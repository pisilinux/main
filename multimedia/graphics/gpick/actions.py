#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def build():
	scons.make("USE_GTK3=True")

def install():
	scons.install("install DESTDIR=%s/usr USE_GTK3=True" % get.installDIR())

	pisitools.dodoc("LICENSE.txt", "README.md")

