#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tdesktop-%s-full" % get.srcVERSION()
wallet_engine_ver = "0.0.7"

def setup():
    # shelltools.system("rm -rf cmake/external/glib/cppgir/expected-lite")
    # shelltools.copy("expected-lite-*/*", "cmake/external/glib/cppgir/expected-lite")
    # shelltools.copy("cppgir-*/*", "cmake/external/glib/cppgir")

    shelltools.export("NINJAJOBS", "-j 4")
    shelltools.system("patch -p1 < fix-tgcalls-cstdint.patch -d Telegram/ThirdParty/tgcalls")

    shelltools.cd("wallet-engine-%s" % wallet_engine_ver)
    shelltools.system("patch -Np1 < wallet-engine.patch")
    # 'just' komutu kullanilarak derleniyor
    shelltools.system("just build")
    shelltools.system("just bindings-cpp")

    # Kutuphaneyi ve basliklari gecici bir dizine kur
    shelltools.system("mkdir -p install/lib install/include/wallet_engine")
    shelltools.system("cp target/release/libwallet_engine.a install/lib/")
    shelltools.system("cp bindings/cpp-experimental/* install/include/wallet_engine/")
    shelltools.cd("..")


    # shelltools.system("sed -i 's/DESKTOP_APP_USE_PACKAGED/NO_ONE_WILL_EVER_SET_THIS/' \
		# cmake/external/rlottie/CMakeLists.txt || die")
    shelltools.system('echo "target_link_libraries(external_webrtc INTERFACE jpeg Xcomposite Xdamage Xext Xfixes Xrandr Xrender Xtst X11)" | tee -a cmake/external/webrtc/CMakeLists.txt')
    pisitools.cxxflags.add("-Wno-deprecated-declarations -Wno-error=deprecated-declarations -Wno-switch -Wp,-U_GLIBCXX_ASSERTIONS")
    # shelltools.system("rm -rf Telegram/ThirdParty/libtgvoip/webrtc_dsp/absl")

	pisitools.cxxflags.add("-g1")

    params = ' '.join([
        '-B build',
        '-G Ninja',
        '-Ddisable_autoupdate=1',
        '-DCMAKE_BUILD_TYPE=None',
        '-DCMAKE_INSTALL_PREFIX="/usr"',
        '-DTDESKTOP_API_TEST=ON',
        '-DDESKTOP_APP_QT6=ON',
        '-DDESKTOP_APP_USE_PACKAGED=ON',
        '-DDESKTOP_APP_DISABLE_CRASH_REPORTS=ON',
        '-DDESKTOP_APP_SPECIAL_TARGET=""',
        '-DDESKTOP_APP_DISABLE_WAYLAND_INTEGRATION=ON',
        '-DCMAKE_DEPENDS_IN_PROJECT_ONLY=ON',
        '-DTDESKTOP_API_ID=611335',
        '-DTDESKTOP_API_HASH=d524b414d21f4d37f08684c1df41ac9c',
        '-DCMAKE_PREFIX_PATH="$PWD/wallet-engine-%s/install"' ,
        '-DTDESKTOP_LAUNCHER_BASENAME="telegramdesktop"'
    ]) % (wallet_engine_ver)

    cmaketools.configure(params)


def build():
    # shelltools.cd("build")
    shelltools.system("ninja -C build")
    # cmaketools.make("-j4")


def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    # shelltools.cd("build")
    # cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
