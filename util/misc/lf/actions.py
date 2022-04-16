#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lf-r%s" % get.srcVERSION()

def build():
	shelltools.export("version", "%s" % get.srcVERSION())
	shelltools.system("GO111MODULE=on GOPATH=%s gen/build.sh" % get.workDIR())

def install():
	pisitools.dobin("lf")
	pisitools.doman("lf.1")
	pisitools.insinto("/usr/share/applications", "lf.desktop")

	pisitools.dodoc("LICENSE", "README.md")
	for i in ["etc/*"]:
		pisitools.insinto("/usr/share/doc/lf/examples/", "%s" % i)

