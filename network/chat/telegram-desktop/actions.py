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


def setup():
    shelltools.export("NINJAJOBS", "-j 4")
    #shelltools.export("LC_ALL", "en_US.UTF-8")
    shelltools.system("sed -i 's/DESKTOP_APP_USE_PACKAGED/NO_ONE_WILL_EVER_SET_THIS/' \
		cmake/external/rlottie/CMakeLists.txt || die")
    shelltools.system('echo "target_link_libraries(external_webrtc INTERFACE jpeg)" | tee -a cmake/external/webrtc/CMakeLists.txt')
    pisitools.cxxflags.add("-Wno-deprecated-declarations -Wno-error=deprecated-declarations -Wno-switch")
    params = ' '.join([
        '-B build',
        '-Ddisable_autoupdate=1',
        '-DCMAKE_BUILD_TYPE=Release',
        '-DCMAKE_INSTALL_PREFIX="/usr"',
        '-DTDESKTOP_API_TEST=ON',
        '-DDESKTOP_APP_USE_GLIBC_WRAPS=OFF',
        '-DDESKTOP_APP_USE_PACKAGED=ON',
        '-DDESKTOP_APP_USE_PACKAGED_GSL=OFF',
        '-DDESKTOP_APP_USE_PACKAGED_RLOTTIE=OFF',
        '-DDESKTOP_APP_USE_PACKAGED_VARIANT=OFF',
        '-DDESKTOP_APP_DISABLE_CRASH_REPORTS=ON',
        '-DTDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME=ON',
        '-DTDESKTOP_DISABLE_DESKTOP_FILE_GENERATION=ON',
        '-DTDESKTOP_USE_PACKAGED_TGVOIP=OFF',
        '-DDESKTOP_APP_SPECIAL_TARGET=""',
	'-DDESKTOP_APP_DISABLE_WAYLAND_INTEGRATION=OFF'
        '-DTDESKTOP_LAUNCHER_BASENAME="telegramdesktop"'
    ])

    cmaketools.configure(params)


def build():
    shelltools.cd("build")
    cmaketools.make("-j4")
    #mesontools.build()


def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #mesontools.install()
