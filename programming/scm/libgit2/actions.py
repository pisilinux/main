#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

i = ''.join([
    ' -DCMAKE_INSTALL_PREFIX=/usr',
    ' -DREGEX_BACKEND=pcre2',
    ' -DUSE_{HTTPS,SSH}=ON',
    ' -DUSE_HTTP_PARSER=llhttp',
    ' -Bbuild -G Ninja -L '
    ])

def setup():
    cmaketools.configure(i)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING")
