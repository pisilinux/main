#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "p7zip-%s" % get.srcVERSION()

makefiles = { 'x86_64'   : "makefile.linux_amd64_asm" }

def setup():
    shelltools.copy(makefiles[get.ARCH()], "makefile.machine")

def build():
    autotools.make('OPTFLAGS="%s %s" 7z 7za 7zr sfx' % (get.CFLAGS(), get.CXXFLAGS()))

def check():
    autotools.make("test")
    autotools.make("test_7z")
    autotools.make("test_7zr")

def install():
    autotools.rawInstall("DEST_DIR=%s DEST_HOME=/usr DEST_MAN=/usr/share/man" % get.installDIR())
