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
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DDISABLE_DEPRECATED_QT_FEATURES=ON',
    ' -DJS_PROVIDER=none',
    ' -DWEBVIEW_PROVIDER=none -L '
    ])

def setup():
	pisitools.cxxflags.add("-Wno-unused-result")
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure(j, sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../LICENSE", "../README.md")

