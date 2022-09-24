#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, pisitools, get

def setup():
	shelltools.system("go generate")

def build():
	shelltools.system("go build")

def install():
	pisitools.dobin("ymuse")
	pisitools.insinto("/usr/share/applications", "resources/*.desktop")
	shelltools.copytree("resources/icons", "%s/%s/icons" % (get.installDIR(), get.dataDIR()))
	shelltools.copytree("resources/i18n/generated", "%s/%s/locale" % (get.installDIR(), get.dataDIR()))
