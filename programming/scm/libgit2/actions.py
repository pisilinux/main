#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2015 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    cmaketools.configure("-DTHREADSAFE:BOOL=ON \
                          -DREGEX_BACKEND=pcre2 \
                          -DUSE_SSH:BOOL=ON \
                          -DUSE_HTTP_PARSER=system")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/lib/libgit2.so.1.1", "/usr/lib/libgit2.so.1.0")

    #pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
