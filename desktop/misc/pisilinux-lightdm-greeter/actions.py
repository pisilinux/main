#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2019 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    pass
def build():
    pass
def install():
    pisitools.insinto("/usr/share/web-greeter/themes/pisilinux-lightdm-theme", "*")