#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.cxxflags.add("-fpermissive")
    autotools.configure("--with-alsa \
                         --with-faac \
                         --with-vorbis \
                         --with-lame \
                         --without-jack")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FAQ", "NEWS", "README", "TODO")
