#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, get

j = ''.join([
    ' -DAUTO_RUN_TESTING=OFF',
    ' -DINSTALL_GTEST=OFF',
    ' -DCMAKE_BUILD_TYPE=None '
    ])

def setup():
	shelltools.move("src/ct/icons.gresource.cc.tmp", "src/ct/icons.gresource.cc")
	cmaketools.configure("-B_build %s -LA" % j)

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

#	pisitools.dodoc("../changelog.txt")
