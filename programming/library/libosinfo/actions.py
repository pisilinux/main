#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-D with-usb-ids-path=/usr/share/hwdata/usb.ids \
                          -D with-pci-ids-path=/usr/share/hwdata/pci.ids")

def build():
    mesontools.build()


def install():
    mesontools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
