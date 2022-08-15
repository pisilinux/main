#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "argon2"

def build():
    #shelltools.export("OS_CFLAGS", get.CFLAGS())
    #shelltools.export("OS_LDFLAGS", get.LDFLAGS())
    #shelltools.export("OS_CXXFLAGS", "%s -fno-strict-aliasing" % get.CXXFLAGS())

    shelltools.makedirs("phc-winner-argon2-20190702")
    autotools.make("OPTTARGET='none' LIBRARY_REL='lib' ARGON2_VERSION='%s'" % get.srcVERSION())

def install():
    autotools.rawInstall("DESTDIR=%s LIBRARY_REL='lib' LIBDIR=%s/usr/lib ARGON2_VERSION='%s'" % (get.installDIR(), get.installDIR(), get.srcVERSION()))

    pisitools.dodoc("LICENSE", "README.md")
