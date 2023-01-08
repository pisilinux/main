#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import perlmodules, pisitools, get

def setup():
	perlmodules.configure()
	pisitools.dosed("Makefile", "^OTHERLDFLAGS.*$", "OTHERLDFLAGS = %s" % get.LDFLAGS())

def build():
	perlmodules.make()

def check():
	perlmodules.make("test")

def install():
	perlmodules.install()
	pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "examples")

	pisitools.dodoc("Changes")
