#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

JAVA_HOME = "/usr/lib/jvm/java-7-openjdk"

def setup():
	shelltools.export("JAVA_HOME", "%s" %JAVA_HOME)
	shelltools.export("CFLAGS", "%s -I%s/include -I%s/include/linux" %(get.CFLAGS(), JAVA_HOME, JAVA_HOME))
	shelltools.export("CXXFLAGS", "%s -I%s/include -I%s/include/linux" %(get.CXXFLAGS(), JAVA_HOME, JAVA_HOME))
	
	autotools.autoreconf("-vfi")
	autotools.configure()

def build():
    autotools.make()
    autotools.make("jni")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "COPYING", "README*")
