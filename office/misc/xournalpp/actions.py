#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
#	shelltools.export("CFLAGS", "-lpthread")
	pisitools.cxxflags.add("-Wno-unused-result -Wno-deprecated-declarations")

	cmaketools.configure("-B_build -DCMAKE_BUILD_TYPE=Release")

def build():
	shelltools.cd("_build")
	cmaketools.make()
	cmaketools.make("translations")

def install():
	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../AUTHORS", "../CHANGELOG.md", "../LICENSE", "../README.md")

