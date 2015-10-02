#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("PREFIX=/usr BUILD_STATIC_LIB=0 MANDIR=/%s PROG_EXTRA=sensord DESTDIR=%s user_install" % (get.manDIR(), get.installDIR()))

    pisitools.dodoc("CHANGES", "CONTRIBUTORS", "README")
