#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

paths = ["JavaScriptCore", "WebCore", "WebKit", "WebKit2"]
docs = ["AUTHORS", "COPYING.LIB", \
        "LICENSE-LGPL-2", "LICENSE-LGPL-2.1", "LICENSE"]

def setup():
    shelltools.system("mkdir build")
    shelltools.cd("build")
    cmaketools.configure("-DPORT=GTK \
                          -DUSE_GTK4=ON \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIB_INSTALL_DIR=/usr/lib \
                          -DLIBEXEC_INSTALL_DIR=/usr/lib/webkit2gtk-6.0 \
                          -DENABLE_CREDENTIAL_STORAGE=ON \
                          -DENABLE_GEOLOCATION=ON \
                          -DENABLE_VIDEO=ON \
                          -DENABLE_WEB_AUDIO=ON \
                          -DENABLE_WEBGL=ON \
                          -DUSE_LIBHYPHEN=OFF \
                          -DUSE_SOUP2=OFF \
                          -DUSE_WOFF2=OFF \
                          -DUSE_SYSTEMD=OFF \
                          -DUSE_LIBBACKTRACE=OFF \
                          -DPYTHON_EXECUTABLE=/usr/bin/python3 \
                          -DJPEG_INCLUDE_DIR=/usr/include/openjpeg-2.5 \
                          -DSHOULD_INSTALL_JS_SHELL=ON \
                          -DUSE_WPE_RENDERER=OFF \
                          -DUSE_FLITE=OFF \
                          -DENABLE_MINIBROWSER=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/bin/WebKitWebDriver")

    pisitools.dodoc("../NEWS")
    shelltools.cd("../Source")
    for path in paths:
        for doc in docs:
            if shelltools.isFile("%s/%s" % (path, doc)):
                pisitools.insinto("%s/%s/%s" % (get.docDIR(), get.srcNAME(), path),
                                  "%s/%s" % (path, doc))
