#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde6, shelltools


def setup():
    kde6.configure("-DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.dodoc("LICENSES/*",  "ChangeLog", "AUTHORS", "README*", "DESIGN")
