#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    shelltools.system("./bootstrap.py")
    shelltools.system("python waf configure --prefix=/usr  --confdir=/etc/mpv --enable-zsh-comp --enable-libmpv-shared --enable-cdda --disable-libsmbclient")

def build():
    shelltools.system("python waf build -v")

def install():
    shelltools.system("DESTDIR=%s python waf install" % get.installDIR())

    pisitools.dodoc("Copyright", "RELEASE_NOTES", "README.md")
