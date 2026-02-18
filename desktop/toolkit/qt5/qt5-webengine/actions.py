#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get


def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("qtwebengine-5*", "qt5-webengine-%s" % get.srcVERSION())

    shelltools.cd("qt5-webengine-%s" % get.srcVERSION())

    shelltools.move("../qtwebengine-chromium-87-based/ninja", "%s/qt5-webengine-5.15.16/src/3rdparty" % get.workDIR())
    shelltools.move("../qtwebengine-chromium-87-based/gn", "%s/qt5-webengine-5.15.16/src/3rdparty" % get.workDIR())
    shelltools.move("../qtwebengine-chromium-87-based/chromium", "%s/qt5-webengine-5.15.16/src/3rdparty" % get.workDIR())

    shelltools.system("mkdir .git")
    pisitools.dosed(".qmake.conf", "5.15.19", "5.15.16")

    # shelltools.system("patch -p1 < qtwebengine-everywhere-src-5.15.5-TRUE.patch")

    shelltools.system("sed -i 's/NINJAJOBS/NINJA_JOBS/' src/core/gn_run.pro")


    # Disable jumbo build https://bugreports.qt.io/browse/QTBUG-88657 gcc10
    shelltools.system("sed -i 's|use_jumbo_build=true|use_jumbo_build=false|' -i src/buildtools/config/common.pri")

    shelltools.system("sed -i '1i#include <stdint.h>' src/3rdparty/chromium/base/trace_event/trace_arguments.h")
    shelltools.system("sed -i '1i#include <stdint.h>' src/3rdparty/chromium/cc/input/main_thread_scrolling_reason.h")
    shelltools.system("sed -i '1i#include <stdint.h>' src/3rdparty/chromium/cc/metrics/dropped_frame_counter.h")
    shelltools.system("sed -i '1i#include <stdint.h>' src/3rdparty/chromium/cc/input/snap_selection_strategy.h")

    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("qmake .. -- -proprietary-codecs \
                   -system-webp \
                   -system-opus \
                   -spellchecker \
                   -webengine-icu \
                   -webengine-kerberos \
                   -webengine-webrtc-pipewire")

    #qt5.configure("..")
    
def build():
    shelltools.cd("build")
    qt5.make()

def install():
    shelltools.cd("build")
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())

    #I hope qtchooser will manage this issue
    #for bin in shelltools.ls("%s/usr/lib/qt5/bin" % get.installDIR()):
       #pisitools.dosym("/usr/lib/qt5/bin/%s" % bin, "/usr/bin/%s-qt5" % bin)
    
    shelltools.cd("..")
    pisitools.dodoc("LICENSE*")
