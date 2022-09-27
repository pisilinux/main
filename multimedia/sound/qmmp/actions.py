#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

j = ''.join([
    ' -Bbuild',
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DCMAKE_INSTALL_LIBDIR=lib',
    ' -L '
    ])

def setup():
#    pisitools.dosed("src/plugins/Input/cdaudio/decoder_cdaudio.cpp", "cdio\/cdda\.h", r"cdio/paranoia/cdda.h")
    cmaketools.configure(j)

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
