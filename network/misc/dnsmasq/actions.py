#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())

def install():
    autotools.rawInstall("PREFIX=/usr DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "CHANGELOG.archive", "FAQ", "COPYING", "COPYING-v3", "doc.html")
