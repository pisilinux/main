#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde5

WorkDir="%s-%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    kde5.configure("-DWITH_KDE=1")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("AUTHORS", "COPYING.LGPL")
