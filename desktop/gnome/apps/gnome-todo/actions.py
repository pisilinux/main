#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    pisitools.dosed("src/plugins/background/gtd-plugin-background.c", "libportal/portal-gtk4.h", "libportal-gtk4/portal-gtk4.h")
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "README*", "NEWS")
