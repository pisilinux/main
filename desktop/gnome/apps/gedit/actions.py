#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import mesontools, pisitools, shelltools, get
import os


def setup():
    shelltools.cd("subprojects")
    shelltools.system("git clone https://gitlab.gnome.org/GNOME/libgd.git")
    shelltools.cd("..")

    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("NEWS", "README*", "COPYING")
