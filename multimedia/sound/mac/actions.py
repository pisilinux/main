#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, get

WorkDir = "."
opts = "prefix=/usr -C Source/Projects/NonWindows"

def setup():
	pass

def build():
	autotools.make(opts)

def install():
	autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(), opts))
