#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    '--disable-r ',
    '--disable-io ',
    '--disable-lua ',
    '--disable-php ',
    '--disable-rpath ',
    '--disable-sharp ',
    '--disable-ocaml ',
    '--disable-static ',
    '--disable-dependency-tracking ',
    '--with-libgd ',
    '--with-fontconfig ',
    '--with-pangocairo ',
    '--without-devil ',
    ])

def setup():
    shelltools.export("CONFIG_SHELL", "/bin/bash")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure(j)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml(".")
    pisitools.dodoc("AUTHORS", "CHANGELOG.md", "DEVELOPERS.md", "INSTALL", "LICENSE", "README.md")

    pisitools.removeDir("/usr/share/graphviz/doc")

