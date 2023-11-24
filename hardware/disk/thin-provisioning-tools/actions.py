#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# def setup():
    # autotools.autoreconf()

    # autotools.configure("--prefix=/usr")

def build():
    shelltools.system("cargo build --release")
    # autotools.make()

def install():
    autotools.rawInstall("BINDIR=%s/usr/sbin DATADIR=%s/usr/share DESTDIR=%s/usr" % (get.installDIR(), get.installDIR(), get.installDIR()))
