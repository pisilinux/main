#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    ' -DWITH_ALSA=ON',
    ' -DWITH_NATIVE=OFF -L '
    ])

def setup():
	cmaketools.configure("-B_build %s" % j)

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../AUTHORS", "../ChangeLog")

