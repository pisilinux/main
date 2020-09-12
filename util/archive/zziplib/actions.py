#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("JOBS", get.makeJOBS().replace("-j5", "-j1"))

def setup():
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib -L", sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()
	cmaketools.make("docs")

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dohtml("docs/*.htm*")
	shelltools.cd("..")
	pisitools.dodoc("ChangeLog", "COPYING.LIB", "README", "TODO", "docs/COPYING*", "docs/README.SDL")

