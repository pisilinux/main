#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("./autogen.sh --prefix=/usr --enable-man --enable-gtk-doc")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.make("-C tools/completions PREFIX=%s/usr/share install-zsh-completion" % get.installDIR())
    

