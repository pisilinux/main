#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s/%s" % (get.ARCH(), get.srcNAME())
BASEDIR = "/usr/share/java/zekr"

shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")
#def setup():    

#def build():    

def install():
    pisitools.insinto(BASEDIR, "*")
    pisitools.dosym("%s/zekr.sh" % BASEDIR, "/usr/bin/zekr")

    pisitools.dodoc("doc/changes.txt", "doc/license/*", "doc/readme.txt")
