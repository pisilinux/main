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
        '-DRANGE_V3_TESTS=OFF',
        '-DRANGE_V3_HEADER_CHECKS=OFF',
        '-DRANGE_V3_EXAMPLES=OFF',
        '-DRANGE_V3_PERF=OFF'
    ])
    cmaketools.configure(parameters)


def build():
    shelltools.cd('build')
    cmaketools.make()


def install():
    shelltools.cd('build')
    cmaketools.install()

    pisitools.dodoc('../LICENSE.txt')
