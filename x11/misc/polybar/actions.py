#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-D CMAKE_BUILD_TYPE=Release \
                          -DENABLE_ALSA=ON \
                          -DENABLE_CURL=ON \
                          -DENABLE_I3=ON \
                          -DBUILD_IPC_MSG=ON \
                          -DENABLE_NETWORK=ON \
                          -DENABLE_PULSEAUDIO=ON", sourceDir="..")
    

def build():
    
    shelltools.cd("build")
    
    cmaketools.make()
    cmaketools.make("doc")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
