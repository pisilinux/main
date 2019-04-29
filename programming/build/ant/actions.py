#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")

WorkDir = "apache-ant-%s" % get.srcVERSION()
anthome = "/usr/share/ant"
javadir = "/usr/share/java"

def build():
    shelltools.export("ANT_OPTS", "-Duser.home=%s" % WorkDir)
    shelltools.system("./build.sh dist")

def install():
    pisitools.insinto("/etc/ant/", "%s/etc/*" % WorkDir)
    pisitools.remove("/etc/ant/ant-bootstrap.jar")
    pisitools.insinto("/usr/share/java/ant/", "%s/lib/*" % WorkDir)
    pisitools.insinto("/usr/share/java/", "lib/optional/junit-4.12.jar", "junit.jar")
    pisitools.insinto("/usr/share/java/", "lib/optional/hamcrest-core-1.3.jar", "hamcrest.jar")
    pisitools.insinto("/usr/share/ant/lib/", "%s/lib/*" % WorkDir)
    pisitools.insinto("/usr/share/ant/bin/", "apache-ant-1.9.14/bin/*")
            

    for binsym in ["ant", "antRun", "antRun.pl", "complete-ant-cmd.pl", "runant.pl", "runant.py"]:
            pisitools.dosym("/usr/share/ant/bin/%s" % binsym , "/usr/bin/%s" % binsym)
            
    pisitools.insinto("/usr/share/doc/ant/", "%s/manual/*" % WorkDir) #for and-docs
    pisitools.dodoc("KEYS", "NOTICE", "README", "WHATSNEW", "LICENSE")
