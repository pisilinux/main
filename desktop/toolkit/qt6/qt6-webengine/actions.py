#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt6
from pisi.actionsapi import get

def setup():
    # shelltools.system("mkdir .git")
    # pisitools.dosed(".qmake.conf", "5.15.10", "5.15.5")

    #shelltools.unlinkDir("src/3rdparty")
    #shelltools.move("../qtwebengine-chromium-*", "src/3rdparty")
    #shelltools.system("mkdir src/3rdparty/chromium/.git")
    #shelltools.system("patch -p1 < qtwebengine-5.15.7-build_fixes-1.patch")
    # shelltools.system("patch -p1 < qtwebengine-everywhere-src-5.15.5-TRUE.patch")

    # shelltools.system("sed -i 's/NINJAJOBS/NINJA_JOBS/' src/core/gn_run.pro")

    #shelltools.copy("qtwebengine-release.sh", "%s/qtwebengine-release.sh" % get.workDIR())
    #shelltools.cd("%s" % get.workDIR())

    #shelltools.system("sh ./qtwebengine-release.sh")

    #shelltools.cd("qtwebengine-everywhere-opensource-src-%s" % get.srcVERSION())



    # Disable jumbo build https://bugreports.qt.io/browse/QTBUG-88657 gcc10
    # shelltools.system("sed -i 's|use_jumbo_build=true|use_jumbo_build=false|' -i src/buildtools/config/common.pri")

    #shelltools.system("sh ./qtwebengine-release.sh")
    #shelltools.system("git submodule init")
    #shelltools.system("git submodule update")
    
    # shelltools.makedirs("build")
    # shelltools.cd("build")
    #shelltools.export("QT5LINK", "/usr/lib/qt6/bin")
    #shelltools.export("QT5DIR", "/usr/lib/qt6")
    #shelltools.export("CFLAGS", "%s -I/usr/lib/sqlite3.16.2" % get.CFLAGS())
    #shelltools.system("qmake WEBENGINE_CONFIG+=use_proprietary_codecs WEBENGINE_CONFIG+=use_system_icu WEBENGINE_CONFIG+=use_system_protobuf WEBENGINE_CONFIG+=use_system_ffmpeg qtwebengine.pro")
    #pisitools.ldflags.add("-Wl,--no-keep-memory ")
    #shelltools.export("NINJAJOBS", "-j 4")
    # shelltools.system("qmake .. -- -proprietary-codecs \
                   # -system-ffmpeg \
                   # -system-webp \
                   # -system-opus \
                   # -spellchecker \
                   # -webengine-icu \
                   # -webengine-kerberos \
                   # -webengine-webrtc-pipewire")

    qt6.configure(" -DCMAKE_TOOLCHAIN_FILE=/usr/lib/cmake/Qt6/qt.toolchain.cmake \
                    -DQT_FEATURE_webengine_system_ffmpeg=ON \
                    -DQT_FEATURE_webengine_system_icu=OFF \
                    -DQT_FEATURE_webengine_system_libevent=ON \
                    -DQT_FEATURE_webengine_proprietary_codecs=ON \
                    -DQT_FEATURE_webengine_kerberos=ON \
                    -DQT_FEATURE_webengine_webrtc_pipewire=ON")
    
def build():
    # shelltools.cd("build")
    qt6.make()

def install():
    # shelltools.cd("build")
    qt6.install()

    #I hope qtchooser will manage this issue
    #for bin in shelltools.ls("%s/usr/lib/qt6/bin" % get.installDIR()):
       #pisitools.dosym("/usr/lib/qt6/bin/%s" % bin, "/usr/bin/%s-qt6" % bin)
    
    # shelltools.cd("..")
    pisitools.dodoc("LICENSES/**")
