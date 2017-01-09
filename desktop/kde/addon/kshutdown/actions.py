#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("./Setup-kf5.sh")
    kde5.configure("-DKS_KF5=ON")

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("ChangeLog", "LICENSE")

