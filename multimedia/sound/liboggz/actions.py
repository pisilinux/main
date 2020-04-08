#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get


def setup():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-int-to-pointer-cast -Wno-cast-function-type -Wno-pointer-to-int-cast")
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*")
    pisitools.insinto("/usr/share/bash-completion/completions/","bash-completion/oggz")