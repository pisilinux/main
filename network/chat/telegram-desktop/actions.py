#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import mesontools


def setup():
    params = ' '.join([
        '-B build',
        '-G Ninja .',
        '-Ddisable_autoupdate=1',
        '-DCMAKE_BUILD_TYPE=Release',
        '-DTDESKTOP_API_TEST=ON',
        '-DDESKTOP_APP_USE_GLIBC_WRAPS=OFF',
        '-DDESKTOP_APP_USE_PACKAGED=ON',
        '-DDESKTOP_APP_USE_PACKAGED_RLOTTIE=OFF',
        '-DDESKTOP_APP_USE_PACKAGED_VARIANT=OFF',
        '-DDESKTOP_APP_DISABLE_CRASH_REPORTS=ON',
        '-DTDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME=ON',
        '-DTDESKTOP_DISABLE_DESKTOP_FILE_GENERATION=ON',
        '-DTDESKTOP_USE_PACKAGED_TGVOIP=OFF',
        '-DDESKTOP_APP_SPECIAL_TARGET=""',
        '-DTDESKTOP_LAUNCHER_BASENAME="telegramdesktop"'
    ])

    cmaketools.configure(params)


def build():
    mesontools.build()


def install():
    mesontools.install()
