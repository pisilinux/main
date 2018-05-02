#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


datadir = "/usr/share/%s" % get.srcNAME()


def setup():
    cmaketools.configure("-DDATADIR=%s" % datadir)


def build():
    cmaketools.make()
    shelltools.system("./AstroMenace --pack --rawdata=./RAW_VFS_DATA --dir=./")

def install():
    pisitools.dobin("AstroMenace")
    pisitools.insinto(datadir, "gamedata.vfs")



    pisitools.dodoc("gpl-3.0.txt", "License.txt", "ReadMe.txt")


