#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

j = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DMUST_BUILD_TOXAV=ON',
    ' -DDHT_BOOTSTRAP=OFF',
    ' -DENABLE_STATIC=OFF',
    ' -B_build -L '
    ])

def setup():
	pisitools.dosed("CMakeLists.txt", "RPATH", deleteLine = True)
	pisitools.unlinkDir("third_party/cmp")
	shelltools.system("ln -s cmp-e836703291392aba9db92b46fb47929521fac71f ./third_party/cmp")
	cmaketools.configure(j)

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	pisitools.insinto("/etc", "other/bootstrap_daemon/tox-bootstrapd.conf")

	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
