#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

j = ''.join([
    ' -Ddbus=true',
    ' -Dopengl=true',
    ' -Dvsync_drm=true',
    ' -Dwith_docs=true',
    ' -Dconfig_file=true',
    ' -Dcompton=false '
    ])

def setup():
	mesontools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.insinto("/etc/xdg/", "picom.sample.conf", "picom.conf")

