#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

t = "-Dwith-usb-ids-path=/usr/share/hwdata/usb.ids -Dwith-pci-ids-path=/usr/share/hwdata/pci.ids"

def setup():
    mesontools.configure(t)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS")
