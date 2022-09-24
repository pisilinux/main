#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

i = "%s" % get.installDIR()

j = ''.join([
    ' -B_build',
    ' -DSPDLOG_BUILD_SHARED=ON',
    ' -DSPDLOG_FMT_EXTERNAL=ON',
    ' -DCMAKE_BUILD_TYPE=None',
    ' -L '
    ])

t = "#define SPDLOG_FMT_EXTERNAL"

def setup():
	cmaketools.configure(j)

def build():
	shelltools.cd("_build")
	cmaketools.make()

def install():
	shelltools.cd("_build")
	cmaketools.rawInstall("DESTDIR=%s" % i)

	pisitools.dosed("%s/usr/include/spdlog/tweakme.h" % i, ".*%s" % t, t)
