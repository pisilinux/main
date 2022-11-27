#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

def setup():
    pass
#    pisitools.dosed("Makefile", "(cat pogo.py) \| \$\(CONFIGURE_IN\)( > pogo;)", r"\1\2")

def build():
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
