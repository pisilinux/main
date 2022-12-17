#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

def setup():
#	pisitools.dosed("doc/apireference.rst", "api", deleteLine = True)
	autotools.autoreconf("-vif")
	autotools.configure("--disable-static")

def build():
	autotools.make()
	# doc compilation.
	shelltools.cd("doc")
	autotools.make("man")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	# doc installation.
	pisitools.doman("doc/_build/man/*")
	#shelltools.copytree("doc/_build/html", "%s/usr/share/vapoursynth/html" % get.installDIR())
