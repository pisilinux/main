#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("""DESTDIR=%s PREFIX="/usr\"""" % get.installDIR())

