#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, pisitools, get

j = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -DBUILD_STATIC=ON',
    ' -DCMAKE_BUILD_TYPE=Release -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
