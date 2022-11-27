#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, get

j = ''.join([
    ' -B_build',
    ' -DUSE_VTE=ON',
    ' -DAUTO_RUN_TESTING=OFF',
    ' -DBUILD_GMOCK=OFF',
    ' -DBUILD_TESTING=OFF',
    ' -DINSTALL_GTEST=OFF',
    ' -DCMAKE_BUILD_TYPE=None',
    ' -L '
    ])

def setup():
#	shelltools.move("src/ct/icons.gresource.cc.tmp", "src/ct/icons.gresource.cc")
	cmaketools.configure(j)

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

#	pisitools.dodoc("../changelog.txt")
