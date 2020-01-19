#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	shelltools.export("JAVA_HOME", "/usr/lib/jvm/java-7-openjdk")
	
	autotools.autoreconf("-vfi")
	autotools.configure()

def build():
    autotools.make()
    autotools.make("jni")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "COPYING", "README*")
