#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

i = ''.join([
    ' --disable-oss',
    ' --disable-coreaudio '
    ])

def setup():
    shelltools.export("CC", "/usr/bin/clang")
    shelltools.export("CXX", "/usr/bin/clang++")
    #shelltools.export("LDFLAGS", "%s -fuse-ld=lld -ldl " % get.LDFLAGS())
    autotools.configure(i)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("about.txt", "AUTHORS", "ChangeLog")
