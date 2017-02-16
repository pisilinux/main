#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --enable-shared ")

def build():
    autotools.make()
    autotools.make('tools/qt-faststart')
    autotools.make("doc/ff{mpeg,play,server}.1")

def install():
    autotools.rawInstall("DESTDIR=%s install-man" % get.installDIR())
    pisitools.dobin("tools/qt-faststart")
    pisitools.dodoc("Changelog", "README.md", "LICENSE.md", "COPYING*")
