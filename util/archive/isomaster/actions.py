#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("PREFIX=/usr DEFAULT_EDITOR=gedit")

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr DEFAULT_EDITOR=gedit" % get.installDIR())

    pisitools.dodoc("CHANGELOG.TXT", "CREDITS.TXT", "LICENCE.TXT", "README.TXT", "TODO.TXT")
