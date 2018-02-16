#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    qt5.configure(parameters="USE_WEBGL=true \
                              QUPZILLA_PREFIX=/usr/ \
                              DISABLE_UPDATES_CHECK=true \
                              GNOME_INTEGRATION=true \
                              KDE_INTEGRATION=true ")

def build():
    qt5.make()

def install():
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())
    #zsh
    pisitools.insinto("/usr/share/zsh/site-functions", "linux/completion/*")

    pisitools.dodoc("AUTHORS", "BUILDING*", "CHANGELOG", "COPYRIGHT", "FAQ", "README*")
