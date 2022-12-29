#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -lpthread" % get.CFLAGS())

def setup():
    cmaketools.configure("-Denable-ladspa=ON \
                                        -DFLUID_DAEMON_ENV_FILE=/etc/conf.d/fluidsynth \
                                        -DLIB_SUFFIX=\"\"")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.insinto("/etc/conf.d", "fluidsynth.conf", "fluidsynth")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "THANKS", "TODO")
