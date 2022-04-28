#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

j = ''.join([
    ' -DSTRICT_OPTIONS=ON',
    ' -DPLATFORM_EXTENSIONS=ON',
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DUPDATE_CHECK=ON '
    ])

def setup():
	cmaketools.configure("-B_build %s -L" % j)

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
