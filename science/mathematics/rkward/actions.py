#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools


def setup():
    kde6.configure("-DR_HOME=/usr/lib/R")

def build():
    kde6.make()

def install():
    #for installing rbackend mkdir needed directory(for R-2.5.0)
    pisitools.dodir("/usr/lib/R/library")

    kde6.install()
    pisitools.dodoc("LICENSES/*")

    # TODO: this one seems better than the one in kdelibs
    #pisitools.remove("/usr/share/kde4/apps/katepart/syntax/r.xml")

