#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, get

def setup():
	# unlock compile translations.
	shelltools.unlink("po/stamp-po")
	autotools.autoreconf("-if")
	autotools.configure()

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
