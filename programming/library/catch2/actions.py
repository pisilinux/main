#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, cmaketools, shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    parameters = ' '.join([
        '-B build',
        '-DCMAKE_INSTALL_LIBDIR=lib',
        '-DCATCH_USE_VALGRIND=OFF',
        '-DCATCH_BUILD_EXAMPLES=OFF',
        '-DCATCH_ENABLE_COVERAGE=OFF',
        '-DCATCH_ENABLE_WERROR=OFF',
        '-DBUILD_TESTING=ON'
    ])
    cmaketools.configure(parameters)


def build():
    shelltools.cd('build')
    autotools.make()


def check():
    shelltools.cd('build')
    autotools.make('test')


def install():
    shelltools.cd('build')
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
