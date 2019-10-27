#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	shelltools.system("sed -i -e 's|$(CC) -o $@ $(OBJCLI) $(LDFLAGS) -L. -lxavs|$(CC) -o $@ $(OBJCLI) -L. -lxavs $(LDFLAGS)|' Makefile")
	shelltools.system("sed -i -e 's|xavs$(EXE): $(OBJCLI) $(SONAME)|xavs$(EXE): $(OBJCLI) $(SONAME) libxavs.a|' Makefile")
	autotools.configure()

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" %get.installDIR())


