#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools, shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    parameters = ' '.join([
        '-B build',
        '-DGSL_TEST=OFF',
        '-DCMAKE_EXE_LINKER_FLAGS="%s"' % get.LDFLAGS(),
        '-DCMAKE_BUILD_TYPE=Release'
    ])
    cmaketools.configure(parameters)


def build():
    shelltools.cd('build')
    cmaketools.make()


def install():
    shelltools.cd('build')
    cmaketools.install()

    pisitools.dodoc('../LICENSE')
