#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

#WorkDir = "audacity-minsrc-%s" % get.srcVERSION()

def setup():
    #autotools.autoreconf("-vfi")
    #shelltools.cd("lib-src/portmixer")
    #shelltools.cd("../..")

    #autotools.aclocal("-I m4")
    #autotools.autoconf()
    #shelltools.export("LIBS", "-lavcodec")
    #shelltools.export("WX_CONFIG=wx-config-gtk3 ./configure", "/usr/bin/wxconfig")
    # suppress compiler warnings
    #pisitools.cxxflags.add("-Wno-unused-result -Wno-implicit-int -Wno-format-overflow -Wno-return-type -Wno-format-truncation -Wno-deprecated-declarations -Wno-unknown-pragmas -Wno-maybe-uninitialized -Wno-strict-prototypes -Wno-comment -Wno-implicit-function-declaration -Wno-pointer-to-int-cast -Wno-int-to-pointer-cast -Wno-enum-compare -Wno-aligned-new -Wno-class-memaccess -Wno-unused-but-set-variable -Wno-misleading-indentation -Wno-unused-variable -Wno-reorder -Wno-unused-function -Wno-sign-compare -Wno-unused-value -Wno-pessimizing-move -Wno-reorder -Wno-switch")

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-D CMAKE_INSTALL_PREFIX=/usr \
                            -D audacity_conan_enabled=OFF \
                            -D audacity_has_networking=OFF \
                            -D audacity_has_crashreports=OFF \
                            -D audacity_has_updates_check=OFF \
                            -D audacity_has_sentry_reporting=OFF \
                            -D audacity_lib_preference=system \
                            -D audacity_use_lv2:STRING=local \
                            -D audacity_use_portsmf:STRING=local \
                            -Daudacity_use_sbsms:STRING=local \
                            -D wxWidgets_CONFIG_EXECUTABLE:FILEPATH=/usr/bin/wx-config-gtk3 \
                            -D audacity_obey_system_dependencies=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/audacity")

    pisitools.dodir("/usr/share/audacity/help/manual")
