#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    #shelltools.makedirs("wmctrl-1.0.7")
    autotools.configure()

def build():
    #shelltools.cd("wmctrl-1.0.7")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s LIBDIR=%s/usr/lib" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("COPYING", "README")
