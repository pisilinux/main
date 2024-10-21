#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

def setup():
    mesontools.configure("-Dwith-examples=false -Dwith-sd-bus-provider=elogind -Dwith-systemd-user-unit=false -Dwith-systemd-group=false")

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.dodoc("LICENSE*", "README*", "CHANGELOG*")
