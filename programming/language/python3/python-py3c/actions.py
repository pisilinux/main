#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("sed -i 's/install: py3c.pc/install:/' Makefile")
    pythonmodules.compile(pyVer="3")
    autotools.make("prefix=/usr py3c.pc")

def install():
    #shelltools.system("make prefix=/usr install DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())

    pythonmodules.install(pyVer="3")

    pisitools.dodoc("LICENSE.MIT", "README.rst")
