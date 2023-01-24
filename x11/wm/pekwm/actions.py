#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, pisitools, get

i = ''.join([
    ' -DCMAKE_BUILD_TYPE=RELEASE',
    ' -DCMAKE_INSTALL_PREFIX=/usr -L '
    ])

def setup():
	cmaketools.configure(i)

def build():
	cmaketools.make()

def install():
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "NEWS.md")
