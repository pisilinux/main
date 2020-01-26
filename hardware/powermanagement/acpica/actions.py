#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("sed -i -e 's/_CYGWIN/_LINUX/g' -e 's/-Werror//g' generate/unix/Makefile.*")
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    pisitools.dosed("generate/unix/iasl/Makefile", "-Werror", "")
    if get.ARCH() == "x86_64":
        autotools.make("BITS=64")
    else:
        autotools.make("BITS=32")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dodoc("changes.txt")
