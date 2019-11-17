#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="acr-2.7"

def build():
    shelltools.cd("source/src")
    autotools.make()

def install():
    shelltools.cd("source/src")
    autotools.rawInstall("DESTDIR=%s" %get.installDIR())
	
    shelltools.cd("../..")
    pisitools.insinto("/usr/share/acreloaded", "bot")
    pisitools.insinto("/usr/share/acreloaded", "config")
    pisitools.insinto("/usr/share/acreloaded", "packages")
    pisitools.insinto("/usr/share/acreloaded", "acr/packages")
    
    pisitools.insinto("/usr/share/acreloaded", "bin_unix/native_client")
    pisitools.insinto("/usr/share/acreloaded", "bin_unix/native_server")
    
    pisitools.insinto("/usr/share/doc/acreloaded", "source/README*")