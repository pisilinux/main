#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.export("CFLAGS", "%s -g -I/usr/include/%s -Wall -fPIC" % (get.CFLAGS(), get.curPYTHON()))
    shelltools.export("LDFLAGS", "%s -shared" % get.LDFLAGS())

    autotools.make("USESELINUX=0")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
