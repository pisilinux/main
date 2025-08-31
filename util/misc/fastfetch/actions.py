#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("cmake -B build -S . \
		-DCMAKE_BUILD_TYPE='RelWithDebInfo' \
		-DCMAKE_INSTALL_PREFIX='/usr' \
		-DBUILD_FLASHFETCH='OFF' \
		-DBUILD_TESTS='ON' \
		-DENABLE_SQLITE3='ON' \
		-DENABLE_RPM='OFF' \
		-DENABLE_IMAGEMAGICK6='OFF' \
		-DENABLE_SYSTEM_YYJSON='OFF' \
		-DPACKAGES_DISABLE_APK='ON' \
		-DPACKAGES_DISABLE_DPKG='ON' \
		-DPACKAGES_DISABLE_EMERGE='ON' \
		-DPACKAGES_DISABLE_EOPKG='ON' \
		-DPACKAGES_DISABLE_GUIX='ON' \
		-DPACKAGES_DISABLE_LINGLONG='ON' \
		-DPACKAGES_DISABLE_LPKG='ON' \
		-DPACKAGES_DISABLE_LPKGBUILD='ON' \
		-DPACKAGES_DISABLE_OPKG='ON' \
		-DPACKAGES_DISABLE_PACSTALL='ON' \
		-DPACKAGES_DISABLE_PALUDIS='ON' \
		-DPACKAGES_DISABLE_PKG='ON' \
		-DPACKAGES_DISABLE_PKGTOOL='ON' \
		-DPACKAGES_DISABLE_RPM='ON' \
		-DPACKAGES_DISABLE_SORCERY='ON' \
		-DPACKAGES_DISABLE_XBPS='ON' \
		-Wno-dev")
    shelltools.system("cmake --build build")

def install():
    shelltools.system("DESTDIR=%s cmake --install build" % get.installDIR())

