#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, get

i = ''.join([
    ' --extra-ldflags="-Wl,-z,noexecstack"',
    ' --chroma-format="all"',
    ' --enable-shared '
    ])

def setup():
    shelltools.cd("build/linux")
    autotools.configure(i)

def build():
    shelltools.cd("build/linux")
    autotools.make()

def install():
    shelltools.cd("build/linux")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
