#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

def install():
    for d in ["os", "platform", "device", "datamap", "install-script", "schema"]:
        pisitools.insinto("/usr/share/osinfo", d)

    pisitools.dodoc("LICENSE")
