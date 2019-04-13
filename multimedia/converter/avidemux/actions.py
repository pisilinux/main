#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("bash ./bootStrap.bash")

def install():
    autotools.install("-C buildCore DESTDIR=%s install" % get.installDIR())
    autotools.install("-C buildQt5 DESTDIR=%s install" % get.installDIR())
    autotools.install("-C buildCli DESTDIR=%s install" % get.installDIR())
    autotools.install("-C buildPluginsCommon DESTDIR=%s install" % get.installDIR())
    autotools.install("-C buildPluginsQt5 DESTDIR=%s install" % get.installDIR())
    autotools.install("-C buildPluginsCLI DESTDIR=%s install" % get.installDIR())
    autotools.install("-C buildPluginsSettings DESTDIR=%s install" % get.installDIR())
    
    shelltools.chmod(get.installDIR() + "/usr/lib/libADM6*")
    
    pisitools.insinto("/usr/share/pixmaps", "avidemux_icon.png", "avidemux.png")

    pisitools.dodoc("COPYING", "AUTHORS", "License*")
    pisitools.doman("man/*")
