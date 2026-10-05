#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system('cargo fetch --locked --target host-tuple')

def build():
    # shelltools.system('export RUSTFLAGS+=" -C link-arg=-fuse-ld=mold"')
    shelltools.system('cargo build --frozen --release --package mold-cli')


def install():
    shelltools.system("DESTDIR='%s' PREFIX=/usr ./install-mold.sh" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")
