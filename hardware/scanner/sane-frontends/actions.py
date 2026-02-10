#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir="sane-frontends-%s" % get.srcVERSION()

def setup():
    pisitools.cflags.add("-std=gnu11")
    shelltools.system("sed -i 's/isfdtype(fileno(stderr), S_IFSOCK)/0/' sanei/sanei_init_debug.c")
    autotools.configure("--with-gnu-ld")

def build():
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README")

    # There's xsane instead
    pisitools.remove("/usr/bin/xscanimage")
    pisitools.remove("/usr/share/man/man1/xscanimage.1")
    pisitools.removeDir("/usr/share/sane")
